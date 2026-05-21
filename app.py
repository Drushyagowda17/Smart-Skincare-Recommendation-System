import os
import json
from datetime import datetime
from flask import (Flask, render_template, request, redirect, url_for,
                   session, flash, jsonify)
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from database import get_db, init_db
from recommender import get_recommendation
from ingredient_decoder import decode_ingredients, check_conflicts
from reminders import get_reminders, save_reminder
from utils import (login_required, doctor_login_required, admin_required,
                   format_price, get_skin_type_label, get_concern_label, get_climate_tips)

app = Flask(__name__)
app.secret_key = 'skincare_secret_key_2024_production'
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads', 'progress')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'images'), exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.context_processor
def utility_processor():
    return {
        'format_price': format_price,
        'get_skin_type_label': get_skin_type_label,
        'get_concern_label': get_concern_label,
        'now': datetime.now()
    }


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_code=404, error_message='Page not found'), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('error.html', error_code=500, error_message='Internal server error'), 500


@app.route('/')
def index():
    db = get_db()
    products = db.execute("SELECT * FROM products ORDER BY RANDOM() LIMIT 8").fetchall()
    product_count = db.execute("SELECT COUNT(*) FROM products").fetchone()[0]
    user_count = db.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    doctor_count = db.execute("SELECT COUNT(*) FROM doctors").fetchone()[0]
    db.close()
    return render_template('index.html', featured_products=products,
                           product_count=product_count, user_count=user_count, doctor_count=doctor_count)


