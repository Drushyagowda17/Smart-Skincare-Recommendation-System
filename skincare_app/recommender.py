ROUTINE_RULES = {
    ('oily', 'acne'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Salicylic acid or neem-based gel cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Niacinamide + Zinc PCA pore-minimizing toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Niacinamide 10% serum for oil control', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Oil-free gel moisturizer with green tea', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Matte-finish mineral sunscreen SPF 50', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Charcoal or tea tree deep pore cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Exfoliant', 'desc': 'BHA 2% liquid exfoliant (2-3x/week)', 'wait': '5 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Niacinamide serum for overnight oil control', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Lightweight oil-free gel moisturizer', 'wait': '0 min'}
        ],
        'tips': [
            'Never skip moisturizer even with oily skin — dehydration causes more oil.',
            'Use blotting papers midday instead of washing face again.',
            'Change pillowcase every 3 days to prevent bacterial buildup.',
            'Avoid touching your face throughout the day.',
            'Clay masks once a week help deep clean pores.'
        ]
    },
    ('oily', 'dark_spots'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Brightening vitamin C gel cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Brightening licorice + alpha arbutin toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Vitamin C 20% brightening serum', 'wait': '3 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Oil-free gel moisturizer with niacinamide', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Tinted sunscreen SPF 40+ (prevents further spots)', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Oil-control brightening cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Serum', 'desc': 'Alpha arbutin + niacinamide brightening serum', 'wait': '2 min'},
            {'step': 3, 'type': 'Treatment', 'desc': 'Azelaic acid 10% for targeted dark spots', 'wait': '5 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Matte finish moisturizer', 'wait': '0 min'}
        ],
        'tips': [
            'SPF is the single most important step for preventing dark spots.',
            'Be patient — pigmentation takes 6-12 weeks to visibly fade.',
            'Never pick at pimples — this causes post-inflammatory hyperpigmentation.',
            'Vitamin C in AM + Alpha Arbutin in PM is a powerful combination.',
            'Reapply sunscreen every 2-3 hours if outdoors.'
        ]
    },
    ('oily', 'dullness'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gentle gel cleanser with vitamin C', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'AHA glow toner for gentle exfoliation', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Vitamin C serum for brightening', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Matte finish moisturizer with niacinamide', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Gel sunscreen SPF 50', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Oil-control gel cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Exfoliant', 'desc': 'AHA 10% exfoliating gel (2-3x/week)', 'wait': '5 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Niacinamide serum for pore refinement', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Lightweight gel moisturizer', 'wait': '0 min'}
        ],
        'tips': [
            'Exfoliation is key for dull oily skin — but do not overdo it.',
            'Vitamin C in the morning gives a natural glow throughout the day.',
            'Stay hydrated — water intake directly affects skin radiance.',
            'Weekly enzyme mask can boost cell turnover.',
            'Avoid heavy, pore-clogging products that make skin look flat.'
        ]
    },
    ('oily', 'dryness'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gentle hydrating gel cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Hydrating toner with hyaluronic acid', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Hyaluronic acid serum for hydration', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Oil-free gel moisturizer', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Hydrating gel sunscreen SPF 50', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gentle non-stripping cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Hydrating rose toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Hyaluronic acid + niacinamide serum', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Barrier repair moisturizer', 'wait': '0 min'}
        ],
        'tips': [
            'Dehydrated oily skin is very common — it means your skin lacks water, not oil.',
            'Avoid harsh cleansers that strip moisture.',
            'Layer hydrating products — toner, serum, then moisturizer.',
            'Apply hyaluronic acid on damp skin for maximum absorption.',
            'Drink at least 8 glasses of water daily.'
        ]
    },
    ('oily', 'anti_aging'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gentle gel cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Niacinamide pore toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Vitamin C 20% antioxidant serum', 'wait': '3 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Oil-free gel moisturizer with peptides', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Anti-aging sunscreen SPF 50', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gel cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Serum', 'desc': 'Retinol 0.5% serum (build up gradually)', 'wait': '5 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Peptide firming serum', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Lightweight anti-aging gel moisturizer', 'wait': '0 min'}
        ],
        'tips': [
            'Retinol is the gold standard for anti-aging — start low and slow.',
            'SPF is the single best anti-aging product.',
            'Peptides and retinol on alternate nights if irritation occurs.',
            'Antioxidants in the morning protect against free radical damage.',
            'Consistency is key — anti-aging results take 8-12 weeks.'
        ]
    },
    ('oily', 'sensitivity'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Soothing micellar cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Calming centella toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Niacinamide 5% (lower concentration for sensitivity)', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Barrier repair moisturizer with ceramides', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Mineral sunscreen SPF 50 for sensitive skin', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gentle micellar cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Serum', 'desc': 'Centella asiatica calming serum', 'wait': '2 min'},
            {'step': 3, 'type': 'Moisturizer', 'desc': 'Ceramide barrier repair cream', 'wait': '0 min'}
        ],
        'tips': [
            'Less is more for sensitive skin — keep routine minimal.',
            'Patch test every new product for 48 hours.',
            'Avoid fragrance, essential oils, and alcohol in products.',
            'Centella asiatica (cica) is your best friend for calming.',
            'Introduce new products one at a time, two weeks apart.'
        ]
    },
    ('dry', 'acne'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gentle cream cleanser (non-stripping)', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Hydrating rose toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Niacinamide 10% serum (oil control without drying)', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Barrier repair moisturizer with ceramides', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Hydrating sunscreen SPF 50+', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Milky hydrating cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Treatment', 'desc': 'Azelaic acid 10% (acne + gentle on dry skin)', 'wait': '5 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Hyaluronic acid serum for hydration', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Intense hydration cream', 'wait': '0 min'}
        ],
        'tips': [
            'Dry skin with acne needs gentle, non-stripping acne treatments.',
            'Avoid harsh BHA — use azelaic acid or gentle niacinamide instead.',
            'Hydration is critical — dehydrated skin can worsen acne.',
            'Look for non-comedogenic rich moisturizers.',
            'Spot-treat acne rather than applying actives all over.'
        ]
    },
    ('dry', 'dark_spots'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Milky hydrating cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Brightening licorice toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Vitamin C 20% serum', 'wait': '3 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Brightening day cream with alpha arbutin', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Hydrating tinted sunscreen SPF 40+', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Cream cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Serum', 'desc': 'Alpha arbutin + niacinamide serum', 'wait': '2 min'},
            {'step': 3, 'type': 'Treatment', 'desc': 'Mandelic acid 5% (gentle AHA for dry skin)', 'wait': '5 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Intense hydration cream with squalane', 'wait': '0 min'}
        ],
        'tips': [
            'Mandelic acid is the gentlest AHA — perfect for dry skin.',
            'Always layer hydrating products under brightening actives.',
            'SPF prevents new dark spots from forming.',
            'Squalane locks in moisture without clogging pores.',
            'Be patient — dark spots on dry skin take longer to fade.'
        ]
    },
    ('dry', 'dullness'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Cream cleanser with glycerin', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Hydrating rose toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Vitamin C serum for brightness', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Rich cream moisturizer', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Hydrating sunscreen SPF 50+', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Milky hydrating cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Exfoliant', 'desc': 'PHA gentle exfoliator (2x/week)', 'wait': '5 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Hyaluronic acid serum', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Intense hydration cream with shea butter', 'wait': '0 min'}
        ],
        'tips': [
            'Dull dry skin needs gentle exfoliation — PHAs are ideal.',
            'Hydration = glow. Layer toner + serum + cream.',
            'Facial oil as a last step seals everything in.',
            'Weekly hydrating sheet mask for instant radiance.',
            'Avoid over-washing — once in AM, once in PM is enough.'
        ]
    },
    ('dry', 'dryness'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Milky hydrating cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Hydrating rose toner (pat in 2-3 layers)', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Hyaluronic acid + sodium hyaluronate serum', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Intense hydration cream with ceramides', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Hydrating sunscreen SPF 50+', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Cream cleanser (never gel for dry skin)', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Hydrating toner layers', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Hyaluronic acid serum on damp skin', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Heavy barrier repair cream with shea butter', 'wait': '0 min'},
            {'step': 5, 'type': 'Oil', 'desc': 'Squalane or jojoba oil to seal (optional)', 'wait': '0 min'}
        ],
        'tips': [
            'Apply products on damp skin — locks in 10x more moisture.',
            '7-skin method: pat toner in 3-7 thin layers for deep hydration.',
            'Avoid hot water — use lukewarm water to cleanse.',
            'Humidifier in your room helps especially in winter.',
            'Look for ceramides, squalane, and hyaluronic acid in everything.'
        ]
    },
    ('dry', 'anti_aging'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Anti-aging cream cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Hydrating toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Vitamin C + Ferulic acid serum', 'wait': '3 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Collagen boost cream', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Anti-aging sunscreen SPF 50', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Cream cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Serum', 'desc': 'Retinol 0.5% serum (start 2x/week)', 'wait': '5 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Peptide firming serum', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Anti-aging night cream with collagen', 'wait': '0 min'},
            {'step': 5, 'type': 'Oil', 'desc': 'Facial oil to seal (squalane or rosehip)', 'wait': '0 min'}
        ],
        'tips': [
            'Dry skin ages faster — deep hydration is your anti-aging weapon.',
            'Retinol + rich moisturizer at night is the power combo.',
            'Peptides during the day, retinol at night.',
            'SPF prevents 90% of visible aging signs.',
            'Facial massage improves circulation and absorption.'
        ]
    },
    ('dry', 'sensitivity'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Soothing micellar cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Calming centella toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Centella asiatica + panthenol calming serum', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Barrier repair cream with ceramides + cholesterol', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Mineral sunscreen SPF 50+ (zinc oxide)', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gentle cream cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Serum', 'desc': 'Madecassoside + allantoin soothing serum', 'wait': '2 min'},
            {'step': 3, 'type': 'Moisturizer', 'desc': 'Heavy barrier repair cream', 'wait': '0 min'}
        ],
        'tips': [
            'Minimal routine is best — 3-4 products maximum.',
            'Look for: fragrance-free, alcohol-free, essential-oil-free.',
            'Ceramide + cholesterol + fatty acid trio repairs the barrier.',
            'Avoid physical scrubs — they micro-tear sensitive skin.',
            'New product? Patch test behind ear for 48 hours first.'
        ]
    },
    ('combination', 'acne'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gentle foam cleanser (not too drying)', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Niacinamide pore toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Niacinamide 10% serum', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Lightweight gel-cream moisturizer', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Matte sunscreen SPF 50', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Salicylic acid gel cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Exfoliant', 'desc': 'BHA 2% (on oily T-zone, 2x/week)', 'wait': '5 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Niacinamide serum', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Barrier repair cream (on dry areas), gel (on oily areas)', 'wait': '0 min'}
        ],
        'tips': [
            'Apply different products to different zones — gel on T-zone, cream on cheeks.',
            'BHA only on oily/acne areas, avoid dry patches.',
            'Niacinamide is perfect for combination skin — balances both zones.',
            'Blotting papers for T-zone midday.',
            'Do not over-cleanse — it triggers more oil production.'
        ]
    },
    ('combination', 'dark_spots'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Brightening vitamin C cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Brightening licorice toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Vitamin C 20% serum', 'wait': '3 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Brightening day cream with SPF 15', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Tinted sunscreen SPF 40', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gentle foam cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Serum', 'desc': 'Azelaic acid 10% serum', 'wait': '5 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Alpha arbutin serum on dark spots', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Hydrating yet lightweight night cream', 'wait': '0 min'}
        ],
        'tips': [
            'SPF is non-negotiable for dark spot treatment.',
            'Vitamin C AM + Azelaic Acid PM = powerful brightening duo.',
            'Alpha arbutin can be applied directly on dark spots.',
            'Results take time — 8-12 weeks for visible improvement.',
            'Avoid picking at skin — causes post-inflammatory marks.'
        ]
    },
    ('combination', 'dullness'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gel cleanser with vitamin C', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'AHA glow toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Vitamin C brightening serum', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Lightweight brightening moisturizer', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Gel sunscreen SPF 50', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gentle foam cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Exfoliant', 'desc': 'AHA 10% gel (on dull areas, 2x/week)', 'wait': '5 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Niacinamide serum for glow', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Balancing night cream', 'wait': '0 min'}
        ],
        'tips': [
            'AHA exfoliation reveals brighter skin underneath dead cells.',
            'Vitamin C gives instant radiance boost.',
            'Hydrate different zones differently — cream on dry, gel on oily.',
            'Facial mist throughout the day refreshes dull-looking skin.',
            'Exercise boosts circulation = natural glow.'
        ]
    },
    ('combination', 'dryness'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gentle hydrating cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Hydrating rose toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Hyaluronic acid serum', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Light cream on T-zone, rich cream on cheeks', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Hydrating sunscreen SPF 50', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Milky cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Multi-layer hydrating toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Hyaluronic acid + ceramide serum', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Barrier repair cream on dry areas', 'wait': '0 min'}
        ],
        'tips': [
            'Combination + dry means your T-zone is normal but cheeks are dry.',
            'Multi-masking: hydrating mask on dry areas, clay on oily.',
            'Apply extra layers of hydrating products on dry zones.',
            'Avoid foaming cleansers — they strip moisture.',
            'Squalane oil on dry patches at night works wonders.'
        ]
    },
    ('combination', 'anti_aging'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gentle cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Niacinamide balancing toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Vitamin C + peptide serum', 'wait': '3 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Lightweight anti-aging moisturizer', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Anti-aging sunscreen SPF 50', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gentle foam cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Serum', 'desc': 'Retinol 0.5% serum', 'wait': '5 min'},
            {'step': 3, 'type': 'Moisturizer', 'desc': 'Anti-aging night cream — richer on dry areas', 'wait': '0 min'}
        ],
        'tips': [
            'Retinol is the most proven anti-aging active.',
            'Start retinol 2x/week and build up gradually.',
            'Peptides in AM, retinol in PM for maximum benefit.',
            'SPF 50 daily is non-negotiable for anti-aging.',
            'Focus retinol around eyes (use eye-specific formulation) and forehead.'
        ]
    },
    ('combination', 'sensitivity'): {
        'morning': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Soothing micellar cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Toner', 'desc': 'Calming centella toner', 'wait': '1 min'},
            {'step': 3, 'type': 'Serum', 'desc': 'Niacinamide 5% calming serum', 'wait': '2 min'},
            {'step': 4, 'type': 'Moisturizer', 'desc': 'Barrier repair cream with ceramides', 'wait': '2 min'},
            {'step': 5, 'type': 'Sunscreen', 'desc': 'Mineral sunscreen SPF 50', 'wait': '0 min'}
        ],
        'night': [
            {'step': 1, 'type': 'Cleanser', 'desc': 'Gentle non-foaming cleanser', 'wait': '0 min'},
            {'step': 2, 'type': 'Serum', 'desc': 'Centella + panthenol soothing serum', 'wait': '2 min'},
            {'step': 3, 'type': 'Moisturizer', 'desc': 'Rich barrier cream on dry areas, light on T-zone', 'wait': '0 min'}
        ],
        'tips': [
            'Keep it simple — 3-4 products max.',
            'Avoid: fragrance, alcohol, essential oils, strong acids.',
            'Centella, panthenol, and allantoin are your best friends.',
            'Mineral sunscreen is better for sensitive skin than chemical.',
            'If a product stings, stop using it immediately.'
        ]
    }
}


