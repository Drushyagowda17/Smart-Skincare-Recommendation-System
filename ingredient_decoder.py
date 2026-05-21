INGREDIENT_DATABASE = {
    'retinol': {
        'name': 'Retinol (Vitamin A)',
        'purpose': 'Anti-aging, cell turnover, reduces fine lines and wrinkles',
        'safety': 'Moderate — Start with low concentration (0.25-0.5%). Can cause irritation, dryness, and sun sensitivity.',
        'best_for': ['Anti-Aging', 'Acne', 'Dark Spots'],
        'warnings': ['Avoid during pregnancy', 'Always use sunscreen', 'Do not mix with AHA/BHA initially', 'Start slow — 2x per week'],
        'rating': 4,
        'category': 'Active'
    },
    'niacinamide': {
        'name': 'Niacinamide (Vitamin B3)',
        'purpose': 'Pore minimizing, oil control, brightening, barrier repair',
        'safety': 'Very Safe — Well tolerated at 2-10% concentration by most skin types.',
        'best_for': ['Oily Skin', 'Acne', 'Dark Spots', 'All Skin Types'],
        'warnings': ['May cause flushing at very high concentrations (>10%)', 'Some formulations may pill under makeup'],
        'rating': 5,
        'category': 'Active'
    },
    'vitamin c': {
        'name': 'Vitamin C (L-Ascorbic Acid)',
        'purpose': 'Brightening, antioxidant protection, collagen synthesis, fades dark spots',
        'safety': 'Safe — Can cause tingling in sensitive skin. Use 10-20% concentration.',
        'best_for': ['Dark Spots', 'Dullness', 'Anti-Aging', 'Sun Damage'],
        'warnings': ['Unstable — store in dark, cool place', 'Can oxidize and turn yellow/brown', 'Use in AM before sunscreen', 'May not pair well with certain retinol products'],
        'rating': 5,
        'category': 'Active'
    },
    'aha': {
        'name': 'AHA (Alpha Hydroxy Acid)',
        'purpose': 'Chemical exfoliation, removes dead skin cells, brightens complexion',
        'safety': 'Moderate — Start with low percentages (5-8%). Increases sun sensitivity.',
        'best_for': ['Dullness', 'Dark Spots', 'Anti-Aging', 'Dry Skin'],
        'warnings': ['Do NOT mix with Retinol', 'Always use SPF the next day', 'Over-exfoliation can damage skin barrier', 'Use 2-3 times per week max'],
        'rating': 4,
        'category': 'Exfoliant'
    },
    'bha': {
        'name': 'BHA (Beta Hydroxy Acid / Salicylic Acid)',
        'purpose': 'Oil-soluble exfoliation, unclogs pores, reduces blackheads and acne',
        'safety': 'Safe for oily/acne-prone skin at 0.5-2%. Can be drying.',
        'best_for': ['Acne', 'Oily Skin', 'Blackheads', 'Clogged Pores'],
        'warnings': ['Can be drying — follow with moisturizer', 'Avoid with other strong actives initially', 'Not ideal for very dry skin'],
        'rating': 4,
        'category': 'Exfoliant'
    },
    'ceramides': {
        'name': 'Ceramides',
        'purpose': 'Skin barrier repair, moisture retention, protection against environmental damage',
        'safety': 'Very Safe — Naturally found in skin. Suitable for all skin types including sensitive.',
        'best_for': ['Dry Skin', 'Sensitive Skin', 'Barrier Repair', 'Eczema-Prone Skin'],
        'warnings': ['Very few concerns', 'Choose products with ceramide complex for best results'],
        'rating': 5,
        'category': 'Moisturizing'
    },
    'salicylic acid': {
        'name': 'Salicylic Acid (BHA)',
        'purpose': 'Penetrates pores to dissolve oil and dead skin, treats acne at the source',
        'safety': 'Safe at 0.5-2%. Can cause dryness and peeling initially.',
        'best_for': ['Acne', 'Oily Skin', 'Blackheads', 'Whiteheads'],
        'warnings': ['Do not over-use — can strip skin', 'Pair with hydrating products', 'Avoid mixing with other strong acids'],
        'rating': 4,
        'category': 'Active'
    },
    'hyaluronic acid': {
        'name': 'Hyaluronic Acid',
        'purpose': 'Deep hydration, plumps skin, reduces appearance of fine lines',
        'safety': 'Very Safe — Naturally occurring in skin. Suitable for all skin types.',
        'best_for': ['Dry Skin', 'Dehydrated Skin', 'Anti-Aging', 'All Skin Types'],
        'warnings': ['Apply on damp skin for best results', 'In very dry climates, can pull moisture from skin — layer with occlusive'],
        'rating': 5,
        'category': 'Hydrating'
    },
    'glycerin': {
        'name': 'Glycerin',
        'purpose': 'Humectant that draws moisture to the skin, softens and smooths',
        'safety': 'Very Safe — One of the most well-tolerated ingredients. Used in almost all skincare.',
        'best_for': ['All Skin Types', 'Dry Skin', 'Sensitive Skin'],
        'warnings': ['Very rare to cause issues', 'In extremely dry air, use with an occlusive layer'],
        'rating': 5,
        'category': 'Hydrating'
    },
    'zinc oxide': {
        'name': 'Zinc Oxide',
        'purpose': 'Physical/mineral sunscreen filter, broad-spectrum UV protection, anti-inflammatory',
        'safety': 'Very Safe — Sits on skin surface. Does not penetrate. Ideal for sensitive skin.',
        'best_for': ['Sun Protection', 'Sensitive Skin', 'Acne-Prone Skin', 'Rosacea'],
        'warnings': ['Can leave white cast on darker skin tones', 'Choose micronized or tinted versions for better cosmetic elegance'],
        'rating': 5,
        'category': 'Sunscreen'
    },
    'squalane': {
        'name': 'Squalane',
        'purpose': 'Lightweight emollient, locks in moisture without greasiness, antioxidant properties',
        'safety': 'Very Safe — Biomimetic lipid. Non-comedogenic.',
        'best_for': ['Dry Skin', 'Oily Skin', 'Sensitive Skin', 'Anti-Aging'],
        'warnings': ['Ensure it is squalane (hydrogenated), not squalene (unstable)'],
        'rating': 5,
        'category': 'Moisturizing'
    },
    'peptides': {
        'name': 'Peptides',
        'purpose': 'Signal skin to produce more collagen, firm skin, reduce wrinkles',
        'safety': 'Safe — Well tolerated. Various types (Matrixyl, Argireline, Copper Peptides).',
        'best_for': ['Anti-Aging', 'Firmness', 'Fine Lines', 'All Skin Types'],
        'warnings': ['Copper peptides should not be used with Vitamin C or AHAs', 'Results take time — 8-12 weeks minimum'],
        'rating': 4,
        'category': 'Active'
    },
    'tea tree oil': {
        'name': 'Tea Tree Oil',
        'purpose': 'Natural antibacterial, antifungal — helps control acne-causing bacteria',
        'safety': 'Moderate — Use diluted (1-5%). Never apply undiluted to skin.',
        'best_for': ['Acne', 'Oily Skin', 'Fungal Acne'],
        'warnings': ['Can cause contact dermatitis in sensitive individuals', 'Always dilute before application', 'Do a patch test first'],
        'rating': 3,
        'category': 'Natural'
    },
    'aloe vera': {
        'name': 'Aloe Vera',
        'purpose': 'Soothing, hydrating, anti-inflammatory, wound healing support',
        'safety': 'Very Safe — Gentle and suitable for all skin types including sensitive.',
        'best_for': ['Sensitive Skin', 'Sunburn', 'Irritation', 'All Skin Types'],
        'warnings': ['Rare allergic reactions possible', 'Check for added fragrances in commercial products'],
        'rating': 5,
        'category': 'Natural'
    },
    'centella asiatica': {
        'name': 'Centella Asiatica (Cica)',
        'purpose': 'Calming, barrier repair, wound healing, anti-inflammatory',
        'safety': 'Very Safe — Excellent for sensitive and damaged skin.',
        'best_for': ['Sensitive Skin', 'Redness', 'Barrier Repair', 'Post-Procedure'],
        'warnings': ['Very few side effects reported', 'Quality of extract matters — look for madecassoside'],
        'rating': 5,
        'category': 'Natural'
    },
    'alpha arbutin': {
        'name': 'Alpha Arbutin',
        'purpose': 'Inhibits melanin production, fades dark spots and hyperpigmentation',
        'safety': 'Safe — Gentler alternative to hydroquinone. Well tolerated at 1-2%.',
        'best_for': ['Dark Spots', 'Hyperpigmentation', 'Uneven Skin Tone'],
        'warnings': ['Use with sunscreen for best results', 'Results take 4-8 weeks'],
        'rating': 4,
        'category': 'Active'
    },
    'kojic acid': {
        'name': 'Kojic Acid',
        'purpose': 'Skin brightening, inhibits tyrosinase enzyme, reduces melanin production',
        'safety': 'Moderate — Can cause contact dermatitis in sensitive skin. Use at 1-4%.',
        'best_for': ['Dark Spots', 'Hyperpigmentation', 'Sun Damage'],
        'warnings': ['Can cause irritation and redness', 'Makes skin photosensitive — always use SPF', 'Avoid on broken skin'],
        'rating': 3,
        'category': 'Active'
    },
    'glycolic acid': {
        'name': 'Glycolic Acid (AHA)',
        'purpose': 'Strongest AHA, exfoliates surface dead cells, stimulates collagen, brightens',
        'safety': 'Moderate — Use 5-10% for home use. Professional peels can go higher.',
        'best_for': ['Dullness', 'Anti-Aging', 'Dark Spots', 'Texture'],
        'warnings': ['Increases sun sensitivity significantly', 'Do NOT mix with retinol', 'Can cause purging initially', 'Start with lower concentrations'],
        'rating': 4,
        'category': 'Exfoliant'
    },
    'lactic acid': {
        'name': 'Lactic Acid (AHA)',
        'purpose': 'Gentle exfoliation, hydrating AHA, brightens and smooths skin',
        'safety': 'Safe — Gentler than glycolic acid. Good for beginners.',
        'best_for': ['Dry Skin', 'Dullness', 'Sensitive Skin', 'Beginners'],
        'warnings': ['Still increases sun sensitivity', 'Avoid mixing with retinol', 'Use 2-3 times per week'],
        'rating': 4,
        'category': 'Exfoliant'
    },
    'vitamin e': {
        'name': 'Vitamin E (Tocopherol)',
        'purpose': 'Antioxidant, moisturizing, protects against UV damage, supports healing',
        'safety': 'Safe — Well tolerated by most. Can be comedogenic for some oily skin types.',
        'best_for': ['Dry Skin', 'Anti-Aging', 'Scars', 'Sun Protection Support'],
        'warnings': ['Can clog pores in acne-prone skin if used in heavy formulations', 'Works best when combined with Vitamin C'],
        'rating': 4,
        'category': 'Antioxidant'
    },
    'shea butter': {
        'name': 'Shea Butter',
        'purpose': 'Rich emollient, deeply moisturizes, anti-inflammatory, barrier protection',
        'safety': 'Safe — Natural and well tolerated. Not ideal for very oily skin.',
        'best_for': ['Dry Skin', 'Eczema', 'Barrier Repair', 'Body Care'],
        'warnings': ['Can be too heavy for oily/acne-prone skin on the face', 'Comedogenic rating: 0-2 depending on formulation'],
        'rating': 4,
        'category': 'Moisturizing'
    },
    'panthenol': {
        'name': 'Panthenol (Vitamin B5)',
        'purpose': 'Humectant, soothes irritation, supports barrier repair, anti-inflammatory',
        'safety': 'Very Safe — Extremely well tolerated. Used in wound care products.',
        'best_for': ['Sensitive Skin', 'Irritation', 'Barrier Repair', 'All Skin Types'],
        'warnings': ['Very few concerns', 'Works well with almost all other ingredients'],
        'rating': 5,
        'category': 'Soothing'
    },
    'collagen': {
        'name': 'Collagen',
        'purpose': 'Topical hydration, plumping effect, film-forming moisture retention',
        'safety': 'Safe — Well tolerated. Note: topical collagen cannot penetrate skin deeply.',
        'best_for': ['Anti-Aging', 'Dry Skin', 'Fine Lines'],
        'warnings': ['Topical collagen mostly works as a humectant — does not rebuild collagen', 'For collagen synthesis, use Vitamin C + peptides'],
        'rating': 3,
        'category': 'Anti-Aging'
    },
    'charcoal': {
        'name': 'Activated Charcoal',
        'purpose': 'Draws out impurities and excess oil from pores, deep cleansing',
        'safety': 'Safe for occasional use. Can be drying if overused.',
        'best_for': ['Oily Skin', 'Acne', 'Deep Cleansing', 'Blackheads'],
        'warnings': ['Do not use daily — can strip skin', 'Follow with hydrating products', 'Not suitable for dry or sensitive skin'],
        'rating': 3,
        'category': 'Cleansing'
    },
    'witch hazel': {
        'name': 'Witch Hazel',
        'purpose': 'Natural astringent, reduces inflammation, tightens pores temporarily',
        'safety': 'Moderate — Alcohol-free versions are safer. Can be drying.',
        'best_for': ['Oily Skin', 'Acne', 'Large Pores'],
        'warnings': ['Avoid formulations with alcohol — very drying', 'Can irritate sensitive skin', 'Not for daily use in dry climates'],
        'rating': 3,
        'category': 'Natural'
    },
    'jojoba oil': {
        'name': 'Jojoba Oil',
        'purpose': 'Mimics natural sebum, balances oil production, deep moisturizing',
        'safety': 'Safe — Non-comedogenic. Suitable for most skin types.',
        'best_for': ['Dry Skin', 'Combination Skin', 'Sensitive Skin'],
        'warnings': ['Generally very safe', 'May not be enough moisture for very dry skin alone'],
        'rating': 4,
        'category': 'Moisturizing'
    },
    'neem extract': {
        'name': 'Neem Extract',
        'purpose': 'Antibacterial, antifungal, controls acne, traditional Ayurvedic remedy',
        'safety': 'Safe in formulated products. Pure neem oil can be very potent.',
        'best_for': ['Acne', 'Oily Skin', 'Fungal Issues'],
        'warnings': ['Pure neem oil should be diluted', 'Strong smell', 'Not for use during pregnancy in concentrated forms'],
        'rating': 4,
        'category': 'Natural'
    },
    'turmeric': {
        'name': 'Turmeric (Curcumin)',
        'purpose': 'Anti-inflammatory, brightening, antioxidant, reduces hyperpigmentation',
        'safety': 'Safe in formulated products. Raw turmeric can stain and irritate.',
        'best_for': ['Dark Spots', 'Dullness', 'Inflammation', 'Uneven Tone'],
        'warnings': ['Can stain skin yellow temporarily', 'Use formulated products rather than raw turmeric', 'Patch test recommended'],
        'rating': 4,
        'category': 'Natural'
    },
    'azelaic acid': {
        'name': 'Azelaic Acid',
        'purpose': 'Treats acne, rosacea, fades dark spots, gentle exfoliation, antibacterial',
        'safety': 'Safe — Available OTC at 10%. Prescription at 15-20%. Well tolerated.',
        'best_for': ['Acne', 'Rosacea', 'Dark Spots', 'Sensitive Skin'],
        'warnings': ['Can cause initial tingling', 'Safe during pregnancy (one of few actives)', 'Results take 4-8 weeks'],
        'rating': 5,
        'category': 'Active'
    },
    'ferulic acid': {
        'name': 'Ferulic Acid',
        'purpose': 'Antioxidant, boosts effectiveness of Vitamin C and E, UV protection support',
        'safety': 'Safe — Works best in combination with other antioxidants.',
        'best_for': ['Anti-Aging', 'Sun Protection', 'Brightening'],
        'warnings': ['Most effective in combination serums (C+E+Ferulic)', 'Oxidizes over time — store properly'],
        'rating': 4,
        'category': 'Antioxidant'
    },
    'licorice extract': {
        'name': 'Licorice Root Extract',
        'purpose': 'Brightening, anti-inflammatory, inhibits melanin, soothes irritation',
        'safety': 'Very Safe — Gentle and effective. Suitable for all skin types.',
        'best_for': ['Dark Spots', 'Sensitive Skin', 'Redness', 'Uneven Tone'],
        'warnings': ['Very few side effects', 'Works well with other brightening agents'],
        'rating': 5,
        'category': 'Natural'
    },
    'green tea': {
        'name': 'Green Tea Extract (EGCG)',
        'purpose': 'Powerful antioxidant, anti-inflammatory, reduces sebum, soothes skin',
        'safety': 'Very Safe — Well tolerated by all skin types.',
        'best_for': ['Oily Skin', 'Acne', 'Anti-Aging', 'Sensitive Skin'],
        'warnings': ['Very few concerns', 'Look for high EGCG concentration for efficacy'],
        'rating': 5,
        'category': 'Antioxidant'
    },
    'allantoin': {
        'name': 'Allantoin',
        'purpose': 'Soothing, promotes cell regeneration, softens skin, reduces irritation',
        'safety': 'Very Safe — Used in many sensitive skin products.',
        'best_for': ['Sensitive Skin', 'Irritation', 'Wound Healing', 'Dry Skin'],
        'warnings': ['Extremely gentle — almost no side effects reported'],
        'rating': 5,
        'category': 'Soothing'
    },
    'bentonite clay': {
        'name': 'Bentonite Clay',
        'purpose': 'Absorbs excess oil, deep cleanses pores, detoxifying mask ingredient',
        'safety': 'Safe for occasional use. Can be very drying.',
        'best_for': ['Oily Skin', 'Acne', 'Deep Cleansing'],
        'warnings': ['Do not use more than 1-2 times per week', 'Always follow with moisturizer', 'Not for dry or sensitive skin'],
        'rating': 3,
        'category': 'Cleansing'
    },
    'rose water': {
        'name': 'Rose Water',
        'purpose': 'Mild hydration, soothing, refreshing toner, anti-inflammatory',
        'safety': 'Very Safe — Gentle and suitable for all skin types.',
        'best_for': ['All Skin Types', 'Sensitive Skin', 'Refreshing'],
        'warnings': ['Ensure no added fragrances or alcohol', 'Mild effect — not a replacement for active toner'],
        'rating': 4,
        'category': 'Natural'
    },
    'chamomile': {
        'name': 'Chamomile Extract',
        'purpose': 'Anti-inflammatory, calming, reduces redness, soothes irritated skin',
        'safety': 'Very Safe — Excellent for sensitive and reactive skin.',
        'best_for': ['Sensitive Skin', 'Redness', 'Irritation', 'Rosacea'],
        'warnings': ['Rare: can cause allergic reaction in people allergic to ragweed family'],
        'rating': 5,
        'category': 'Soothing'
    },
    'micellar water': {
        'name': 'Micellar Water',
        'purpose': 'Gentle cleansing, removes makeup and impurities without rinsing',
        'safety': 'Very Safe — No-rinse formula suitable for all skin types.',
        'best_for': ['All Skin Types', 'Sensitive Skin', 'Makeup Removal'],
        'warnings': ['Some formulations contain surfactants that may irritate very sensitive skin', 'For heavy makeup, follow with a proper cleanser'],
        'rating': 4,
        'category': 'Cleansing'
    },
    'titanium dioxide': {
        'name': 'Titanium Dioxide',
        'purpose': 'Physical/mineral sunscreen filter, reflects UV rays, broad-spectrum protection',
        'safety': 'Very Safe — Does not penetrate skin. Suitable for sensitive skin.',
        'best_for': ['Sun Protection', 'Sensitive Skin', 'All Skin Types'],
        'warnings': ['Can leave white cast', 'Often combined with zinc oxide for full spectrum coverage'],
        'rating': 5,
        'category': 'Sunscreen'
    },
    'kaolin clay': {
        'name': 'Kaolin Clay',
        'purpose': 'Gentle oil absorption, mild cleansing, suitable for sensitive oily skin',
        'safety': 'Safe — Gentler than bentonite clay.',
        'best_for': ['Oily Skin', 'Sensitive Skin', 'Mild Cleansing'],
        'warnings': ['Very gentle — suitable for more frequent use than bentonite', 'Still follow with moisturizer'],
        'rating': 4,
        'category': 'Cleansing'
    },
    'rice bran': {
        'name': 'Rice Bran Extract',
        'purpose': 'Gentle physical exfoliation, brightening, rich in Vitamin E and antioxidants',
        'safety': 'Safe — Natural and gentle.',
        'best_for': ['Dullness', 'All Skin Types', 'Gentle Exfoliation'],
        'warnings': ['Very few concerns', 'Patch test if you have grain allergies'],
        'rating': 4,
        'category': 'Natural'
    },
    'zinc pca': {
        'name': 'Zinc PCA',
        'purpose': 'Regulates sebum production, antibacterial, reduces acne and shine',
        'safety': 'Safe — Well tolerated. Effective at 0.1-1%.',
        'best_for': ['Oily Skin', 'Acne', 'Shine Control'],
        'warnings': ['Very few side effects', 'Works well with niacinamide'],
        'rating': 4,
        'category': 'Active'
    },
    'silica': {
        'name': 'Silica',
        'purpose': 'Oil absorbing, mattifying, gives smooth finish, filler ingredient',
        'safety': 'Safe — Used in cosmetics for texture and oil control.',
        'best_for': ['Oily Skin', 'Matte Finish', 'Primer Effect'],
        'warnings': ['Non-active ingredient', 'Used mainly for cosmetic elegance'],
        'rating': 3,
        'category': 'Functional'
    },
    'iron oxides': {
        'name': 'Iron Oxides',
        'purpose': 'Natural mineral pigments for tinted sunscreens, protects against visible light',
        'safety': 'Very Safe — Non-irritating mineral pigments.',
        'best_for': ['Tinted Sunscreens', 'Visible Light Protection', 'Dark Spots Prevention'],
        'warnings': ['Not a standalone sunscreen — used with UV filters', 'Helps with white cast reduction'],
        'rating': 4,
        'category': 'Sunscreen'
    },
    'madecassoside': {
        'name': 'Madecassoside',
        'purpose': 'Derived from Centella Asiatica, powerful anti-inflammatory and wound healing',
        'safety': 'Very Safe — Excellent for damaged and sensitive skin.',
        'best_for': ['Sensitive Skin', 'Barrier Repair', 'Redness', 'Post-Procedure'],
        'warnings': ['Very gentle ingredient with minimal side effects'],
        'rating': 5,
        'category': 'Soothing'
    },
    'cholesterol': {
        'name': 'Cholesterol (Skincare)',
        'purpose': 'Essential lipid for skin barrier, works with ceramides for barrier repair',
        'safety': 'Very Safe — Natural component of skin barrier.',
        'best_for': ['Barrier Repair', 'Dry Skin', 'Sensitive Skin'],
        'warnings': ['Not dietary cholesterol — this is a topical ingredient', 'Best in combination with ceramides'],
        'rating': 5,
        'category': 'Moisturizing'
    },
    'phytosphingosine': {
        'name': 'Phytosphingosine',
        'purpose': 'Ceramide precursor, antimicrobial, anti-inflammatory, barrier building',
        'safety': 'Very Safe — Naturally found in skin.',
        'best_for': ['Barrier Repair', 'Acne', 'Anti-Inflammatory'],
        'warnings': ['Very few concerns', 'Most effective in combination with ceramides and cholesterol'],
        'rating': 5,
        'category': 'Moisturizing'
    },
    'sodium hyaluronate': {
        'name': 'Sodium Hyaluronate',
        'purpose': 'Smaller molecule form of hyaluronic acid, penetrates deeper for better hydration',
        'safety': 'Very Safe — Even more effective than regular hyaluronic acid for deep hydration.',
        'best_for': ['Dehydrated Skin', 'Dry Skin', 'Fine Lines', 'All Skin Types'],
        'warnings': ['Apply on damp skin', 'Same precautions as hyaluronic acid'],
        'rating': 5,
        'category': 'Hydrating'
    },
    'marine collagen': {
        'name': 'Marine Collagen',
        'purpose': 'Fish-derived collagen peptides, hydrating, may support skin elasticity',
        'safety': 'Safe — Well tolerated topically. More research needed for topical efficacy.',
        'best_for': ['Anti-Aging', 'Dry Skin', 'Elasticity'],
        'warnings': ['Not suitable for those with fish allergies', 'Topical effects are primarily hydrating'],
        'rating': 3,
        'category': 'Anti-Aging'
    },
    'gluconolactone': {
        'name': 'Gluconolactone (PHA)',
        'purpose': 'Gentlest chemical exfoliant, hydrating, antioxidant, less irritating than AHA/BHA',
        'safety': 'Very Safe — Ideal for sensitive skin that cannot tolerate AHA/BHA.',
        'best_for': ['Sensitive Skin', 'Gentle Exfoliation', 'Beginners'],
        'warnings': ['Very gentle — may need longer for visible results', 'Still use sunscreen'],
        'rating': 4,
        'category': 'Exfoliant'
    },
    'lactobionic acid': {
        'name': 'Lactobionic Acid (PHA)',
        'purpose': 'Ultra-gentle exfoliant, strong antioxidant, hydrating, anti-aging',
        'safety': 'Very Safe — Even gentler than gluconolactone.',
        'best_for': ['Sensitive Skin', 'Rosacea', 'Anti-Aging', 'Post-Procedure'],
        'warnings': ['Very few side effects', 'Ideal for those who cannot use AHA/BHA'],
        'rating': 4,
        'category': 'Exfoliant'
    },
    'papain': {
        'name': 'Papain (Papaya Enzyme)',
        'purpose': 'Natural enzyme exfoliant, breaks down dead skin proteins, brightening',
        'safety': 'Safe — Gentler than chemical exfoliants. Good for sensitive skin.',
        'best_for': ['Gentle Exfoliation', 'Dullness', 'All Skin Types'],
        'warnings': ['Can cause reactions in people with latex allergies', 'Patch test recommended'],
        'rating': 4,
        'category': 'Natural'
    },
    'bromelain': {
        'name': 'Bromelain (Pineapple Enzyme)',
        'purpose': 'Natural enzyme exfoliant, anti-inflammatory, helps with skin renewal',
        'safety': 'Safe — Natural and gentle.',
        'best_for': ['Gentle Exfoliation', 'Inflammation', 'All Skin Types'],
        'warnings': ['Avoid if allergic to pineapple', 'Very mild — suitable for frequent use'],
        'rating': 4,
        'category': 'Natural'
    },
    'mandelic acid': {
        'name': 'Mandelic Acid (AHA)',
        'purpose': 'Gentle AHA from almonds, exfoliates, brightens, treats acne and pigmentation',
        'safety': 'Safe — Larger molecule size means slower penetration and less irritation.',
        'best_for': ['Dark Spots', 'Acne', 'Sensitive Skin', 'Beginners'],
        'warnings': ['Still increases sun sensitivity', 'Gentler than glycolic — good starting AHA', 'Avoid with retinol'],
        'rating': 4,
        'category': 'Exfoliant'
    },
    'matrixyl 3000': {
        'name': 'Matrixyl 3000',
        'purpose': 'Peptide complex that stimulates collagen and elastin production, anti-wrinkle',
        'safety': 'Safe — Well studied peptide complex with good efficacy data.',
        'best_for': ['Anti-Aging', 'Fine Lines', 'Wrinkles', 'Firmness'],
        'warnings': ['Results take 8-12 weeks', 'Works best with consistent use'],
        'rating': 4,
        'category': 'Active'
    },
    'argireline': {
        'name': 'Argireline (Acetyl Hexapeptide-3)',
        'purpose': 'Peptide that relaxes facial muscles, reduces expression lines — "Botox in a bottle"',
        'safety': 'Safe — Non-invasive alternative to injectables. Results are milder.',
        'best_for': ['Expression Lines', 'Forehead Wrinkles', 'Crow\'s Feet'],
        'warnings': ['Effects are temporary and milder than injectables', 'Consistent use required', 'May cause slight muscle relaxation sensation'],
        'rating': 3,
        'category': 'Active'
    }
}

