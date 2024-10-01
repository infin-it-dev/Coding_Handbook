#!/bin/bash

# This is a Bash script that teaches the basics of Bash scripting.

# Print a welcome message.
echo "Welcome to the Bash scripting tutorial!"

# Ask the user for their name.
echo "What is your name?"
read name

# Print a greeting to the user.
echo "Hello, $name!"

# Ask the user for their age.
echo "How old are you?"
read age

# Print a message based on the user's age.
if [ $age -lt 18 ]; then
  echo "You are not old enough to vote."
else
  echo "You are old enough to vote."
fi

# Ask the user for a number.
echo "Enter a number:"
read num

# Print a message based on the user's number.
if [ $num -eq 0 ]; then
  echo "Your number is zero."
elif [ $num -gt 0 ]; then
  echo "Your number is positive."
else
  echo "Your number is negative."
fi

# Print a closing message.
echo "Thanks for learning Bash scripting with us!"
