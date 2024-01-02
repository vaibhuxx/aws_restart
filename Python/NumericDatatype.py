'''
Lab 109

Lab overview
Python makes it easier to do math. In fact, Python is a popular language among data scientists, who must analyze large amounts of data. In this lab, you will explore the basic data types that are used to store numeric values.

In this lab, you will:

Use the Python shell
Use the int data type
Use the float data type
Use the complex data type
Use the bool data type

Addition -> + Operator
Subtraction -> - Operator
Multiplication -> * Operator
Division -> / Operator
Modules (To get Remainder) -> % Operator

'''
'''
 A function is a piece of reusable code with a name. You use a function by:

Calling by its name
Including a list of one or more inputs called arguments, which are enclosed in parentheses
Python has several built-in functions that you can use to help you write more useful programs.

A collection of functions is called a library. Python’s collection of built-in functions is called the Python Standard Library.


Creating a variable
A variable is like a labeled box that stores information. You can change the contents of the box, but the label stays the same. In this activity, you will use the variable name myValue, but will store different data types in that labeled box.



'''

print("Python has three numeric types : int, float, and complex")
myValue=1
print(myValue)
print(type(myValue))
print(str(myValue)+"is of the data type"+str(type(myValue)))

#Exercise 3
'''
The int data type only stores whole numbers. If you want to store a number with a decimal, like 3.14, you need a new data type called a float.

'''
myVal = 3.14
print(myVal)
print(type(myVal))
print(str(myVal)+ "is of the data type"+str(type(myVal)))


#Exercise 4

'''
In advanced math, an imaginary number is a complex number that can be written as a real number that is multiplied by the imaginary unit i. This complex data type is complicated because it must represent a letter and a number, such as 5j.

'''
myValue = 5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

#Exercise 5
'''
The bool (Boolean) data type comprises the permanent names True and False, which are represented by the numerals 1 and 0, where 1 = True and 0 = False. The bool data type is implemented as a subset of int and is not considered a real data type. However, in some programming languages, it is implemented as a different data type. These exercises call the Python bool a fake data type.
'''
myValue=True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue=False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

