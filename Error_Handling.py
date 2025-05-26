number1 = int(input("Give me a number: "))
number2 = int(input("Give me another number: "))
    
while True:
    if number2 == 0:
        print("You can't divide by zero.")
        number2 = int(input("Give me another number: "))
    else:
        division = number1/number2
        print(f"\n{number1} divided by {number2} gives you {division}")
        break