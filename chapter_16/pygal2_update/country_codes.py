from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    return next(
        (code for code, name in COUNTRIES.items() if name == country_name),
        None,
    )
