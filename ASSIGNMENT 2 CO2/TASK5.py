# Functions, Parameters and Scope

def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order


print("Buggy function:")
print(add_item_buggy("Tea"))
print(add_item_buggy("Vada"))

print("\nCorrect function:")
print(add_item("Tea"))
print(add_item("Vada"))

print("\nDefault values:")
print(add_item_buggy.__defaults__)


# Function with positional, keyword and default parameters
def customer_order(name, item="Tea", quantity=1):
    return name, item, quantity


print(customer_order("Arun"))
print(customer_order("Bala", "Coffee", 2))
print(customer_order(name="Divya", item="Juice", quantity=3))


# Returning multiple values
def calculate_bill(amount):
    gst = amount * 0.05
    total = amount + gst
    return total, gst


total, gst = calculate_bill(100)
print("Total:", total)
print("GST:", gst)


# Local and global scope
count = 10

def local_example():
    count = 5
    print("Local count:", count)


def global_example():
    global count
    count = 20
    print("Global count:", count)


local_example()
global_example()
print("Outside function:", count)


# Nonlocal scope
def outer():
    value = 10

    def inner():
        nonlocal value
        value += 5

    inner()
    print("Nonlocal value:", value)


outer()


# Three independent customers
customers = ["Arun", "Bala", "Divya"]

for customer in customers:
    order = []
    order = add_item("Tea", order)
    order = add_item("Vada", order)
    print(customer, ":", order)
