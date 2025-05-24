#Number 1
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

print("The shoe size is " + str(Shoes["size"]))

#Number 2
Shoes["brand"] = "Adidas"
print(Shoes["brand"])

#Number 3
Shoes["type"] = "sneakers"
print(Shoes["type"])

#Number 4
for key in Shoes.keys():
    print("\nKey: " + str(key))
    
#Number 5
for value in Shoes.values():
    print("\nValue:" + str(value))
    
#Number 6
if "size" in Shoes:
    print("Yep, 'size' exists in the dictionary")
else:
    print("'size' is not in the dictionary")
    
#Number 7
for key, value in Shoes.items():
    print("\nKey: " + key)
    print("Value: " + str(value))

#Number 8
del Shoes["color"]
print(Shoes)

#Number 9
Shoes.clear()
print(Shoes)

#Number 10
id = {
    "Name": "Harry",
    "Age": 30,
    "Course": "Law"
}

id_copy = id.copy()
print(id_copy)

#Number 11
employees = {
    "cooks": {
        "Name": "Samuel",
        "Age":57,
        "Salary": 3000
    },
    
    "cleaners": {
        "Name": "Nantambi",
        "Age": 23,
        "Salary": 4000
    }
}