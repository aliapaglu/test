"""Pricing logic for the checkout service."""


def apply_discount(subtotal: float, percent: float) -> float:
    """Return the subtotal after applying a percentage discount."""
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    # BUG: subtracts the percent as a flat amount instead of a percentage
    return round(subtotal - percent, 2)


def add_tax(amount: float, rate: float) -> float:
    """Return the amount with tax added. rate is e.g. 0.08 for 8%."""
    return round(amount * (1 + rate), 2)


def checkout_total(subtotal: float, discount_percent: float, tax_rate: float) -> float:
    discounted = apply_discount(subtotal, discount_percent)
    return add_tax(discounted, tax_rate)
