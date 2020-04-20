"""
Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures
"""

def isUnique(str1):
    solution_string = ''
    for letter in str1:
        if letter not in solution_string:
            solution_string += letter 
        else:
            return False     
    return True
            


if __name__ == '__main__':
    string1 = 'hello'
    string2 = 'Mohamed'
    print isUnique(string1)
    print isUnique(string2)

    