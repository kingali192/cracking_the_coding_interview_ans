"""
Assumeyou have a method isSubstringwhich checks if one word is a substring of another. 
Given two strings, sl and s2, write code to check if s2 is a rotation of sl 
using only one call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").
"""
from collections import Counter
def ratateString(str1, str2):
    # check if every letter in one string is in the other.
    return Counter(str1) - Counter(str2) == {}


if __name__ == '__main__':
    string1 = 'waterbottle'
    string2 = 'erbottlewat'
    string3 = 'mohamed'
    print ratateString(string1, string2)
    print ratateString(string1, string3)