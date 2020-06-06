appetizers = ["Wings", "Cookies", "Spring Rolls"]
entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
desserts = ["Ice Cream", "Cake", "Pie"]
drinks = ["Coffee", "Tea", "Unicorn Tears"]
neworder = []

def welcome_message():
    print("**************************************")
    print("**  Welcome to the Snakes Cafe!  **")
    print("**  Please see our menu below.  **")
    print("**")
    print('** To quit at any time, type "quit" **')
    print("**************************************")
    print()

def appetizers_menu():
    print("Appetizers")
    print("----------")
    for appetizer in appetizers:
        print(appetizer)

def entrees_menu():
    print()
    print("Entrees")
    print("-------")
    for entree in entrees:
        print(entree)

def dessert_menu():
    print()
    print("Desserts")
    print("--------")
    for dessert in desserts:
        print(dessert)

def drinks_menu():
    print()
    print("Drinks")
    print("------")
    for drink in drinks:
        print(drink)

def enter_order():
    print()
    print("**************************************")
    print("** What would you like to order? **")
    print("**************************************")

# loop until users enters quit
def submit_order():
    n = 0 
    while n == 0:
        order = input()
        neworder.append(order)
        if order == "quit":
            n = 1
            break
        if order in appetizers or order in entrees or order in desserts or order in drinks:
            count = neworder.count(order)
            if count < 2:
                print(f"** {count} order of {order} have been added to your meal **")
            else:
                print(f"** {count} orders of {order} have been added to your meal **")
        else:
            print(f"Sorry, we don't have {order} in our menu")

def main():
    welcome_message()
    appetizers_menu()
    entrees_menu()
    dessert_menu()
    drinks_menu()
    enter_order()
    submit_order()


main()