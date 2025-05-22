#Number 1
x = ("samsung", "iphone", "tecno", "redmi")
print("My favourite phone brand is: " + x[0])

#Number 2
print("\nThe second last item in my tuple is " + x[-2])

#Number 3
print("\nAt first the second item was " + x[1])
x = ("samsung", "itel", "tecno", "redmi")
print("But now it is " + x[1])

#Number 4
print(x)
x = ("samsung", "iphone", "tecno", "redmi", "Huawei")
print(x)

#Number 5
for x in x:
    print(x)

#Number 6
x = ("iphone", "tecno", "redmi", "Huawei")
print(x)

#Number 7
cities_in_uganda = ["Kampala", "Jinja", "Entebbe", "Fortportal", "Mbale", "Masaka", "Luwero"]
cities_in_uganda = tuple(cities_in_uganda)
print(cities_in_uganda)

#Number 8
city_1, city_2, city_3, city_4, city_5, city_6, city_7 = cities_in_uganda
print(city_1)
print(city_2)
print(city_3)
print(city_4)
print(city_5)
print(city_6)
print(city_7)

#Number 9
print(cities_in_uganda[1:4])

#Number 10
first_name = ("Mayega",) #When making tuples containing one item, add a comma afterwards so that it isnot treated as a String
last_name = ("Alvin", "Kenneth")
full_name = first_name + last_name
print(full_name)

#Number 11
colours = ("Red", "Blue", "Green", "Yellow", "Violet")
product = colours * 3
print(product)

#Number 12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))