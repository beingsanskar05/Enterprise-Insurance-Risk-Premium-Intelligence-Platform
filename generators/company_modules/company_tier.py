"""
Company Tier Generator

Determines the business size category
of each company.
"""

import numpy as np

from config.master_data import (
    COMPANY_TIERS,
    COMPANY_TIER_DISTRIBUTION
)


def generate_company_tier():
    """
    Randomly assign a company tier
    based on predefined probabilities.
    """

    probabilities = []

    for tier in COMPANY_TIERS:
        probabilities.append(
            COMPANY_TIER_DISTRIBUTION[tier] / 100
        )

    tier = np.random.choice(
        COMPANY_TIERS,
        p=probabilities
    )

    return tier

def test_company_tiers():

    print("\nCOMPANY TIER TEST\n")

    for _ in range(20):

        print(generate_company_tier())


if __name__ == "__main__":

    test_company_tiers()