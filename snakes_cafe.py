appetizers = ["Wings", "Cookies", "Spring Rolls"]
entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
desserts = ["Ice Cream", "Cake", "Pie"]
drinks = ["Coffee", "Tea", "Unicorn Tears"]
neworder = []

print("**************************************")
print("**  Welcome to the Snakes Cafe!  **")
print("**  Please see our menu below.  **")
print("**")
print('** To quit at any time, type "quit" **')
print("**************************************")
print()

print("Appetizers")
print("----------")
for appetizer in appetizers:
    print(appetizer)

print()
print("Entrees")
print("-------")
for entree in entrees:
    print(entree)

print()
print("Desserts")
print("--------")
for dessert in desserts:
    print(dessert)

print()
print("Drinks")
print("------")
for drink in drinks:
    print(drink)

print()
print("**************************************")
print("** What would you like to order? **")
print("**************************************")
# loop until users enters quit
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