@app.route('/recommend', methods=['POST'])
def recommend():
    skin_type = request.form.get('skin_type', 'combination')
    age = request.form.get('age', '25')
    gender = request.form.get('gender', 'female')
    city = request.form.get('city', 'bengaluru')
    climate = request.form.get('climate', 'moderate')
    budget = request.form.get('budget', 'medium')
    water = request.form.get('water', '8')
    sleep = request.form.get('sleep', '7')
    sensitivity = request.form.get('sensitivity', 'no')
    routine_level = request.form.get('routine_level', 'intermediate')
    concern = request.form.get('concern', 'acne')

    if sensitivity == 'yes':
        concern = 'sensitivity'

    db = get_db()
    result = get_recommendation(skin_type, concern, budget, city, age, gender, water, sleep, routine_level, db)

    all_products = db.execute(
        "SELECT p.*, COALESCE(AVG(r.rating), 0) as avg_rating, COUNT(r.id) as rating_count "
        "FROM products p LEFT JOIN product_ratings r ON p.id = r.product_id "
        "WHERE (p.skin_type = ? OR p.skin_type = 'all') AND p.concern = ? "
        "GROUP BY p.id ORDER BY avg_rating DESC",
        (skin_type, concern)
    ).fetchall()
    db.close()

    return render_template('results.html',
                           result=result,
                           skin_type=skin_type,
                           concern=concern,
                           budget=budget,
                           city=city,
                           age=age,
                           gender=gender,
                           water=water,
                           sleep=sleep,
                           routine_level=routine_level,
                           all_products=all_products)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm_password', '')

        if not username or not email or not password:
            flash('All fields are required.', 'danger')
            return render_template('register.html')

        if password != confirm:
            flash('Passwords do not match.', 'danger')
            return render_template('register.html')

        if len(password) < 6:
            flash('Password must be at least 6 characters.', 'danger')
            return render_template('register.html')

        db = get_db()
        existing = db.execute("SELECT id FROM users WHERE username = ? OR email = ?", (username, email)).fetchone()
        if existing:
            flash('Username or email already exists.', 'danger')
            db.close()
            return render_template('register.html')

        db.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
            (username, email, generate_password_hash(password))
        )
        db.commit()
        db.close()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username = ? OR email = ?", (username, username)).fetchone()
        db.close()

        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash(f'Welcome back, {user["username"]}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('doctor_id', None)
    session.pop('doctor_name', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('index'))


@app.route('/save_routine', methods=['POST'])
@login_required
def save_routine():
    skin_type = request.form.get('skin_type', '')
    concern = request.form.get('concern', '')
    budget = request.form.get('budget', '')
    morning = request.form.get('morning_routine', '')
    night = request.form.get('night_routine', '')

    db = get_db()
    db.execute(
        "INSERT INTO saved_routines (user_id, skin_type, concern, budget, morning_routine, night_routine) VALUES (?, ?, ?, ?, ?, ?)",
        (session['user_id'], skin_type, concern, budget, morning, night)
    )
    db.commit()
    db.close()

    flash('Routine saved successfully!', 'success')
    return redirect(url_for('saved_routines'))


@app.route('/saved_routines')
@login_required
def saved_routines():
    db = get_db()
    routines = db.execute(
        "SELECT * FROM saved_routines WHERE user_id = ? ORDER BY created_at DESC",
        (session['user_id'],)
    ).fetchall()
    db.close()
    return render_template('saved_routines.html', routines=routines)


@app.route('/delete_routine/<int:routine_id>', methods=['POST'])
@login_required
def delete_routine(routine_id):
    db = get_db()
    db.execute("DELETE FROM saved_routines WHERE id = ? AND user_id = ?", (routine_id, session['user_id']))
    db.commit()
    db.close()
    flash('Routine deleted.', 'info')
    return redirect(url_for('saved_routines'))


@app.route('/ingredient-decoder', methods=['GET', 'POST'])
def ingredient_decoder():
    found = []
    not_found = []
    conflicts = []
    raw_text = ''

    if request.method == 'POST':
        raw_text = request.form.get('ingredients', '')
        if raw_text.strip():
            found, not_found = decode_ingredients(raw_text)
            conflicts = check_conflicts(raw_text)

    return render_template('ingredient_decoder.html', found=found, not_found=not_found,
                           conflicts=conflicts, raw_text=raw_text)


@app.route('/routine-builder')
def routine_builder():
    db = get_db()
    products = db.execute("SELECT * FROM products ORDER BY category, name").fetchall()
    db.close()
    return render_template('routine_builder.html', products=products)


@app.route('/compare', methods=['GET', 'POST'])
def compare():
    db = get_db()
    products = db.execute(
        "SELECT p.*, COALESCE(AVG(r.rating), 0) as avg_rating, COUNT(r.id) as rating_count "
        "FROM products p LEFT JOIN product_ratings r ON p.id = r.product_id "
        "GROUP BY p.id ORDER BY p.name"
    ).fetchall()

    selected = []
    if request.method == 'POST':
        product_ids = request.form.getlist('product_ids')
        if len(product_ids) >= 2:
            placeholders = ','.join('?' * len(product_ids))
            selected = db.execute(
                f"SELECT p.*, COALESCE(AVG(r.rating), 0) as avg_rating, COUNT(r.id) as rating_count "
                f"FROM products p LEFT JOIN product_ratings r ON p.id = r.product_id "
                f"WHERE p.id IN ({placeholders}) GROUP BY p.id",
                product_ids
            ).fetchall()

    db.close()
    return render_template('compare.html', products=products, selected=selected)


@app.route('/progress', methods=['GET', 'POST'])
@login_required
def progress():
    db = get_db()

    if request.method == 'POST':
        note = request.form.get('note', '')
        file = request.files.get('image')

        if file and allowed_file(file.filename):
            filename = secure_filename(f"{session['user_id']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{file.filename}")
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            db.execute(
                "INSERT INTO progress_images (user_id, image, note) VALUES (?, ?, ?)",
                (session['user_id'], filename, note)
            )
            db.commit()
            flash('Progress photo uploaded!', 'success')
        elif file:
            flash('Invalid file type. Use PNG, JPG, JPEG, GIF, or WEBP.', 'danger')

    images = db.execute(
        "SELECT * FROM progress_images WHERE user_id = ? ORDER BY created_at DESC",
        (session['user_id'],)
    ).fetchall()
    db.close()
    return render_template('progress.html', images=images)


@app.route('/delete_progress/<int:image_id>', methods=['POST'])
@login_required
def delete_progress(image_id):
    db = get_db()
    image = db.execute("SELECT * FROM progress_images WHERE id = ? AND user_id = ?",
                       (image_id, session['user_id'])).fetchone()
    if image:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], image['image'])
        if os.path.exists(filepath):
            os.remove(filepath)
        db.execute("DELETE FROM progress_images WHERE id = ?", (image_id,))
        db.commit()
        flash('Progress image deleted.', 'info')
    db.close()
    return redirect(url_for('progress'))


