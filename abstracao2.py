# Python program showing
# abstract base class work

from abc import ABC, abstractmethod

class Polygon(ABC):

	@abstractmethod
	def noofsides(self):
		pass

class Triangle(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("Eu tenho 3 lados")

class Pentagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("Eu tenho 5 lados")

class Hexagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("Eu tenho 6 lados")

class Quadrilateral(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("Eu tenho 4 lados")

# Driver code
R = Triangle()
R.noofsides()


class Animal(ABC):
    def move(self):
	    pass

class Human(Animal):
    def move(self):
	    print("Eu posso andar e correr")

class Snake(Animal):
    def move(self):
	    print("Eu posso rastejar")

class Dog(Animal):
    def move(self):
	    print("Eu posso latir")

class Lion(Animal):
    def move(self):
	    print("Eu posso rugir")

R = Human()
R.move()
K = Snake()
K.move()
R = Dog()
R.move()
K = Lion()
K.move()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()



class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# This will raise an error because Animal is an abstract class
# a = Animal()

dog = Dog()
print(dog.speak()) # Output: "Woof!"

cat = Cat()
print(cat.speak()) # Output: "Meow!"
