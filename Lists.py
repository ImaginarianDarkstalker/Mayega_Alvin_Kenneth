Names = ["Jack", "Nakato", "Joshua", "Mary", "Quill"]

print(Names[1]) #This prints Nakato
Names[0] = "Peter"
print(Names)

Names.append("Sylus")
print(Names)

Names.insert(2, "Bathel")
print(Names)

# Names.remove(Names[3])
# print(Names)
# Alternative way to remove an item

del Names[3]
print(Names)

print(Names[-1])

foods = ["Matooke", "Posho", "Millet", "Cassava", "Peas", "Cheese", "Pineapple"]
print(foods[2:5])

countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"]
countries_copy = list(countries)
print(countries)
print(countries_copy)

for country in countries:
    print(countries)

animals = ["Cow", "Goat", "Tiger", "Dog", "Crow", "Anaconda", "Emu"]
animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)

animals_with_a = [animal for animal in animals if "a" in animal]
print(animals_with_a)

first_name = ["Mayega"]
last_name = ["Alvin", "Kenneth"]
full_name = first_name + last_name
print(full_name)
