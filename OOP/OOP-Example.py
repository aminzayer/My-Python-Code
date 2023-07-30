# Object Oriented Programing Example
class MyClass:
    def __init__(self, param1, param2) -> None:
        self.param1 = param1
        self.param2 = param2

    def MyClassMethod1(self):
        # perform some action
        print(self.param1)

    def MyClassMethod2(self):
        # perform some action
        print(self.param2)


# Create new instance of Class
Myobjectclass = MyClass(10, 20)
Myobjectclass.MyClassMethod1()


class Sample():

    def_name = 'amin'
    def_age = '39'

    def __init__(self, name='amin', age=39):
        self.def_name = name
        self.def_age = age

    def method_print_All(self):
        print('Name :', self.def_name, ' Age :', self.def_age)


MyClass1 = Sample()
MyClass1.method_print_All()

MyClass2 = Sample('Ali', 40)
MyClass2.method_print_All()

# Inheritance in python
# Parent Class


class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        print('helo')

    def report(self):
        print(f'I am {self.first_name} {self.last_name}')


x = Person('Amin', 'Zayeromali')
x.report()

# Child Class


class Agent(Person):

    def __init__(self, first_name, last_name, code_name):
        Person.__init__(self, first_name, last_name)
        self.code_name = code_name

    def report(self):
        print(f'I Am Here. My code is {self.code_name} (override method)')

    def reveal(self, passcode):

        if passcode == 123:
            print("I am a secret agent!")
        else:
            self.report()


x1 = Agent('Amin', 'Zayer', 'mr.X')
x1.reveal(123)
x1.report()

# Special Method on Python OOP
class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Print Sepecial Methode
    def __str__(self):
        return f"{self.title} written by {self.author}"

    def __len__(self):
        return self.pages

mybook = Book('Python','Amin Zayer',120)
print(mybook)
print(len(mybook))


# Abstraction example
class Shape:

    def area(self):
        pass


class Rectangle(Shape):

    def area(self, width, height):
        return width * height


# Encapsulation example
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


# Polymorphism example
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


# Inheritance example
class Animal:

    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        return "Woof!"


class Cat(Animal):

    def sound(self):
        return "Meow!"


# Composition example
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