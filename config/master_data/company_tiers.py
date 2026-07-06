
# ==========================================
# COMPANY TIERS
# ==========================================

COMPANY_TIERS = [
    "Startup",
    "Small",
    "Medium",
    "Large",
    "Enterprise",
    "Fortune"
]

# ==========================================
# COMPANY TIER DISTRIBUTION (%)
# Must Sum to 100
# ==========================================

COMPANY_TIER_DISTRIBUTION = {
    "Startup": 10,
    "Small": 25,
    "Medium": 35,
    "Large": 20,
    "Enterprise": 8,
    "Fortune": 2
}

# ==========================================
# REVENUE ALLOCATION INSIDE INDUSTRY RANGE
# ==========================================

COMPANY_TIER_REVENUE_RATIO = {

    "Startup": (0.00, 0.08),

    "Small": (0.08, 0.20),

    "Medium": (0.20, 0.45),

    "Large": (0.45, 0.70),

    "Enterprise": (0.70, 0.90),

    "Fortune": (0.90, 1.00)

}

# ==========================================
# COMPANY TIER PROFILES
# ==========================================

COMPANY_TIER_PROFILE = {

    "Startup": {
        "employee_range": (20, 150),
        "asset_range": (1, 2),
        "premium_multiplier": 0.80
    },

    "Small": {
        "employee_range": (100, 500),
        "asset_range": (2, 4),
        "premium_multiplier": 0.90
    },

    "Medium": {
        "employee_range": (500, 3000),
        "asset_range": (3, 6),
        "premium_multiplier": 1.00
    },

    "Large": {
        "employee_range": (3000, 12000),
        "asset_range": (5, 10),
        "premium_multiplier": 1.15
    },

    "Enterprise": {
        "employee_range": (12000, 40000),
        "asset_range": (8, 15),
        "premium_multiplier": 1.30
    },

    "Fortune": {
        "employee_range": (40000, 100000),
        "asset_range": (15, 50),
        "premium_multiplier": 1.50
    }

}