@app.route('/myths')
def myths():
    return render_template('myths.html')


@app.route('/ayurveda')
def ayurveda():
    return render_template('ayurveda.html')


@app.route('/hyperpigmentation')
def hyperpigmentation():
    return render_template('hyperpigmentation.html')


@app.route('/consult', methods=['GET', 'POST'])
@login_required
def consult():
    db = get_db()

    if request.method == 'POST':
        question = request.form.get('question', '').strip()
        doctor_id = request.form.get('doctor_id')

        if question:
            db.execute(
                "INSERT INTO consultations (user_id, doctor_id, question) VALUES (?, ?, ?)",
                (session['user_id'], doctor_id if doctor_id else None, question)
            )
            db.commit()
            flash('Your consultation request has been submitted!', 'success')

    doctors = db.execute("SELECT * FROM doctors").fetchall()
    consultations = db.execute(
        "SELECT c.*, d.name as doctor_name FROM consultations c "
        "LEFT JOIN doctors d ON c.doctor_id = d.id "
        "WHERE c.user_id = ? ORDER BY c.created_at DESC",
        (session['user_id'],)
    ).fetchall()
    db.close()
    return render_template('consult.html', doctors=doctors, consultations=consultations)


@app.route('/doctor/login', methods=['GET', 'POST'])
def doctor_login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        db = get_db()
        doctor = db.execute("SELECT * FROM doctors WHERE email = ?", (email,)).fetchone()
        db.close()

        if doctor and check_password_hash(doctor['password_hash'], password):
            session['doctor_id'] = doctor['id']
            session['doctor_name'] = doctor['name']
            flash(f'Welcome, {doctor["name"]}!', 'success')
            return redirect(url_for('doctor_dashboard'))
        else:
            flash('Invalid doctor credentials.', 'danger')

    return render_template('doctor_login.html')


@app.route('/doctor/dashboard')
@doctor_login_required
def doctor_dashboard():
    db = get_db()
    pending = db.execute(
        "SELECT c.*, u.username FROM consultations c "
        "JOIN users u ON c.user_id = u.id "
        "WHERE (c.doctor_id = ? OR c.doctor_id IS NULL) AND c.status = 'pending' "
        "ORDER BY c.created_at DESC",
        (session['doctor_id'],)
    ).fetchall()

    active = db.execute(
        "SELECT c.*, u.username FROM consultations c "
        "JOIN users u ON c.user_id = u.id "
        "WHERE c.doctor_id = ? AND c.status = 'approved' "
        "ORDER BY c.created_at DESC",
        (session['doctor_id'],)
    ).fetchall()

    completed = db.execute(
        "SELECT c.*, u.username FROM consultations c "
        "JOIN users u ON c.user_id = u.id "
        "WHERE c.doctor_id = ? AND c.status = 'completed' "
        "ORDER BY c.created_at DESC LIMIT 20",
        (session['doctor_id'],)
    ).fetchall()

    stats = {
        'pending': len(pending),
        'active': len(active),
        'completed': len(completed),
        'total': len(pending) + len(active) + len(completed)
    }

    db.close()
    return render_template('doctor_dashboard.html', pending=pending, active=active,
                           completed=completed, stats=stats)


