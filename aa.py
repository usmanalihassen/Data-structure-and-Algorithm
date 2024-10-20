def calculate_final_price(price, discount, tax_rate=0, apply_tax=False):
    """
    Calculate the final price of a product after applying a discount and an optional tax.

    Arguments:
    price -- the original price of the product (required)
    discount -- the discount percentage to apply (required)
    tax_rate -- the tax percentage to apply (optional, default is 0)
    apply_tax -- whether to apply the tax to the discounted price (optional, default is False)

    Returns:
    The final price after applying the discount and, if specified, the tax.
    """
    # Apply the discount
    discounted_price = price - (price * discount / 100)
    
    # Apply tax if requested
    if apply_tax:
        final_price = discounted_price + (discounted_price * tax_rate / 100)
    else:
        final_price = discounted_price

    return final_price

# Example usage of the function
original_price = 100.0  # The original price of the product
discount_percentage = 20.0  # The discount percentage
tax_percentage = 10.0  # The tax rate percentage

# Calculate the final price with different argument combinations
price_without_tax = calculate_final_price(original_price, discount_percentage)
price_with_tax = calculate_final_price(original_price, discount_percentage, tax_rate=tax_percentage, apply_tax=True)

# Display the results
print(f"Original price: ${original_price:.2f}")
print(f"Price after {discount_percentage}% discount (without tax): ${price_without_tax:.2f}")
print(f"Price after {discount_percentage}% discount and {tax_percentage}% tax: ${price_with_tax:.2f}")
