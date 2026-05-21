import sqlite3
import os
from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'skincare.db')
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'schema.sql')


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    with open(SCHEMA_PATH, 'r') as f:
        conn.executescript(f.read())
    seed_products(conn)
    seed_doctors(conn)
    conn.commit()
    conn.close()


def seed_doctors(conn):
    cursor = conn.execute("SELECT COUNT(*) FROM doctors")
    if cursor.fetchone()[0] > 0:
        return

    doctors = [
        ("Dr. Priya Sharma", "priya@skincare.com", generate_password_hash("doctor123"), "Dermatology", 12),
        ("Dr. Arjun Mehta", "arjun@skincare.com", generate_password_hash("doctor123"), "Cosmetic Dermatology", 8),
        ("Dr. Sneha Reddy", "sneha@skincare.com", generate_password_hash("doctor123"), "Clinical Dermatology", 15),
    ]
    conn.executemany(
        "INSERT INTO doctors (name, email, password_hash, specialization, experience) VALUES (?, ?, ?, ?, ?)",
        doctors
    )


def seed_products(conn):
    cursor = conn.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] > 0:
        return

    products = [
        # CLEANSERS
        ("Gentle Foam Cleanser", "cleanser", 350, "all", "acne", "Salicylic Acid, Tea Tree Oil, Glycerin, Aloe Vera, Niacinamide"),
        ("Milky Hydrating Cleanser", "cleanser", 420, "dry", "dryness", "Ceramide NP, Hyaluronic Acid, Squalane, Glycerin, Shea Butter"),
        ("Oil Control Gel Wash", "cleanser", 299, "oily", "acne", "Salicylic Acid 2%, Zinc PCA, Neem Extract, Tea Tree Oil, Charcoal"),
        ("Brightening Vitamin C Wash", "cleanser", 480, "combination", "dark_spots", "Vitamin C, Kojic Acid, Licorice Extract, Glycerin, Turmeric"),
        ("Soothing Micellar Cleanser", "cleanser", 380, "all", "sensitivity", "Micellar Water, Chamomile, Centella Asiatica, Panthenol, Allantoin"),
        ("Anti-Aging Cream Cleanser", "cleanser", 550, "dry", "anti_aging", "Retinol, Peptides, Vitamin E, Jojoba Oil, Collagen"),
        ("Charcoal Deep Pore Cleanser", "cleanser", 320, "oily", "acne", "Activated Charcoal, Bentonite Clay, Tea Tree, Salicylic Acid, Witch Hazel"),

        # TONERS
        ("AHA Glow Toner", "toner", 550, "oily", "dullness", "Glycolic Acid 7%, Lactic Acid, Witch Hazel, Rose Water, Niacinamide"),
        ("Hydrating Rose Toner", "toner", 320, "dry", "dryness", "Rose Water, Hyaluronic Acid, Glycerin, Aloe Vera, Panthenol"),
        ("Niacinamide Pore Toner", "toner", 450, "combination", "acne", "Niacinamide 5%, Zinc PCA, Salicylic Acid, Green Tea, Witch Hazel"),
        ("Calming Centella Toner", "toner", 480, "all", "sensitivity", "Centella Asiatica, Madecassoside, Panthenol, Allantoin, Chamomile"),
        ("Brightening Licorice Toner", "toner", 390, "all", "dark_spots", "Licorice Root Extract, Alpha Arbutin, Vitamin C, Niacinamide, Hyaluronic Acid"),

        # SERUMS
        ("10% Niacinamide Serum", "serum", 599, "oily", "acne", "Niacinamide 10%, Zinc PCA, Hyaluronic Acid, Aloe Vera, Panthenol"),
        ("Vitamin C 20% Serum", "serum", 750, "all", "dark_spots", "L-Ascorbic Acid 20%, Vitamin E, Ferulic Acid, Hyaluronic Acid, Squalane"),
        ("Hyaluronic Acid Serum", "serum", 680, "dry", "dryness", "Hyaluronic Acid 2%, Sodium Hyaluronate, Glycerin, Panthenol, Ceramides"),
        ("Retinol 0.5% Serum", "serum", 890, "combination", "anti_aging", "Retinol 0.5%, Squalane, Vitamin E, Jojoba Oil, Peptides"),
        ("Alpha Arbutin Serum", "serum", 520, "all", "dark_spots", "Alpha Arbutin 2%, Niacinamide, Hyaluronic Acid, Licorice, Vitamin C"),
        ("Peptide Firming Serum", "serum", 950, "all", "anti_aging", "Matrixyl 3000, Argireline, Hyaluronic Acid, Vitamin E, Squalane"),
        ("BHA Exfoliating Serum", "serum", 620, "oily", "acne", "Salicylic Acid 2%, Niacinamide, Green Tea, Tea Tree, Centella"),
        ("Azelaic Acid Serum", "serum", 550, "combination", "dark_spots", "Azelaic Acid 10%, Niacinamide, Vitamin C, Licorice Extract, Allantoin"),

        # MOISTURIZERS
        ("Oil-Free Gel Moisturizer", "moisturizer", 450, "oily", "acne", "Hyaluronic Acid, Niacinamide, Aloe Vera, Green Tea, Centella Asiatica"),
        ("Intense Hydration Cream", "moisturizer", 520, "dry", "dryness", "Shea Butter, Ceramide NP, Squalane, Jojoba Oil, Hyaluronic Acid"),
        ("Barrier Repair Moisturizer", "moisturizer", 680, "all", "sensitivity", "Ceramide AP, Cholesterol, Phytosphingosine, Niacinamide, Squalane"),
        ("Brightening Day Cream", "moisturizer", 550, "combination", "dark_spots", "Vitamin C, Niacinamide, Alpha Arbutin, SPF 15, Licorice Extract"),
        ("Anti-Aging Night Cream", "moisturizer", 780, "all", "anti_aging", "Retinol, Peptides, Hyaluronic Acid, Vitamin E, Collagen"),
        ("Matte Finish Moisturizer", "moisturizer", 350, "oily", "dullness", "Niacinamide, Green Tea, Salicylic Acid, Zinc PCA, Aloe Vera"),
        ("Collagen Boost Cream", "moisturizer", 890, "dry", "anti_aging", "Marine Collagen, Peptides, Hyaluronic Acid, Vitamin C, Retinol"),

        # SUNSCREENS
        ("Matte Sunscreen SPF 50", "sunscreen", 450, "oily", "acne", "Zinc Oxide, Titanium Dioxide, Niacinamide, Silica, Green Tea"),
        ("Hydrating Sunscreen SPF 50+", "sunscreen", 520, "dry", "dryness", "Hyaluronic Acid, Vitamin E, Squalane, Zinc Oxide, Titanium Dioxide"),
        ("Tinted Sunscreen SPF 40", "sunscreen", 600, "combination", "dark_spots", "Iron Oxides, Zinc Oxide, Niacinamide, Vitamin C, Titanium Dioxide"),
        ("Gel Sunscreen SPF 50", "sunscreen", 380, "all", "dullness", "Zinc Oxide, Aloe Vera, Vitamin E, Green Tea, Hyaluronic Acid"),
        ("Anti-Aging Sunscreen SPF 50", "sunscreen", 700, "all", "anti_aging", "Zinc Oxide, Vitamin C, Peptides, Hyaluronic Acid, Niacinamide"),
        ("Sensitive Skin Sunscreen SPF 50+", "sunscreen", 550, "all", "sensitivity", "Zinc Oxide, Centella Asiatica, Ceramides, Allantoin, Panthenol"),

        # EXFOLIANTS
        ("AHA 10% Exfoliating Gel", "exfoliant", 650, "combination", "dullness", "Glycolic Acid 10%, Lactic Acid, Aloe Vera, Hyaluronic Acid, Panthenol"),
        ("BHA 2% Liquid Exfoliant", "exfoliant", 580, "oily", "acne", "Salicylic Acid 2%, Green Tea, Niacinamide, Aloe Vera, Centella Asiatica"),
        ("PHA Gentle Exfoliator", "exfoliant", 520, "dry", "sensitivity", "Gluconolactone, Lactobionic Acid, Hyaluronic Acid, Ceramides, Allantoin"),
        ("Enzyme Peel Exfoliant", "exfoliant", 480, "all", "dullness", "Papain, Bromelain, Glycerin, Aloe Vera, Vitamin C"),
        ("Mandelic Acid 5% Serum", "exfoliant", 550, "all", "dark_spots", "Mandelic Acid 5%, Niacinamide, Hyaluronic Acid, Aloe Vera, Licorice Extract"),
        ("Retexturizing AHA Peel", "exfoliant", 750, "combination", "anti_aging", "Glycolic Acid 15%, Lactic Acid, Salicylic Acid, Peptides, Centella"),
        ("Daily Microfoliant Powder", "exfoliant", 420, "oily", "dullness", "Rice Bran, Papain, Salicylic Acid, Niacinamide, Kaolin Clay"),
    ]

    conn.executemany(
        "INSERT INTO products (name, category, price, skin_type, concern, ingredients) VALUES (?, ?, ?, ?, ?, ?)",
        products
    )
