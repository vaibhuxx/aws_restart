'''
Lab overview
In Python, a collection of letters and symbols is called a string. Strings are used often in Python for input and output.

In this lab, you will:

Write Python code that uses the string data type
Concatenate strings
Use the string to get input
Format strings for output

'''
#Lab 110
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

'''
String concatenation is the process of combining two strings into one string. You have actually been doing string concatenation since lab 1, but you didn’t call this process by that term. The plus sign (+) is used to concatenate strings. When the plus sign (+) is used with strings, it behaves differently than when you use it for numbers. In lab 1, you used the plus sign (+) to add numbers. Now, you will use the plus sign (+) to combine, or concatenate, strings.

'''
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#Exercise 3
'''
In coding, information that a user enters is known as input. You will use a built-in function named input() to get information from the user. The input() function will pause the code until a user enters a string and presses ENTER. Return to the Python script:

'''
name = input("What is your name? ")
print(name)

#Exercise 4
'''
When your script wants to communicate information back to the user, it is called output. You have been using the print() function to write output to the shell. You will create a survey and output the information that it collects back to the user.

'''
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))