CONFLICT_RULES = [
    {
        'ingredients': ['retinol', 'aha'],
        'severity': 'high',
        'message': 'Retinol + AHA: Both are strong actives that increase cell turnover. Using together can cause severe irritation, redness, and barrier damage. Use on alternate nights.'
    },
    {
        'ingredients': ['retinol', 'bha'],
        'severity': 'high',
        'message': 'Retinol + BHA: Combining these can over-exfoliate and compromise your skin barrier. Alternate usage — retinol one night, BHA another.'
    },
    {
        'ingredients': ['retinol', 'vitamin c'],
        'severity': 'medium',
        'message': 'Retinol + Vitamin C: Can cause irritation when layered. Use Vitamin C in the morning and Retinol at night for best results.'
    },
    {
        'ingredients': ['retinol', 'glycolic acid'],
        'severity': 'high',
        'message': 'Retinol + Glycolic Acid: High risk of over-exfoliation. Never use in the same routine. Alternate nights if both are needed.'
    },
    {
        'ingredients': ['aha', 'bha'],
        'severity': 'medium',
        'message': 'AHA + BHA: Double exfoliation can be too harsh. If using both, apply BHA first, wait, then AHA — or use on different days.'
    },
    {
        'ingredients': ['vitamin c', 'aha'],
        'severity': 'medium',
        'message': 'Vitamin C + AHA: Both are acidic and can irritate. Use Vitamin C in AM and AHA in PM for optimal results.'
    },
    {
        'ingredients': ['vitamin c', 'bha'],
        'severity': 'low',
        'message': 'Vitamin C + BHA: Both work at low pH. May reduce each other\'s effectiveness. Best used at different times of day.'
    },
    {
        'ingredients': ['salicylic acid', 'glycolic acid'],
        'severity': 'high',
        'message': 'Salicylic Acid + Glycolic Acid: Double acid exfoliation can severely damage the skin barrier. Use on alternate days.'
    },
    {
        'ingredients': ['retinol', 'salicylic acid'],
        'severity': 'medium',
        'message': 'Retinol + Salicylic Acid: Can cause excessive dryness and irritation. Use on alternate evenings.'
    },
    {
        'ingredients': ['retinol', 'lactic acid'],
        'severity': 'medium',
        'message': 'Retinol + Lactic Acid: Both promote exfoliation. Using together may lead to irritation. Alternate nights recommended.'
    }
]


def decode_ingredients(ingredient_text):
    ingredient_text = ingredient_text.lower()
    found = []
    not_found = []

    parts = [i.strip() for i in ingredient_text.replace('\n', ',').split(',') if i.strip()]

    for part in parts:
        matched = False
        for key, data in INGREDIENT_DATABASE.items():
            if key in part.lower() or part.lower() in key:
                found.append(data)
                matched = True
                break
        if not matched:
            clean_name = part.strip().title()
            if len(clean_name) > 1:
                not_found.append({
                    'name': clean_name,
                    'purpose': 'Ingredient not in our database. Could be a fragrance, preservative, or specialized compound.',
                    'safety': 'Unknown — Research this ingredient separately or consult a dermatologist.',
                    'best_for': ['Check manufacturer claims'],
                    'warnings': ['Not yet analyzed in our database'],
                    'rating': 0,
                    'category': 'Unknown'
                })

    return found, not_found


def check_conflicts(ingredient_text):
    ingredient_text_lower = ingredient_text.lower()
    conflicts = []

    for rule in CONFLICT_RULES:
        all_present = True
        for ing in rule['ingredients']:
            if ing not in ingredient_text_lower:
                all_present = False
                break
        if all_present:
            conflicts.append(rule)

    return conflicts
