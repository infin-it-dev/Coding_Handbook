#Python has flexible variables, to be more specific, variables do not have a defined type. Unless you specify of course.

var_string = "this is a string!" #you can also define a string using ' ' instead of " "
var_num = 69420 #number variables like this can also be decimals without any specification EX: var_num = 420.69, the same goes for complex numbers, and longs! (Decimals are also called floats or doubles in the coding community)
var_list = ["this", "is", "a", "list!"] #lists CAN be changed and can hold any data type!
var_tuple = ("This", "is", "a", "tuple!") #tuples cannot be changed and can hold any data type!
var_enum = Enum("Colors", ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]) #enums can hold any data type! #Enums cannot be changed!
#Enums are like dictionaries but use numbers as keys! So if you wanted to get "Red" from the above Enum, you would do:
print(var_enum[1]) #Enums start at 1 instead of 0! Remember that!
var_dict = {"A" : "Apple", "B": "Book", "C" : "Cat"} #dictionaries can have strings, numbers, and variables as the key! Values can be any data type!
var_bool = True #Can ONLY be True or False!
var_set = {"this", 1, "is", "a", "set!"} #sets cannot be changed by the program after they are created! Think of them like constants

#MAKE NOTE!
#Python counts from 0! So whenever you want to find the first element in a list/tuple/etc, you want to use 0 instead of 1!

#TIPS!
#If you want to write a string with double quotes in it, use single quotes! Like this:
my_string = 'Hi!, say "Hi" back!'
#And use double quotes if you want to use single quotes in a string! Like:
my_string2 = "Hi, I'm a programmer!"


#To print out a message you would type:
print("Hello World!") #in the parenthesis you would put what you want to print out, in this case, I want the program to say Hello World!
#the print function can be used to print out variable values, strings, numbers, dictionaries, lists, etc!

#To create a function! you want to do something like this:
my_function:
  #put function code here

#If you want to create a class, you would start with this:
class my_class:
  __init__():
    #Code here

#To run the class, write the file name, then dot and your class name followed by parenthesis, like this!
Python_Data_Types.my_class()
