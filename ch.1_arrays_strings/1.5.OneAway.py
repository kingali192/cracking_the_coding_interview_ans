"""
There are three types of edits that can be performed on strings: 
insert a character, remove a character, or replace a character. 
Given two strings, write a function to check if they are one edit (or zero edits) away.
"""
from collections import Counter

def oneAway(str1, str2):
    # replace
    if len(str1) == len(str2):
        counter = 0
        stringDict = Counter(str1)
        for letter in str2:
            if letter not in stringDict:
                counter += 1
        
        if counter > 1:
            return False  
        return True
    
    # Take one away or add one
    elif (len(str1) - len(str2) == 1)  or (len(str2) - len(str1) == 1):
        if len(str1) > len(str2):
            longer, shorter = str1, str2
        longer, shorter = str2, str1 
        longDict = Counter(longer)
        for letter in shorter:
            if letter not in longDict:
                return False
        return True
    else:
        return False

if __name__ == '__main__':
    string1 = 'mighty'
    string2 = 'might'
    string3 = 'jazzy'
    string4 = 'maghty'
    print oneAway(string1, string2) # Should be True
    print oneAway(string2, string3) # Should be False
    print oneAway(string1, string4) # Should be True



