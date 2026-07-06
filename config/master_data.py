"""
Master Reference Data
Enterprise Insurance Risk & Premium Intelligence Platform
"""

# ==========================================
# INDUSTRIES
# ==========================================

INDUSTRIES = [
    "Manufacturing",
    "Healthcare",
    "Retail",
    "Information Technology",
    "Logistics",
    "Construction",
    "Energy",
    "Telecom",
    "Hospitality",
    "Heritage & Monuments"
]

# ==========================================
# INDUSTRY DISTRIBUTION
# Total = 10,000 Companies
# ==========================================

INDUSTRY_DISTRIBUTION = {
    "Manufacturing": 1500,
    "Healthcare": 1000,
    "Retail": 1200,
    "Information Technology": 1000,
    "Logistics": 1000,
    "Construction": 1200,
    "Energy": 800,
    "Telecom": 800,
    "Hospitality": 1000,
    "Heritage & Monuments": 500
}

# ==========================================
# REVENUE RANGES (Crores)
# ==========================================

REVENUE_RANGES = {

    "Manufacturing": (50, 5000),

    "Healthcare": (20, 3000),

    "Retail": (50, 4000),

    "Information Technology": (30, 6000),

    "Logistics": (20, 2500),

    "Construction": (50, 8000),

    "Energy": (200, 15000),

    "Telecom": (100, 10000),

    "Hospitality": (20, 2000),

    "Heritage & Monuments": (10, 500)

}

# ==========================================
# EMPLOYEE MULTIPLIERS
# Employees Generated From Revenue
# ==========================================

EMPLOYEE_MULTIPLIERS = {

    "Manufacturing": 8,

    "Healthcare": 10,

    "Retail": 6,

    "Information Technology": 4,

    "Logistics": 5,

    "Construction": 7,

    "Energy": 3,

    "Telecom": 4,

    "Hospitality": 8,

    "Heritage & Monuments": 2

}


# ==========================================
# CITY STATE MAPPING
# ==========================================

CITY_STATE_MAPPING = {

    "Mumbai": "Maharashtra",

    "Pune": "Maharashtra",

    "Nagpur": "Maharashtra",

    "Delhi": "Delhi",

    "Bengaluru": "Karnataka",

    "Mysuru": "Karnataka",

    "Hyderabad": "Telangana",

    "Chennai": "Tamil Nadu",

    "Coimbatore": "Tamil Nadu",

    "Ahmedabad": "Gujarat",

    "Surat": "Gujarat",

    "Kolkata": "West Bengal",

    "Jaipur": "Rajasthan",

    "Lucknow": "Uttar Pradesh",

    "Noida": "Uttar Pradesh",

    "Indore": "Madhya Pradesh",

    "Gurugram": "Haryana",

    "Chandigarh": "Punjab",

    "Kochi": "Kerala",

    "Visakhapatnam": "Andhra Pradesh"

}

# Manufacturing Names

MANUFACTURING_PREFIXES = [
    "Apex",
    "Titan",
    "Vertex",
    "Prime",
    "Nova",
    "Global",
    "United",
    "Elite"
]

MANUFACTURING_KEYWORDS = [
    "Manufacturing",
    "Industrial",
    "Engineering",
    "Production",
    "Industries"
]

# Healthcare Names

HEALTHCARE_PREFIXES = [
    "CarePlus",
    "Meditech",
    "LifeCare",
    "Apollo",
    "HealthFirst",
    "MediCore"
]

HEALTHCARE_KEYWORDS = [
    "Hospitals",
    "Healthcare",
    "Medical Systems",
    "Life Sciences"
]

#IT Names

IT_PREFIXES = [
    "Vertex",
    "Nova",
    "Quantum",
    "Cloud",
    "Digital",
    "TechNova",
    "ByteCore"
]

IT_KEYWORDS = [
    "Technologies",
    "Data Systems",
    "Digital Solutions",
    "Software Services",
    "Analytics"
]

#Logistics Names

LOGISTICS_PREFIXES = [
    "Swift",
    "Global",
    "Trans",
    "Express",
    "Prime"
]

LOGISTICS_KEYWORDS = [
    "Logistics",
    "Supply Chain",
    "Freight Services",
    "Distribution"
]

#Energy Names

ENERGY_PREFIXES = [
    "Green",
    "Solar",
    "Power",
    "Eco",
    "Renew"
]

ENERGY_KEYWORDS = [
    "Energy",
    "Power Systems",
    "Renewables",
    "Energy Solutions"
]

#Heritage Names

HERITAGE_PREFIXES = [
    "National",
    "Ancient",
    "Indian",
    "Royal",
    "Historic"
]

HERITAGE_KEYWORDS = [
    "Heritage Trust",
    "Monument Foundation",
    "Conservation Society",
    "Museum Authority"
]

#Common Suffixes

COMPANY_SUFFIXES = [
    "Ltd",
    "Corporation",
    "Group",
    "Enterprises",
    "Private Limited"
]

#Why Are We Doing This?

#Later the generator will create names like

#prefix + keyword + suffix

"""Example:
Apex Manufacturing Ltd

Titan Engineering Corporation

Nova Digital Solutions Pvt Ltd

National Heritage Trust"""

#def generate_company_name(industry):

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