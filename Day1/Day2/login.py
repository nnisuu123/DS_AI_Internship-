# Welcome to Shopping Cart Program

print("===================================")
print("      WELCOME TO SHOPPING")
print("===================================")

cart = []

# Taking input from the user
while True:
    item = input("Enter your item (type 'done' to finish): ")

    if item.lower() == "done":
        break

    cart.append(item)

print("\n==============================")
print("Cart Type : List")
print("==============================")
print(cart)

print("\nTotal Items in Cart :", len(cart))

# Convert list to tuple
cart_tuple = tuple(cart)

print("\n==============================")
print("Cart Type : Tuple")
print("==============================")
print(cart_tuple)

print("\n==============================")
print("Checkout Completed")
print("Thank You for Shopping!")
print("==============================")