# Single Responsibility Principle (SRP):
# This class adheres to SRP by having each method responsible for a single task.
from abc import ABC, abstractmethod


class Calculator:
    def add(self, x, y):
        """Adds two numbers."""
        return x + y

    def subtract(self, x, y):
        """Subtracts two numbers."""
        return x - y

    def multiply(self, x, y):
        """Multiplies two numbers."""
        return x * y

    def divide(self, x, y):
        """Divides two numbers."""
        return x / y


# Open/Closed Principle (OCP):
# This example demonstrates OCP by allowing extension (new shapes) without modifying existing code.
class Shape:
    def area(self):
        """Abstract method for calculating area."""
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculates the area of a rectangle."""
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates the area of a circle."""
        return 3.14 * self.radius ** 2


# Liskov Substitution Principle (LSP):
# Bird subclasses can be substituted for the Bird superclass without affecting program correctness.
class Bird:
    def fly(self):
        """Abstract method for flying."""
        pass


class Sparrow(Bird):
    def fly(self):
        """Implements flying behavior for Sparrow."""
        print("Sparrow is flying")


class Ostrich(Bird):
    def fly(self):
        """Ostrich cannot fly, adhering to LSP."""
        raise NotImplementedError("Ostrich cannot fly")


# Interface Segregation Principle (ISP):
# Machines adhere to ISP by implementing only the methods they need.
class Machine:
    def print_document(self):
        """Abstract method for printing a document."""
        pass

    def scan_document(self):
        """Abstract method for scanning a document."""
        pass


class Printer(Machine):
    def print_document(self):
        """Implements printing behavior for Printer."""
        print("Printing document")


class Scanner(Machine):
    def scan_document(self):
        """Implements scanning behavior for Scanner."""
        print("Scanning document")


class Photocopier(Machine):
    def print_document(self):
        """Implements printing behavior for Photocopier."""
        print("Printing document")

    def scan_document(self):
        """Implements scanning behavior for Photocopier."""
        print("Scanning document")


# Dependency Inversion Principle (DIP):
# Formatters adhere to DIP by depending on abstractions (Formatter) rather than concrete implementations.


class Formatter(ABC):
    @abstractmethod
    def format(self, text):
        """Abstract method for formatting text."""
        pass


class PlainTextFormatter(Formatter):
    def format(self, text):
        """Implements text formatting for plain text."""
        return f"{text}"


class HtmlFormatter(Formatter):
    def format(self, text):
        """Implements text formatting for HTML."""
        return f"<p>{text}</p>"


# Example of using Calculator class (Single Responsibility Principle):
calculator = Calculator()
result = calculator.add(5, 3)
print("Addition result:", result)

# Example of using Rectangle and Circle classes (Open/Closed Principle):
rectangle = Rectangle(4, 5)
circle = Circle(3)
print("Area of Rectangle:", rectangle.area())
print("Area of Circle:", circle.area())

# Example of using Sparrow and Ostrich classes (Liskov Substitution Principle):
sparrow = Sparrow()
ostrich = Ostrich()
sparrow.fly()  # Outputs: Sparrow is flying
# ostrich.fly()  # Uncommenting this line will raise NotImplementedError

# Example of using Printer, Scanner, and Photocopier classes (Interface Segregation Principle):
printer = Printer()
scanner = Scanner()
photocopier = Photocopier()
printer.print_document()  # Outputs: Printing document
scanner.scan_document()  # Outputs: Scanning document
photocopier.print_document()  # Outputs: Printing document
photocopier.scan_document()  # Outputs: Scanning document

# Example of using PlainTextFormatter and HtmlFormatter classes (Dependency Inversion Principle):
plain_formatter = PlainTextFormatter()
html_formatter = HtmlFormatter()
plain_text = plain_formatter.format("This is a plain text.")
html_text = html_formatter.format("This is an HTML text.")
print("Plain text:", plain_text)
print("HTML text:", html_text)
