# Clothing Inventory Management

#Here I say welcome
print(("Welcome to the clothing inventory".upper().center(40)))
       
#Inventory with 4 products
inventory={"T-shirt":15.50,
           "Jeans":40.00,
           "Sneakers":60.00,
           "hat":12.00}

#Menu options

print("-" * 40) 
print("MENU".upper().center(40))
print("-" * 40) 

print("\n1. Add new product")
print("2. Check the price")
print("3. Modify the price")
print("4. Delete product")

#Here the user chooses an option
option=input("\nSelect an option: ")

#Here I start to add a new product
if option=="1":
    new=input("\nEnter the product that you want to add: ")

    #The idea is to check if the product exits in the inventory
    if new in inventory:
        print("\nThe product already exists.")
    else:
         price=float(input("\nPut the price: "))
         inventory[new]=price
         print("\nProduct added successfully.")

#Checkin the price
elif option=="2":
     name=input("\nEnter the product that you want to check: ")

     if name not in inventory:
        print("\nThis product is not in the inventory.")
     else:
        print(f"\nThe price of {name} is: ${inventory[name]}")

#Modify the price
elif option=="3":
    name=input("\n:Which product do you want to modify?: ")
    
    if name not in inventory:
        print("\nThis product is not in the inventory.")
    else: 
     newprice=float(input("Enter the new price: "))
     inventory[name]=newprice
     print("\nPrice updated successfully,")

#Delete product
elif option=="4":
    name=input("\nWhich product do you want to delete?: ")

    if name not in inventory:
        print("\n\033[31mThis product does not exist.\033[0m")
    else:
        del inventory[name]
        print("\nProduct deleted.")

#Here I invalid the option
else:
    print("\n\033[31mInvalid option.\33[0m")

#Summary about (count+average)
print("\nCurrent number of products:", len(inventory))

if len(inventory)>0:
    total=0
    for price in inventory.values():
        total+=price

    average=total/len(inventory)

    #Table showing the summary
    print("\n" + "-" * 40)
    print("Final Inventory".upper().center(40))
    print("-" * 40)

    print(f"| {'Product':15} | {'Price':10} |")
    print("-" * 40)

    for product, price in inventory.items():
        print(f"| {product:15} | ${price:<10.2f}|")

    print("-" * 40)

