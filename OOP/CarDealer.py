# Single Responsibility Principle (SRP):
# This class follows SRP by handling only the responsibilities related to car dealership.
# It manages the inventory of cars, adding, removing, displaying them, and providing additional services.

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


class CarDealer:
    def __init__(self):
        self.inventory = []

    def add_car(self, car):
        """Adds a car to the dealer's inventory."""
        self.inventory.append(car)
        print(f"{car.brand} {car.model} added to inventory.")

    def remove_car(self, car):
        """Removes a car from the dealer's inventory."""
        if car in self.inventory:
            self.inventory.remove(car)
            print(f"{car.brand} {car.model} removed from inventory.")
        else:
            print("Car not found in inventory.")

    def show_inventory(self):
        """Displays the list of cars in the dealer's inventory."""
        if self.inventory:
            print("Dealer Inventory:")
            for idx, car in enumerate(self.inventory, start=1):
                print(f"{idx}. {car.brand} {car.model}, Price: ${car.price}")
        else:
            print("Inventory is empty.")

    def search_by_brand(self, brand):
        """Searches and displays cars by brand."""
        matching_cars = [car for car in self.inventory if car.brand == brand]
        if matching_cars:
            print(f"Cars from {brand}:")
            for car in matching_cars:
                print(f"{car.model}, Price: ${car.price}")
        else:
            print(f"No cars found from {brand}.")

    def sell_car(self, car):
        """Sells a car from the inventory."""
        if car in self.inventory:
            self.remove_car(car)
            print(f"{car.brand} {car.model} sold.")
        else:
            print("Car not found in inventory.")

# Example of using Car and CarDealer classes with additional features:


# Create some car objects
car1 = Car("Toyota", "Corolla", 15000)
car2 = Car("Honda", "Civic", 18000)
car3 = Car("Ford", "Mustang", 30000)
car4 = Car("Toyota", "Camry", 20000)

# Create a car dealer
dealer = CarDealer()

# Add cars to the dealer's inventory
dealer.add_car(car1)
dealer.add_car(car2)
dealer.add_car(car3)
dealer.add_car(car4)

# Show the dealer's inventory
dealer.show_inventory()

# Search for cars by brand
dealer.search_by_brand("Toyota")

# Sell a car
dealer.sell_car(car2)

# Show the updated inventory
dealer.show_inventory()
