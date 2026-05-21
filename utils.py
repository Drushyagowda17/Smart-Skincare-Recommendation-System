import functools
from flask import session, redirect, url_for, flash


def login_required(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this feature.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def doctor_login_required(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if 'doctor_id' not in session:
            flash('Please login as a doctor to access this page.', 'warning')
            return redirect(url_for('doctor_login'))
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Admin access required.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def get_climate_tips(city):
    climate_map = {
        'bengaluru': {
            'climate': 'Moderate, pleasant',
            'humidity': 'Medium',
            'tips': [
                'Lightweight moisturizer is sufficient for most of the year.',
                'SPF 30+ daily even in overcast weather.',
                'Use a gentle cleanser — no need for heavy oil control.',
                'Hyaluronic acid works well in this humidity level.'
            ]
        },
        'delhi': {
            'climate': 'Extreme — hot summers, cold winters, high pollution',
            'humidity': 'Low to Medium',
            'tips': [
                'Double cleanse to remove pollution particles.',
                'Use Vitamin C serum to fight pollution damage.',
                'Heavy moisturizer in winter, gel-based in summer.',
                'SPF 50 is essential due to high UV index.',
                'Antioxidant serums are critical for pollution defense.'
            ]
        },
        'mumbai': {
            'climate': 'Tropical, hot and humid',
            'humidity': 'High',
            'tips': [
                'Gel-based and water-based products work best.',
                'Avoid heavy creams — they clog pores in humidity.',
                'Use niacinamide to control excess oil.',
                'Matte sunscreen to prevent greasy feeling.',
                'Salicylic acid cleanser helps with humidity-related breakouts.'
            ]
        },
        'hyderabad': {
            'climate': 'Hot and semi-arid',
            'humidity': 'Low to Medium',
            'tips': [
                'Hydrating toner is essential in dry weather.',
                'Use ceramide-based moisturizers for barrier repair.',
                'SPF 50 mandatory — high UV exposure.',
                'Lightweight serums absorb better in this climate.',
                'Drink extra water to compensate for dry air.'
            ]
        },
        'chennai': {
            'climate': 'Hot and humid tropical',
            'humidity': 'Very High',
            'tips': [
                'Non-comedogenic products only — humidity clogs pores.',
                'Water-resistant sunscreen for sweat.',
                'Gel moisturizers prevent sticky feeling.',
                'BHA-based cleanser for oily T-zone.',
                'Keep blotting papers handy for midday oil control.'
            ]
        },
        'kolkata': {
            'climate': 'Tropical wet, hot and humid',
            'humidity': 'High',
            'tips': [
                'Light, water-based skincare routine is best.',
                'Niacinamide serum for oil and pore control.',
                'Gel sunscreen that does not feel heavy.',
                'Clay masks weekly to manage excess sebum.',
                'Avoid heavy occlusives in summer months.'
            ]
        }
    }
    return climate_map.get(city.lower(), {
        'climate': 'Variable',
        'humidity': 'Medium',
        'tips': ['Use SPF 30+ daily.', 'Adjust routine based on seasonal changes.']
    })


def format_price(price):
    return f"₹{price:,.0f}"


def get_skin_type_label(skin_type):
    labels = {
        'oily': 'Oily Skin',
        'dry': 'Dry Skin',
        'combination': 'Combination Skin',
        'all': 'All Skin Types'
    }
    return labels.get(skin_type, skin_type.title())


def get_concern_label(concern):
    labels = {
        'acne': 'Acne & Breakouts',
        'dark_spots': 'Dark Spots & Pigmentation',
        'dullness': 'Dullness & Uneven Tone',
        'dryness': 'Dryness & Dehydration',
        'anti_aging': 'Anti-Aging & Wrinkles',
        'sensitivity': 'Sensitivity & Redness'
    }
    return labels.get(concern, concern.replace('_', ' ').title())
