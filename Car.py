class Car:
    def start(self):
        print("Starting the car...")

# Method Overriding
class ElectricCar(Car):
    def start(self):
        print("Electric car is starting silently...")

class GasCar(Car):
    def start(self):
        print("Gas car is starting with a roar!")

# MRO: Multiple inheritance
class HybridCar(ElectricCar, GasCar):
    pass

# Method Overloading (simulated)
class ServiceCenter:
    def book_service(self, *args):
        if len(args) == 1:
            print(f"Booking basic service for: {args[0]}")
        elif len(args) == 2:
            print(f"Booking {args[1]} service for: {args[0]}")
        else:
            print("Invalid service booking.")

# Test Overriding
print("--- Method Overriding ---")
car = Car()
electric = ElectricCar()
gas = GasCar()
hybrid = HybridCar()

car.start()
electric.start()
gas.start()
hybrid.start()  # Uses ElectricCar's start due to MRO

# Show MRO
print("\n--- Method Resolution Order ---")
print(HybridCar.__mro__)

# Test Overloading
print("\n--- Method Overloading (Simulated) ---")
sc = ServiceCenter()
sc.book_service("Toyota")
sc.book_service("Honda", "Full")
sc.book_service("BMW", "Oil", "Extra")  # Invalid
