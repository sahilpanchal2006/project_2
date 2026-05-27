"""
Custom context processor for Grow Sale Products.

Provides company-wide information available in all templates.
"""

from datetime import datetime


def company_info(request):
    """Return company information for use in all templates."""
    current_years = datetime.now().year - 2000
    return {
        'company_name': 'Grow Sale Products',
        'company_phone': '+91 99253 91567',
        'company_hours': 'Mon-Sat: 10AM-8PM',
        'company_location': 'Ahmedabad',
        'company_established': 2000,
        'company_experience_years': current_years,
        'company_years': current_years,
    }
