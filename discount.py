def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    :param price: Original price of the item.
    :param discount_percent: Discount percentage to apply.
    :return: Final price after discount, or the original price if discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    # Prompt the user for the original price and discount percentage
    try:
        price = float(input("Enter the original price of the item: $"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)
        
        # Print the final price
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")

# Execute the main function
if __name__ == "__main__":
    main()