@app.route('/doctor/patients')
@doctor_login_required
def doctor_patients():
    db = get_db()
    patients = db.execute(
        "SELECT DISTINCT u.id, u.username, u.email, u.created_at, "
        "COUNT(c.id) as consult_count "
        "FROM users u JOIN consultations c ON u.id = c.user_id "
        "WHERE c.doctor_id = ? "
        "GROUP BY u.id ORDER BY u.username",
        (session['doctor_id'],)
    ).fetchall()
    db.close()
    return render_template('doctor_patients.html', patients=patients)


@app.route('/doctor/respond', methods=['POST'])
@doctor_login_required
def doctor_respond():
    consult_id = request.form.get('consult_id')
    response = request.form.get('response', '').strip()
    action = request.form.get('action', 'approve')

    db = get_db()
    if action == 'approve':
        db.execute(
            "UPDATE consultations SET doctor_id = ?, status = 'approved' WHERE id = ?",
            (session['doctor_id'], consult_id)
        )
        flash('Consultation approved.', 'success')
    elif action == 'respond':
        db.execute(
            "UPDATE consultations SET doctor_response = ?, status = 'completed' WHERE id = ?",
            (response, consult_id)
        )
        flash('Response sent to patient.', 'success')
    elif action == 'complete':
        db.execute(
            "UPDATE consultations SET status = 'completed' WHERE id = ?",
            (consult_id,)
        )
        flash('Consultation marked as completed.', 'success')

    db.commit()
    db.close()
    return redirect(url_for('doctor_dashboard'))


@app.route('/doctor/logout')
def doctor_logout():
    session.pop('doctor_id', None)
    session.pop('doctor_name', None)
    flash('Doctor logged out.', 'info')
    return redirect(url_for('index'))


@app.route('/skin-diary', methods=['GET', 'POST'])
@login_required
def skin_diary():
    db = get_db()

    if request.method == 'POST':
        sleep_hours = request.form.get('sleep_hours', 7)
        water_intake = request.form.get('water_intake', 8)
        stress_level = request.form.get('stress_level', 5)
        diet = request.form.get('diet', '')
        skin_status = request.form.get('skin_status', '')
        notes = request.form.get('notes', '')

        db.execute(
            "INSERT INTO skin_diary (user_id, sleep_hours, water_intake, stress_level, diet, skin_status, notes) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (session['user_id'], sleep_hours, water_intake, stress_level, diet, skin_status, notes)
        )
        db.commit()
        flash('Diary entry saved!', 'success')

    entries = db.execute(
        "SELECT * FROM skin_diary WHERE user_id = ? ORDER BY created_at DESC LIMIT 30",
        (session['user_id'],)
    ).fetchall()
    db.close()
    return render_template('skin_diary.html', entries=entries)


@app.route('/rate/<int:product_id>', methods=['POST'])
@login_required
def rate_product(product_id):
    rating = request.form.get('rating', type=int)
    if not rating or rating < 1 or rating > 5:
        return jsonify({'success': False, 'message': 'Invalid rating'}), 400

    db = get_db()
    existing = db.execute(
        "SELECT id FROM product_ratings WHERE product_id = ? AND user_id = ?",
        (product_id, session['user_id'])
    ).fetchone()

    if existing:
        db.execute(
            "UPDATE product_ratings SET rating = ? WHERE id = ?",
            (rating, existing['id'])
        )
    else:
        db.execute(
            "INSERT INTO product_ratings (product_id, user_id, rating) VALUES (?, ?, ?)",
            (product_id, session['user_id'], rating)
        )

    db.commit()

    avg = db.execute(
        "SELECT COALESCE(AVG(rating), 0) as avg, COUNT(*) as count FROM product_ratings WHERE product_id = ?",
        (product_id,)
    ).fetchone()
    db.close()

    return jsonify({
        'success': True,
        'avg_rating': round(avg['avg'], 1),
        'rating_count': avg['count'],
        'message': 'Rating submitted!'
    })


