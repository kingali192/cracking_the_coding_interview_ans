"""
Given a string, write a function to check if it is a permutation of a palin­drome. 
A palindrome is a word or phrase that is the same forwards and backwards. 
A permutation is a rearrangement of letters. T
he palindrome does not need to be limited to just dictionary words.
"""

def PalindromePermutation(str1):
    # build a dictionary from the letters of the string, and if all keys or all keys except for one %2 then True else False
    str_dict = {}
    for letter in str1:
        if letter not in str_dict:
            str_dict[letter] = 1
        else:
            str_dict[letter] += 1
    
    count = 0
    for key, value in str_dict:
        if value %2 != 0:
            count += 1
    
    if count > 1:
        return False
    return True
    



if __name__ == '__main__':
    pass