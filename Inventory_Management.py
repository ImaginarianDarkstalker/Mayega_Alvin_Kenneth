inventory = {
    "eggs (trays)": 100,
    "chicken feed (sacks)": 40,
    "fertilizer (sacks)": 50,
    "coffee (sacks)": 20,
    "matooke (bunches)": 100,
    "chickens": 1000,
    "cattle": 20,
    "milk (litres)": 100
    
}

print("Welcome to the Farm Inventory Management System (FIMS)!\n(Inventory values are updated daily)")
print("\nIf you want to view the items in the inventory, **Press 1**.\nIf you want to add or update items in the inventory, **Press 2**.\nIf you want to remove inventory items, **Press 3**.\nIf you want to quit the program, **Press 4**")

while True:
    choice = input("\nEnter your choice (1-4):")
    if choice == "1":
        print("\nHere is the farm's inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    
    elif choice == "2":
        item = input("\nEnter item name: ")
        quantity = int(input("Enter quantity: "))
        inventory[item] = quantity
        print("Inventory updated")
    
    elif choice == "3":
        item = input("\nEnter item to remove: ")
        if item in inventory:
            del inventory[item]
            print(f"{item} removed.")
        else:
            print("Item not found.")
            
    elif choice == "4":
        print("\nThank you for using FIMS!")
        break
    
    else:
        print("\nPlease choose an option between 1 and 4")
            