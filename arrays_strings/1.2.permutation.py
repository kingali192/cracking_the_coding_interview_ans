"""
Given two strings,write a method to decide if one is a permutation of the
other.
Solution 1: two strings sorted are equal to each other: O(nlogn)
Solution 2: check if each letter is in the other string: O(n)
Solution 3: One string into a dictionary and lookup + same length?
"""
from collections import Counter

def permutations1(str1, str2):
    return sorted(str1) == sorted(str2)

def permutations2(str1, str2):
    for letter in str1:
        if letter not in str2:
            return False
    return True

def permutations3(str1, str2):
    pass
    

if __name__ == '__main__':
    string1 = 'caat'
    string2 = 'taca'
    print permutations1(string1, string2)
    print permutations2(string1, string2)