def get_recommendation(skin_type, concern, budget, city, age, gender, water, sleep, routine_level, db_conn):
    key = (skin_type, concern)
    rule = ROUTINE_RULES.get(key)

    if not rule:
        key = ('combination', concern)
        rule = ROUTINE_RULES.get(key, ROUTINE_RULES[('combination', 'acne')])

    budget_map = {'low': 500, 'medium': 1000, 'high': 2500}
    budget_limit = budget_map.get(budget, 1000)

    cursor = db_conn.execute(
        "SELECT * FROM products WHERE (skin_type = ? OR skin_type = 'all') AND concern = ? AND price <= ? ORDER BY price ASC",
        (skin_type, concern, budget_limit)
    )
    matched_products = [dict(row) for row in cursor.fetchall()]

    if not matched_products:
        cursor = db_conn.execute(
            "SELECT * FROM products WHERE (skin_type = ? OR skin_type = 'all') AND concern = ? ORDER BY price ASC",
            (skin_type, concern)
        )
        matched_products = [dict(row) for row in cursor.fetchall()]

    if not matched_products:
        cursor = db_conn.execute(
            "SELECT * FROM products WHERE (skin_type = ? OR skin_type = 'all') ORDER BY price ASC",
            (skin_type,)
        )
        matched_products = [dict(row) for row in cursor.fetchall()]

    morning_products = {}
    night_products = {}
    categories_needed = ['cleanser', 'toner', 'serum', 'moisturizer', 'sunscreen', 'exfoliant']

    for cat in categories_needed:
        for p in matched_products:
            if p['category'] == cat and cat not in morning_products:
                morning_products[cat] = p
            if p['category'] == cat and cat not in night_products:
                if cat != 'sunscreen':
                    night_products[cat] = p

    warnings = []

    if sleep and float(sleep) < 6:
        warnings.append('You are sleeping less than 6 hours. Poor sleep accelerates skin aging and worsens acne. Aim for 7-8 hours.')

    if water and float(water) < 6:
        warnings.append('Your water intake is below recommended levels. Dehydration makes skin look dull and dry. Aim for 8+ glasses daily.')

    if age:
        age_val = int(age)
        if age_val > 35:
            warnings.append('After 35, collagen production slows down. Consider adding peptides and retinol to your routine.')
        if age_val > 45:
            warnings.append('Mature skin benefits from richer moisturizers and concentrated actives like retinol and peptides.')
        if age_val < 20:
            warnings.append('Young skin does not need heavy anti-aging products. Focus on gentle cleansing, moisturizing, and SPF.')

    if routine_level == 'beginner':
        warnings.append('As a beginner, start with just cleanser + moisturizer + sunscreen. Add actives one at a time after 2 weeks.')

    from utils import get_climate_tips
    climate_info = get_climate_tips(city) if city else None

    return {
        'morning': rule['morning'],
        'night': rule['night'],
        'tips': rule['tips'],
        'warnings': warnings,
        'products': matched_products,
        'morning_products': morning_products,
        'night_products': night_products,
        'climate': climate_info
    }
