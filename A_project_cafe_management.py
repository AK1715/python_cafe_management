# define the menu of restaurant
menu = {
    'pizza':50,
    'pasta':60,
    'burger':70,
    'salad':80,
    'coffee':100,
}

#greet
print("Welcome to PYTHON Restaurant")
print("pizza: Rs50 \npasta: Rs60 \nburger: Rs70 \nsalad: Rs80 \ncoffee: Rs100")

order_total = 0
#70 + 80 = 150

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Order Item {item_1} is not avaliable yet")


another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Order item {item_2} not avaliable yet")
    
print(f"The total amount of items is {order_total}")