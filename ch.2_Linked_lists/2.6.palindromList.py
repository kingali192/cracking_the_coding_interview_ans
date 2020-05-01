"""
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
    dictionary = {}
    node = head
    while node:
        if node.val not in dictionary:
            dictionary[node.val] = 1
        else:
            dictionary[node.val] += 1
        node = node.next
        
    count = 0
    for value in dictionary.keys():
        if value%2 != 0:
            count +=1
        
        
    if count > 1:
        return False
    return True


def isPalindrom2(self, head):
    numList = []
    while head is not None:
        numList.append(head.val)
        head = head.next 
    
    return numList == numList[::-1]