@app.route('/admin')
@admin_required
def admin():
    db = get_db()

    products = db.execute(
        "SELECT p.*, COALESCE(AVG(r.rating), 0) as avg_rating, COUNT(r.id) as rating_count "
        "FROM products p LEFT JOIN product_ratings r ON p.id = r.product_id "
        "GROUP BY p.id ORDER BY p.name"
    ).fetchall()

    users = db.execute("SELECT * FROM users ORDER BY created_at DESC").fetchall()
    doctors = db.execute("SELECT * FROM doctors ORDER BY name").fetchall()

    consultations = db.execute(
        "SELECT c.*, u.username, d.name as doctor_name "
        "FROM consultations c "
        "JOIN users u ON c.user_id = u.id "
        "LEFT JOIN doctors d ON c.doctor_id = d.id "
        "ORDER BY c.created_at DESC LIMIT 50"
    ).fetchall()

    ratings = db.execute(
        "SELECT r.*, p.name as product_name, u.username "
        "FROM product_ratings r "
        "JOIN products p ON r.product_id = p.id "
        "JOIN users u ON r.user_id = u.id "
        "ORDER BY r.id DESC LIMIT 50"
    ).fetchall()

    stats = {
        'total_products': db.execute("SELECT COUNT(*) FROM products").fetchone()[0],
        'total_users': db.execute("SELECT COUNT(*) FROM users").fetchone()[0],
        'total_doctors': db.execute("SELECT COUNT(*) FROM doctors").fetchone()[0],
        'total_consultations': db.execute("SELECT COUNT(*) FROM consultations").fetchone()[0],
        'pending_consultations': db.execute("SELECT COUNT(*) FROM consultations WHERE status='pending'").fetchone()[0],
        'total_ratings': db.execute("SELECT COUNT(*) FROM product_ratings").fetchone()[0],
        'total_routines': db.execute("SELECT COUNT(*) FROM saved_routines").fetchone()[0],
        'total_diary_entries': db.execute("SELECT COUNT(*) FROM skin_diary").fetchone()[0],
        'category_counts': {},
        'concern_counts': {},
        'skin_type_counts': {}
    }

    for row in db.execute("SELECT category, COUNT(*) as cnt FROM products GROUP BY category").fetchall():
        stats['category_counts'][row['category']] = row['cnt']

    for row in db.execute("SELECT concern, COUNT(*) as cnt FROM products GROUP BY concern").fetchall():
        stats['concern_counts'][row['concern']] = row['cnt']

    for row in db.execute("SELECT skin_type, COUNT(*) as cnt FROM products GROUP BY skin_type").fetchall():
        stats['skin_type_counts'][row['skin_type']] = row['cnt']

    db.close()
    return render_template('admin.html', products=products, users=users, doctors=doctors,
                           consultations=consultations, ratings=ratings, stats=stats)


@app.route('/admin/add_product', methods=['POST'])
@admin_required
def add_product():
    name = request.form.get('name', '').strip()
    category = request.form.get('category', '')
    price = request.form.get('price', type=float)
    skin_type = request.form.get('skin_type', '')
    concern = request.form.get('concern', '')
    ingredients = request.form.get('ingredients', '')

    if not all([name, category, price, skin_type, concern, ingredients]):
        flash('All fields are required.', 'danger')
        return redirect(url_for('admin'))

    db = get_db()
    db.execute(
        "INSERT INTO products (name, category, price, skin_type, concern, ingredients) VALUES (?, ?, ?, ?, ?, ?)",
        (name, category, price, skin_type, concern, ingredients)
    )
    db.commit()
    db.close()

    flash(f'Product "{name}" added successfully!', 'success')
    return redirect(url_for('admin'))


