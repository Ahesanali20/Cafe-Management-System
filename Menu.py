# Menu Of Restaurant

menu = {
    'Burger' : 40,
    'Pasta' : 50,
    'Coffee' : 60,
    'Salad' : 70,
    'Pizza' : 80,
}

print("Welcome To SKYWAY RESTAURENT")
print("Burger : Rs.40\nPasta : Rs.50\nCoffee : Rs.60\nSalad : Rs.70\nPizza : Rs.80\n")

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
