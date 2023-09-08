"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""
from abc import ABC, abstractmethod

# Abstract base class for Shapes
class Shape(ABC):
    # Abstract method that can be inherited by subclasses
    # This is a decorator
    @abstractmethod
    def set_values(self):
        pass
    @abstractmethod
    def area(self):
        pass

# Rectangle is a subclass that inherits from Shape
class Rectangle(Shape):
    def set_values(self, width, height):
        # Make the width and height a private variable with a double underscore
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height


if __name__ == "__main__":

    # Create a rectangle object
    rect = Rectangle()

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())
