#Number 1
my_favourite_beverages = ["Fanta", "Coca Cola", "Minute Maid"]
my_favourite_beverages = set(my_favourite_beverages)
print(my_favourite_beverages)

#Number 2
my_favourite_beverages.add("Sprite")
my_favourite_beverages.add("Pepsi")
print(my_favourite_beverages)

#Number 3
mySet = {"oven", "kettle", "microwave", "refridgerator"}
if "microwave" in mySet:
    print("Yep, Microwave is present in the set")
else:
    print("Nope, microwave isn't in the set")

#Number 4
mySet.remove("kettle")
print(mySet)

#Number 5
for Set in mySet:
    print(Set)
    
#Number 6
items_set = {"chair", "table", "cup", "hat"}
items_list = ["orange", "pan"]
items_set.update(items_list)
print(items_set)

#Number 7
age_set = {22}
first_names_set = {"Mayega"}
combined_set = age_set.union(first_names_set)
print(combined_set)