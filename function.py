def welcome(name):
    print("Hello",name)
    print("welcome to python")
welcome("python")
welcome("java")

def greek(name,city,age):
    print("hello",name)
    print("welcome to",city)
    print("your age is",age)
greek("harish","hindupur",27)

def college(name,address,grade,marks):

    print("my name is",name)
    print("my college address is",address)
    print("our college grade",grade)
    print("my semister marks are",marks)
college("harish","chittoor","A+",93)

def display_result(name, total, percentage):
    print("Student Name:", total)
    print("Total Marks:", name)
    print("Percentage:", percentage)
 
display_result("harish",355,95)

#comment code

print("this is a comment code")

def add(a,b):
    return a+b
result=add(10,20)
print(result)

def calculate(a,b):
    addition=a+b
    substraction=a-b
    multiplication=a*b
    division=a/b
    return addition,substraction,multiplication,division
x,y,z,w=calculate(10,5)
print("Addition:",x)
print("Subtraction:",y)
print("Multiplication:",z)
print("Division:",w)


square = lambda x: x * x

print(square(5))

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")

student = {
    "name": "Harish",
    "age": 22,
    "course": "Python"
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()    # inherited from Animal
dog.bark()   # Dog's own method


class Dog:
    def sound(self):
        print("Dog says: Bark")


class Cat:
    def sound(self):
        print("Cat says: Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()