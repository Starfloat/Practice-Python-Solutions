# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?
Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

user_num = int(input('Enter a number to check if it is odd or even: '))

if user_num % 2 == 0:
    print('This number is an even number.')
    if user_num % 4 == 0:
        print('It is also a multiple of 4.')
else:
    print('This number is an odd number.')


num = int(input('Enter a new number: '))
check = int(input('Enter another to be divided by: '))

if num % check == 0:
    print('This number divides evenly')
else:
    print('This number is odd.')
