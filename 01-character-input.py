# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

"""
Exercise 1 (and Solution)
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
2. Print out that many copies of the previous message on separate lines.
"""
from datetime import date

name = input('Enter your name: ')
age  = int(input('Enter your age: '))

today = date.today()
year = today.year
age_difference_from_100 = 100-age

year_to_be_100 = year + age_difference_from_100

print(name + ', you will be age 100 in the year', + year_to_be_100)
