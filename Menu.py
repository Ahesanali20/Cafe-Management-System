"""
A simple restaurant menu management system that allows customers to order items
from a predefined menu and calculate the total cost of their order.

The module displays a menu, takes customer orders, validates item availability,
and calculates the total amount due.
"""

menu = {
    'Burger' : 40,
    'Pasta' : 50,
    'Coffee' : 60,
    'Salad' : 70,
    'Pizza' : 80,
}

print("""
Welcome To SKYWAY RESTAURANT

Menu:
Burger           Rs.40
Pasta            Rs.50
Coffee           Rs.60
Salad            Rs.70
Pizza            Rs.80
""")

total_amount = 0

selected_item = input(
    "Enter the name of item you want to order : ").capitalize()

if selected_item in menu:
    total_amount += menu[selected_item]
    print(f"Your item {selected_item} has been Added to your order")

else:
    print(f"Your item {selected_item} is not available!")

continue_ordering = input("Do you want order another item ? (yes/no)")
while continue_ordering.lower() == "yes":
    additional_item = input(
        "Enter the name of another item you want to order : ").capitalize()
    if additional_item in menu:
        total_amount += menu[additional_item]
        print(f"Your item {additional_item} has been Added to your order")

    else:
        print(f"Your item {additional_item} is not available!")

    continue_ordering = input("Do you want order another item ? (yes/no)")
    if continue_ordering != "yes":
        break
print(f"Sir, Total Amount of your order is {total_amount}.")
