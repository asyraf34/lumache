"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass

def get_random_ingredients(kind=None):
    """
   1.Chicken breast\n
   2.Curry powder\n
   3.Onion

    """
    return ["shells", "gorgonzola", "parsley"]
