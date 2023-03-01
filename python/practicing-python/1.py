# This really brings back memories of learning to
# program for the first time. Funnily enough, I
# remember (suddenly, haven't recalled this in
# a long time) the first program I was really proud
# of was a game, maybe tic-tac-toe but I don't think so,
# but something similar, that I implemented the
# winning (and simple) algorithm for. I thought I'd
# created a simple AI (maybe I did? why not) and was
# super jazzed!

# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). If you want to do this in a generic way, see exercise 39.

# Extras:

#     Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#     Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

# add this learning project folder to github
# learn how to have auto linebreaks for comments

current_year = 2023

# how to do input sanitization?
# side note: seem to be much more engaged than normal, thinking of lots of side issues, edge cases, etc.: this is great!

name = input("Hi! Please enter your name: ")
age = int(input("Now your age, please: "))
num_copies = int(input("How many copies would you like? "))

# edge case: they're 100+ years old already!
for i in range(0,num_copies):
  print("You will be 100 years old in " + str((2023 + (100 - age))))

# write some tests
# make an alias for "python3"