@app.route('/admin/delete_product/<int:product_id>', methods=['POST'])
@admin_required
def delete_product(product_id):
    db = get_db()
    db.execute("DELETE FROM product_ratings WHERE product_id = ?", (product_id,))
    db.execute("DELETE FROM products WHERE id = ?", (product_id,))
    db.commit()
    db.close()
    flash('Product deleted.', 'info')
    return redirect(url_for('admin'))


@app.route('/admin/add_doctor', methods=['POST'])
@admin_required
def add_doctor():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')
    specialization = request.form.get('specialization', '').strip()
    experience_raw = request.form.get('experience', '')

    if not all([name, email, password, specialization, experience_raw]):
        flash('All fields are required.', 'danger')
        return redirect(url_for('admin'))

    try:
        experience = int(experience_raw)
        if experience < 0:
            raise ValueError
    except (ValueError, TypeError):
        flash('Experience must be a non-negative number.', 'danger')
        return redirect(url_for('admin'))

    if len(password) < 6:
        flash('Password must be at least 6 characters.', 'danger')
        return redirect(url_for('admin'))

    db = get_db()
    existing = db.execute("SELECT id FROM doctors WHERE email = ?", (email,)).fetchone()
    if existing:
        flash('Email already registered for a doctor.', 'danger')
        db.close()
        return redirect(url_for('admin'))

    db.execute(
        "INSERT INTO doctors (name, email, password_hash, specialization, experience) VALUES (?, ?, ?, ?, ?)",
        (name, email, generate_password_hash(password), specialization, experience)
    )
    db.commit()
    db.close()

    flash(f'Doctor account for "{name}" created successfully!', 'success')
    return redirect(url_for('admin'))


@app.route('/admin/delete_doctor/<int:doctor_id>', methods=['POST'])
@admin_required
def delete_doctor(doctor_id):
    db = get_db()
    db.execute("UPDATE consultations SET doctor_id = NULL WHERE doctor_id = ?", (doctor_id,))
    db.execute("DELETE FROM doctors WHERE id = ?", (doctor_id,))
    db.commit()
    db.close()
    flash('Doctor deleted.', 'info')
    return redirect(url_for('admin'))


@app.route('/api/diary-data')
@login_required
def diary_data():
    db = get_db()
    entries = db.execute(
        "SELECT * FROM skin_diary WHERE user_id = ? ORDER BY created_at ASC LIMIT 30",
        (session['user_id'],)
    ).fetchall()
    db.close()

    data = {
        'labels': [],
        'sleep': [],
        'water': [],
        'stress': []
    }
    for e in entries:
        data['labels'].append(e['created_at'][:10] if e['created_at'] else '')
        data['sleep'].append(e['sleep_hours'])
        data['water'].append(e['water_intake'])
        data['stress'].append(e['stress_level'])

    return jsonify(data)


@app.route('/api/reminders', methods=['GET', 'POST'])
@login_required
def api_reminders():
    db = get_db()
    if request.method == 'POST':
        data = request.get_json()
        save_reminder(session['user_id'], data.get('routine_type', 'morning'),
                      data.get('time', '07:00'), data.get('enabled', 1), db)
        db.close()
        return jsonify({'success': True})

    reminders = get_reminders(session['user_id'], db)
    db.close()
    return jsonify(reminders)


if __name__ == '__main__':
    init_db()
    print("\n" + "=" * 60)
    print("  SMART SKINCARE RECOMMENDATION SYSTEM")
    print("  Running at: http://127.0.0.1:5000")
    print("=" * 60)
    print("\n  Doctor Logins:")
    print("    priya@skincare.com / doctor123")
    print("    arjun@skincare.com / doctor123")
    print("    sneha@skincare.com / doctor123")
    print("\n  Admin: Register any user, then visit /admin")
    print("=" * 60 + "\n")
    app.run(debug=True, port=5000)
