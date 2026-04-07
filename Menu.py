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

order_total = 0

order_item = input("Enter the name of item you want to order : ").capitalize()

if order_item in menu:
    order_total += menu[order_item]
    print(f"Your item {order_item} has been Added to your order")

else:
    print(f"Your item {order_item} is not available!")

another_order = input("Do you want order another item ? (yes/no)")
while another_order.lower() == "yes":
    order_item_2 = input(
        "Enter the name of another item you want to order : ").capitalize()
    if order_item_2 in menu:
        order_total += menu[order_item_2]
        print(f"Your item {order_item_2} has been Added to your order")

    else:
        print(f"Your item {order_item_2} is not available!")

    another_order = input("Do you want order another item ? (yes/no)")
    if another_order != "yes":
        break
print(f"Sir, Total Amount of your order is {order_total}.")
