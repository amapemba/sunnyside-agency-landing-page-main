cell_phone=str(input("Enter the cell phone make and model:"))
price_phone=float(input("Enter the price of phone in dollars: $"))
price_warranty=float(input("Enter the price of the warranty in dollars: $"))

print("Receipt")

print(f'The cell phone purchased: {cell_phone}')

print(f'The purchase price is: ${price_phone}')

print(f'The warranty cost is: ${price_warranty}')

tax = 0.06
shipping_cost = 0.017

subtotal=price_phone+price_warranty
shipping_total=shipping_cost * price_phone

The_tax=subtotal*tax

print(f'Shipping: ${shipping_total:.2f}')

print(f'Tax: ${The_tax:.2f}')

total=The_tax+price_phone+price_warranty+shipping_total

print(f'The amount due is: ${total:.2f}')