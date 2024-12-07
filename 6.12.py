num_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

total_cost = num_products * product_price

if num_products > 2:
    discount = total_cost * 0.25  #
    total_cost -= discount

print(f"Amount to pay: {total_cost:.2f}")