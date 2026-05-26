def calculate_price_with_tax(price: float, tax: float = 17.0) -> float:
    """
    Calculate the final product price including tax.

    Args:
        price (float): The original product price before tax.
        tax (float, optional): Tax rate as a percentage.
            Defaults to 17.0 (17%).

    Returns:
        float: Final price including tax.

    Example:
        >>> calculate_price_with_tax(100)
        117.0

        >>> calculate_price_with_tax(200, 10)
        220.0
    """
    return price + (price * tax / 100.0)

price = float(input("Enter the price you want to calculate the price with tax:"))
print("The price with the tax is: ",calculate_price_with_tax(price))    