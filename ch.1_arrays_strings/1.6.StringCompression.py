"""
 Implement a method to perform basic string compression using the counts of repeated characters. 
 For example, the string aabcccccaaa would become a2blc5a3. 
 If the "compressed" string would not become smaller than the original string, 
 your method should return the original string. 
 You can assume the string has only uppercase and lowercase letters (a - z).
"""

def StringCompression(str):
    solution = ''
    count = 0
    j = 1
    for i in range(len(str)):
        if str[j] == str[i]:
            j+=1
            count += 1
        else:
            solution += str[i] + count
            i = j
            count = 0
    if len(solution) < len(str):
        return solution
    return str
            

if __name__ == '__main__':
    pass