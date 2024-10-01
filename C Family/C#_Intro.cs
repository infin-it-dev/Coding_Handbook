
using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            // Declare and initialize variables
            int age = 25;
            string name = "John";
            double height = 1.75;

            // Print out the values of the variables
            Console.WriteLine("My name is " + name + ", I am " + age + " years old, and I am " + height + " meters tall.");

            // Modify the values of the variables
            age = 30;
            name = "Jane";
            height = 1.80;

            // Print out the new values of the variables
            Console.WriteLine("My name is " + name + ", I am " + age + " years old, and I am " + height + " meters tall.");
        }
    }
}
