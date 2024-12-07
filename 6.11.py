current_price = float(input("Enter current product price: "))
previous_price = float(input("Enter previous product price: "))

price_reduction = ((previous_price - current_price) / previous_price) * 100


if price_reduction >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {price_reduction:.0f}%")
else:
    print("Price reduction is less than 10%, no purchase recommendation.")
