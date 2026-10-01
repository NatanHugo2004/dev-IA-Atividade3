def apply_discount(price, percent):
    """Aplica um desconto percentual ao preço."""
    discount = price * (percent / 100)
    return price - discount
