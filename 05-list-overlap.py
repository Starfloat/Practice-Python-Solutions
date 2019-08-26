# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:
1. Randomly generate two lists to test this
2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""
import random

a=[]
b=[]
for i in range(25):
    a.append(random.randint(0,25))
    b.append(random.randint(0,20))
a.sort()
b.sort()
print(a)
print(b)

def list_common_elements(a,b):
    common_list = []
    for i in a:
        for j in b:
            if i == j and i not in common_list:
                common_list.append(i)
    print(common_list)
list_common_elements(a,b)
        
        
