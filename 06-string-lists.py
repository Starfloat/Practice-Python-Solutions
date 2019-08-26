# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)

"""
def palindrome_check(word):
    word_to_list = []
    for i in word:
        if word[0].lower() == word[-1].lower():
            word_to_list.append(i)

    if word_to_list != []:
        print(''.join(word_to_list), 'is a palindrome.')
    else:
        print(word, 'is not a palindrome.')

palindrome_check('Racecar')
        
    
