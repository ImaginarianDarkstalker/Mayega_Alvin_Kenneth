#Number 1
Names = ["Jack", "Nakato", "Joshua", "Mary", "Quill"]
print(Names[1]) #This prints Nakato

#Number 2
Names[0] = "Peter"
print(Names)

#Number 3
Names.append("Sylus")
print(Names)

#Number 4
Names.insert(2, "Bathel")
print(Names)

#Number 5
del Names[3]
print(Names)

#Number 6
print(Names[-1])

#Number 7
foods = ["Matooke", "Posho", "Millet", "Cassava", "Peas", "Cheese", "Pineapple"]
print(foods[2:5])

#Number 8
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"]
countries_copy = list(countries)
print(countries)
print(countries_copy)

#Number 9
for country in countries:
    print(countries)

#Number 10
animals = ["Cow", "Goat", "Tiger", "Dog", "Crow", "Anaconda", "Emu"]
animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)

#Number 11
animals_with_a = [animal for animal in animals if "a" in animal]
print(animals_with_a)

#Number 12
first_name = ["Mayega"]
last_name = ["Alvin", "Kenneth"]
full_name = first_name + last_name
print(full_name)
