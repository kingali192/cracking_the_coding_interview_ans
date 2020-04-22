"""
 Write a method to replace all spaces in a string with '%20'. 
 You may assume that the string has sufficient space at the end to hold the additional characters, 
 and that you are given the "true" length of the string.
"""

def urlify(str1):
    spaceCount = 0
    for i in str1:
        if i == ' ':
            spaceCount += 1
    
    truelength = len(str1)
    index = truelength + spaceCount*2
    if truelength < len(str1):
        str1[truelength] = '/0'
        
    for i in range(truelength-1, 0):
        if str1[i] == ' ':
            str1[index - 1] = '0'
            str1[index - 2] = '2'
            str1[index - 3] = '%'
            index = index - 3
        else:
            str1[index - 1] = str[i]
            index -= 1
    
    return str1

    

if __name__ == '__main__':
    stringg = 'hello world we out here'
    print urlify(stringg)
    

