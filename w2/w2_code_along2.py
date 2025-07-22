
meal_price_child = float(input("What is the price of a child's meal? "))
meal_price_adult = float(input("What is the price of an adult's meal? ")) 
num_children = int(input("How many children are there? "))
num_adult = int(input("How many adults are there? "))
subtotal = meal_price_child*num_children+meal_price_adult*num_adult

print(f"Subtotal: ${subtotal}")

tax = float(input("What is the sales tax rate? ")) 
print(f"Sales Tax: ${((tax/100)*subtotal):.2f}")
print(f"Total: ${round(subtotal+((tax/100)*subtotal),2)}")

payment = float(input("What is the payment amount? "))
# print(f"Change: ${round(payment-(subtotal+((tax/100)*subtotal)),2)}") 