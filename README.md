# GlowGuide — Smart Skincare Recommendation System


A fully functional offline skincare platform built with Flask, SQLite, and vanilla JavaScript.

### Repository Access
To clone or download this repository:
```bash
git clone https://github.com/Drushyagowda17/Smart-Skincare-Recommendation-System.git
cd Smart-Skincare-Recommendation-System/skincare_app
```


## Features

- **Smart Skin Quiz** — 10-question personalized analysis with AM/PM routines
- **Recommendation Engine** — 18 rule-based mappings (3 skin types × 6 concerns)
- **Ingredient Decoder** — Paste any ingredient list for safety analysis + conflict detection
- **Routine Builder** — Drag-and-drop AM/PM routine builder with layering tips
- **Product Comparison** — Side-by-side comparison of 2-3 products
- **Progress Tracker** — Before/after photo upload and timeline
- **Skin Diary** — Track sleep, water, stress, diet with Chart.js trends
- **Doctor Consultation** — Submit questions, get responses from doctors
- **Myths vs Facts** — 10 debunked skincare myths
- **Ayurveda Guide** — Traditional ingredients with research notes
- **Hyperpigmentation Hub** — PIH, sun damage, treatment protocols
- **City Climate Filter** — Location-based skincare adjustments
- **Admin Dashboard** — Stats, product management, Chart.js visualizations
- **Dark Mode** — Full dark theme with smooth transitions
- **4 User Roles** — Guest, User, Doctor, Admin

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, Bootstrap 5, Vanilla JavaScript
- **Database:** SQLite (sqlite3)
- **Charts:** Chart.js (CDN)
- **Security:** werkzeug.security (password hashing, sessions)

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Seed Data

- **40+ products** across 6 categories (cleansers, toners, serums, moisturizers, sunscreens, exfoliants)
- **3 doctors** pre-seeded for consultations

## Doctor Login Credentials

| Doctor | Email | Password |
|--------|-------|----------|
| Dr. Priya Sharma | priya@skincare.com | doctor123 |
| Dr. Arjun Mehta | arjun@skincare.com | doctor123 |
| Dr. Sneha Reddy | sneha@skincare.com | doctor123 |

## Admin Access

Register any user account, then visit `/admin`.

## Folder Structure

```
skincare_app/
├── app.py                  # Main Flask application
├── database.py             # Database initialization + seed data
├── recommender.py           # 18-rule recommendation engine
├── ingredient_decoder.py    # 50+ ingredient database + conflicts
├── reminders.py             # Reminder management
├── utils.py                 # Decorators + helpers
├── schema.sql               # Database schema
├── requirements.txt
├── README.md
├── templates/               # 18 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── results.html
│   ├── login.html
│   ├── register.html
│   ├── doctor_login.html
│   ├── doctor_dashboard.html
│   ├── doctor_patients.html
│   ├── ingredient_decoder.html
│   ├── routine_builder.html
│   ├── compare.html
│   ├── progress.html
│   ├── myths.html
│   ├── ayurveda.html
│   ├── hyperpigmentation.html
│   ├── saved_routines.html
│   ├── skin_diary.html
│   ├── consult.html
│   ├── admin.html
│   └── error.html
├── static/
│   ├── css/style.css        # Complete design system
│   ├── js/main.js           # All client-side logic
│   ├── uploads/progress/    # User progress photos
│   └── images/
└── skincare.db              # SQLite database (auto-created)
```
