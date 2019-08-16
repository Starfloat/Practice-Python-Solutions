# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

'''

user_num = int(input('Enter a number: '))

a_list = []
check_list = list(range(1, user_num+1))

for i in check_list:
    if user_num%i == 0:
        a_list.append(i)
print('The divisors of', user_num, 'are', a_list)
