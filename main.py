# Python Programming + FastApi Backend Development

print("Hello World! We are Learning FastApi for Backend Engineering!")

amount_allowed = 50
product_price = 15
tax = 0.03

total_product_price = product_price + (product_price*tax)

amount_left = amount_allowed - total_product_price

print(f"Total Amount Left After Product Purchase: ${amount_left:.2f}")



user_input = int(input("How many days before your birthday: "))
weeks_left = user_input//7

print(f"Approximate Weeks before your birthday are: {weeks_left}")