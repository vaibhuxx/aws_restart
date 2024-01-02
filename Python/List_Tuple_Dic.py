#Lab111
'''
Lab overview
In Python, string and numeric data types are often used in groups called collections. Three such collections that Python supports are the list, the tuple, and the dictionary.

In this lab, you will:

Use the list data type
Use the tuple data type
Use the dictionary data type___

'''
#Exercise 1
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
'''
Accessing a list by position
You can access the contents of a list by position. In this activity, you will print out each item in our list by their position:

In programming languages, the list position starts at zero (0). The brackets tell Python which position in the list you want. To access the apple string, enter the following code

'''
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
'''
Changing the values in a list
The values of a list can be changed. In this activity, you will change cherry to orange

'''
myFruitList[2] = "orange"
print(myFruitList)


#Exercise 2
'''
Defining a tuple
The tuple is like a list, but it can't be changed. A data type that can't be changed after it's created is said to be immutable. To define a tuple, you use parentheses instead of brackets ([]).

'''
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
'''Accessing a tuple by position'''
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#Exercise 3
'''Defining a dictionary
A dictionary is a list with named positions (keys). Imagine that your list shows people’s favorite fruit.'''


myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
'''Accessing a dictionary by name'''
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])


