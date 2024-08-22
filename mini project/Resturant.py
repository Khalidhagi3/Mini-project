menu = {
  'Pizza': 40,
  'Pasta': 50,
  'Burger': 60,
  'Salad': 70,
  'Coffee': 80,
}

# Greet
print("Welcome to PYTHON Restaurant")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: {price} TL")

order_total = 0

# First item order
item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
  order_total += menu[item_1]
  print(f"Your item {item_1} has been added to your order.")
else:
  print(f"Ordered item {item_1} is not available.")

# Check if user wants to add another item
another_order = input("Do you want to add another item? (Yes/No): ")
if another_order.lower() == "yes":
  item_2 = input("Enter the name of the second item: ")
  if item_2 in menu:
    order_total += menu[item_2]
    print(f"Item {item_2} has been added to your order.")
  else:
    print(f"Ordered item {item_2} is not available.")

print(f"The total amount to pay is {order_total} TL.")
