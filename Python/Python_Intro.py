#This is Python Code
#Python is used for many things, including: web development, data science, machine learning, and more!
#Python is a high-level programming language, which means it is easy for humans to read and write.
#Python is an interpreted language, which means that it is translated one line at a time.
#Python is an object-oriented language, which means it manipulates programming constructs called objects.
#Python is a beginner-friendly language, which means it is easy to learn.



# This program will ask the user for their name and age, and then greet them and tell them how old they will be in 10 years.

# Ask the user for their name and declaring the variable 'name'
name = input("What is your name? ")

# Ask the user for their age and declaring the variable 'age'
age = int(input("What is your age? "))

# Calculate the user's age in 10 years and calls the variable 'age' to add 10 years to the user's age
age_in_10_years = age + 10

# Greet the user and tell them how old they will be in 10 years
print("Hello, " + name + "! In 10 years, you will be " + str(age_in_10_years) + " years old.")
