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