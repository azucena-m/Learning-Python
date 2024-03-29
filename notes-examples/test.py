#variables
# a program is built by a series of statements, you can run more than one statements by placing a semi colon after each statement
name = "Beau"; print(name)

#you can check the type of variable by checkig it with type. eg: print(type(name)) (print is used in this case so that we can see it in the console)

#can also utilize isinstace to check type. eg: print(isinstance(name,str)) (in this case we need 2 parameters, we are checking if the variable name is a str)

#python has int and float for decimals
#you can make a value that is an int into a float eg: age = float(2) --this is called casting

#Can run

#python keywords: for, if, while, import etc. 
#a statement is an operation on a value
#an expression returns a value


# arithmatic operators
1 + 1 #2
2 - 1 #1
2 * 2 #4
4 / 2 #2
4 % 3 #1
4 ** 2 #16 4 to the power of 2
5 // 2 #2 4 divided by 2 and floored, meaning after division it is rounded down
age = 8
age += 8 # age = age + 8


#boolean operators
condition1 = True
condition2 = False

not condition1 #false
condition1 and condition2 #false
condition1 or condition2 #true


#ternary operator
def is_adult(age):
    if age > 18:
        return True
    else:
        return False
    
def is_adult2(age):
    return True if age > 18 else False #same as top but using a ternary operator

#strings
name = "Beau"
name += " is my name" #will add is my namea at the end of the original value creating Beau is my name
age = str(39)
print("""Beau is
      39
      years old""") #by adding 3 quotes you create multi line strings

print("beau".upper()) #capitalizes all letters
print("bEAu person".title()) #capitalizes the first letter of each word
print("BEAU".lower()) #makes all letters lowercase
print("Beau".islower()) #checks to see if all letters are lowercase

#global functions
print(len(name)) #prints the length of the value of the variable


#escaping quotes
name = "be\"au\" "


#slicing
print(name[1:3]) #starts at the first index and ends before the second index

#complex numbers, using the j as an imaginary number
complex_num = 2 +3j
num = complex(2,3) #complex number constructor, the second number is the imaginary number
print(num.real, num.imag) #prints the real number in this case 2 and the imaginary number 3


#rounding numbers
print(round(5.49, 1)) #if you place a comma and number after the number you want rounded it will round to that specification, in this case to the tenths place. 5.5


#library importing for nums, from enum import Enum, some people use enums to create constants
class State(Enum): #this is assuming you have imprted the enum library
    INACTIVE = 0
    ACTIVE = 1
print(State.ACTIVE.value) #this prints the value stored in active


#---lists essential data structures (similar to arrays is js)
dogs = ["Roger", "Syd"]
print("Roger" in dogs) #this is to check if something is in the list
dogs[2] = "Beau" #this updates the list at index 2, changing syd to beau
dogs.append("Judah") #this will add an item at the end of the list
dogs.extend(["Toby", 5]) #this will do similar to append but can add multiple items
dogs += ["Toby", 5] #same thing as extend, and you need [] brackets on both

#sorting method
items = ["Roger", "bob", "Beau", "Quincy"]
items.sort(key=str.lower)  #the parameters inside the () lower case all letters so that they can be properly sorte, without this python sorts by capital letters first
print(items)

#making a copy of the sorted lis
itemscopy = items[:] #by slicing but not providing indices you copy the items list


#----Tuples another data structure, cannot be modified, created similar to lists but using parenthesis instead of brackets
names = ('Roger', 'Syd')
names.index('Roger') #this will return the index number
len(names) #getting the length


#---Dictionaries data structure the creates key value pairs (similar to objects in js)
dog = { 'name': 'Roger', 'age': 8, 'color': 'green'}
print(dog['name']) #will print rodger

print(dog.popitem()) #will remove the last key item pair in the dictionary

dog['favorite food'] = 'meat' # this will add a key value pair at the end of the dictionary
del dog['color'] #will delete the key pair of color
dogCopy = dog.copy() #will make a copy of dog


#----Sets another imprtant data structure, they work like Tuples, they have an immutable set. no key value pairs, similar to list but in curly braces. 
set1 = {'Roger', 'Syd'}
set2 = {'Roger'}
intersect = set1 & set2 #you can intersect, where both sets have common item, what they have in common
mod = set1 | set2 #you can create a union, but if there is a duplicate name it will only return that once
difference = set1 - set2 #this checks for the difference, so if there are two names that are the same in both sets it will not return them, but will return a name that is in one list and not the other


#----Functions, create sets of instructions to be run when needed, mush be indented inside the block of instructions
def hello():
    print('hello!')
def hello(name="my friend"):
    print("Hello " + name) #this is an optional parameter, if you do not pass in an arugment at callback it will return "my friend" instead
def hello(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old!") #using two parameters, but changing the age into a string

def talk(phrase): #nested functions
    def say(word):
        print(word)

    words = phrase.split('')
    for word in words:
        say(word)

talk('I am goint to buy the milk')

def count():
    count = 0
    def increment():
        nonlocal count #nonlocal allows us the access the variable that was declared outside this function called count in the inner function
        count = count + 1
        print(count)

    increment()
count()


#closures, a special way of doing a function in python
def counter():
    count = 0
    def increment():
        nonlocal count
        count = count + 1
        return count
    return increment

increment = counter()
print(increment())
print(increment())
print(increment())



#---Objects, everything in python is an object similar to js
#they have attributes and methods


##loops
#two kinds, while and for loops
condition = True
while condition == True:
    print('The condition is True')
    condition = False #added this to stop the loop, otherwise, it will be infinite

count = 0
while count < 10:
    print('The condition is True')
    count = count + 1

items = [1, 2, 3, 4]
for item in items:
    print(item) #commonly used for items in a list

#items = [1, 2, 3, 4]
#for index, item in enumerate(items):
#    print(item) /the enumerate will return the items and the index number

for item in range(15):
    print(item) #using range function you can loop until you hit that target in range

#break and continue in loops
items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue #continue stops the current iteration and tells python to start the next one, break stops the loop all together
    print(item)

#--classes, from classes we can instantiate objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print('woof') 
    
roger = dog()
print(roger.name)
print(roger.age)
roger.bark()


#--modules, every python file is a module
 

 # Lambda functions, have no name and have only one expression in the body, it has to return a value.Can be assigned to variables
lambda num : num * 2
multiply = lambda a, b : a * b
print(multiply(2, 4))


# map, filter, reduce
#reduce has to be imported: from functools import reduce

# recursion, a function can call itself

# deocrators, inhance or change a function, eg: @logtime

# docstrings, documment the goal of code for you or others
#they follow convections and processed automatically, eg """ this is what this code is doing""" can be accessed through helper methods and other methods to get information about the code


# annotations, allow us to optionally declary the variable type

#exceptions, a way to handle errors in a try block  

# list compressions, this syntax is sometimes preferred over loops
numbers = [1, 2, 3, 4, 5]
numbers_power_2 = [n**2 for n in numbers]


# Polymorphyism generelizes a functionality so it can work on different types

