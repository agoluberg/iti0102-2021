"""EX01 hello."""
"""
1. Print Hello
Example output:

What is your name? Mari
Hello, Mari! Enter a random number: 5
Great! Now enter a second random number: 4
5 + 4 is 9

"""
# ask for a name
name = input("What is your name? ")
# ask for first random number
num1 = int(input(f"Hello, {name}! Enter a random number: "))
# ask for second random number
num2 = int(input("Great! Now enter a second random number: "))
# print out sum
print(num1, "+", num2)
"""
2. Poem
Example output:

Roses are red,
violets are blue,
I love to code
And so will you!

"""
color = "red"
objects = "violets"
activity = "code"

print(color + objects)

"""
3. GreetingsGreetingsGreetings
Example output:

Enter a greeting: Hello
Enter a recipient: world
How many times to repeat: 3
Hello world! Hello world! Hello world!
    
"""
greeting = "Hello"
print(greeting)
