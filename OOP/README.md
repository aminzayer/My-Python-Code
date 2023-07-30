
# Python OOP Repository

## Object-Oriented Programming Principles

In order to achieve better development and organized code in Python, the principles of Object-Oriented Programming (OOP) are of great importance. OOP is a programming approach that allows you to modularize and extend a program using separate and independent components. Below are some OOP principles that can be helpful in developing Python projects, along with code examples:

### 1. Abstraction

Abstraction means hiding the complex details and only showing the essential features. In Python, abstraction can be achieved using classes and methods. Think of classes as templates for creating objects, exposing only the necessary methods and attributes.

```python
# Python example of abstraction
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self, width, height):
        return width * height

```

### 2. Encapsulation

Encapsulation means bundling the attributes and behaviors related to an object within a class. In Python, you can achieve this principle by limiting access to attributes and methods using access specifiers (e.g., public, private, protected).

```python
# Python example of encapsulation

class Car:
    def __init__(self):
        self.__speed = 0  # Private attribute

    def accelerate(self):
        self.__speed += 10

    def get_speed(self):
        return self.__speed

my_car = Car()
my_car.accelerate()
print(my_car.get_speed())  # Output: 10

```

### 3. Polymorphism

Polymorphism means that you can perform a similar operation on different objects. In Python, polymorphism can be achieved through inheritance and also with functions and methods that accept multiple parameters.

```python
# Python example of polymorphism
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

def make_sound(animal):
    return animal.sound()

dog = Dog()
cat = Cat()

print(make_sound(dog))  # Output: Woof!
print(make_sound(cat))  # Output: Meow!

```

### 4. Inheritance

Inheritance means inheriting attributes and behaviors of one class by another class. This principle allows classes to be arranged in a hierarchical or multiple inheritance structure to reflect various structures in projects.

```python
# Python example of inheritance
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

```

### 5. Composition

Composition means combining smaller objects to form a larger object. This principle allows you to create diverse and complex structures using classes and objects.

```python
# Python example of composition
class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()

my_car = Car()
print(my_car.start())  # Output: Engine started.

```

### 6. Encapsulation (again, as it's an important principle)

Encapsulation means hiding the internal components of a class from the outside. This principle reduces complexity and improves the code structure.

```python
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

# Usage:
account = BankAccount(1000)
print(account.get_balance())  # Output: 1000
account.deposit(500)
print(account.get_balance())  # Output: 1500
account.withdraw(200)
print(account.get_balance())  # Output: 1300

```

### 7. Dependency Injection

Dependency Injection means providing the required dependencies of a class from outside. This principle allows you to change the structure and behavior of your program.

```python
class EmailSender:
    def send_email(self, recipient, subject, body, smtp_server):
        # Code for sending email using the provided smtp_server
        print(f"Email sent to {recipient} with subject '{subject}'.")

# Usage:
smtp_server_1 = "smtp.example.com"
smtp_server_2 = "smtp.anotherexample.com"

email_sender_1 = EmailSender()
email_sender_2 = EmailSender()

email_sender_1.send_email("user@example.com", "Hello", "This is a test email.", smtp_server_1)
email_sender_2.send_email("anotheruser@example.com", "Greetings", "This is another test email.", smtp_server_2)

```

In the end, using Object-Oriented Programming principles in Python helps make your code extendable, maintainable, and readable. These principles enable you to create organized and modular code, allowing for better project management and scalability.
