"""
Company Generator

Generates company master data for EIRPI.
"""

import pandas as pd
import numpy as np

from faker import Faker

from config.project_config import *
from config.master_data import *

fake = Faker()
np.random.seed(RANDOM_SEED)

# ==========================================
# COMPANY NAME GENERATOR
# ==========================================

def generate_company_name(industry):

    if industry == "Manufacturing":

        prefix = np.random.choice(MANUFACTURING_PREFIXES)
        keyword = np.random.choice(MANUFACTURING_KEYWORDS)
        suffix = np.random.choice(COMPANY_SUFFIXES)

        return f"{prefix} {keyword} {suffix}"

    elif industry == "Healthcare":

        prefix = np.random.choice(HEALTHCARE_PREFIXES)
        keyword = np.random.choice(HEALTHCARE_KEYWORDS)
        suffix = np.random.choice(COMPANY_SUFFIXES)

        return f"{prefix} {keyword} {suffix}"

    elif industry == "Information Technology":

        prefix = np.random.choice(IT_PREFIXES)
        keyword = np.random.choice(IT_KEYWORDS)
        suffix = np.random.choice(COMPANY_SUFFIXES)

        return f"{prefix} {keyword} {suffix}"

    elif industry == "Logistics":

        prefix = np.random.choice(LOGISTICS_PREFIXES)
        keyword = np.random.choice(LOGISTICS_KEYWORDS)
        suffix = np.random.choice(COMPANY_SUFFIXES)

        return f"{prefix} {keyword} {suffix}"

    elif industry == "Energy":

        prefix = np.random.choice(ENERGY_PREFIXES)
        keyword = np.random.choice(ENERGY_KEYWORDS)
        suffix = np.random.choice(COMPANY_SUFFIXES)

        return f"{prefix} {keyword} {suffix}"

    elif industry == "Heritage & Monuments":

        prefix = np.random.choice(HERITAGE_PREFIXES)
        keyword = np.random.choice(HERITAGE_KEYWORDS)

        return f"{prefix} {keyword}"

    else:

        return fake.company()

# ==========================================
# REVENUE GENERATOR
# ==========================================

def generate_revenue(industry):
    """
    Generate realistic annual revenue (in Crores)
    based on industry.
    """

    min_rev, max_rev = REVENUE_RANGES[industry]

    # Generate a lognormal value
    value = np.random.lognormal(mean=2.5, sigma=0.8)

    # Normalize to 0–1
    value = value / 100

    # Clamp to 1
    value = min(value, 1)

    # Scale to industry range
    revenue = min_rev + value * (max_rev - min_rev)

    return round(revenue, 2)


# ==========================================
# REVENUE TEST
# ==========================================

def test_revenue_generation():

    print("\n===== REVENUE GENERATION TEST =====\n")

    for industry in INDUSTRIES:

        print(f"\n{industry}")

        for _ in range(5):

            revenue = generate_revenue(industry)

            print(f"₹ {revenue} Cr")

# ==========================================
# TEST FUNCTION
# ==========================================

def test_company_names():

    print("\nGENERATED COMPANY NAMES\n")

    industries = [
        "Manufacturing",
        "Healthcare",
        "Information Technology",
        "Logistics",
        "Energy",
        "Heritage & Monuments"
    ]

    for industry in industries:

        print(f"\n{industry}")

        for _ in range(3):

            print(generate_company_name(industry))


# ==========================================
# MAIN COMPANY GENERATOR
# ==========================================

def generate_companies():

    pass


# ==========================================
# ENTRY POINT
# ==========================================

'''if __name__ == "__main__":

    test_company_names()'''

if __name__ == "__main__":
    test_revenue_generation()