"""
You have two numbers represented by a linked list,where each node 
contains a single digit. The digits are stored in reverse order,
such that the 1's digit is at the head of the list. 
Write a function that adds the two numbers and returns the sum as a linked list.
"""
class ListNode(object):
    def __init__(self):
        self.data = data
        self.next = next
        

def sumList(self, l1, l2):
    sumval = 0
    root = curr = ListNode(0)
    while l1 or l2 or sumval:
        if l1: 
            sumval += l1.val 
            l1 = l1.next
        if l2: 
            sumval += l2.val
            l2 = l2.next
        curr.next = curr = ListNode(sumval % 10) #don't understand
        sumval //= 10 #don't understand
    return root.next
    
    result.data = value % 10 # second digit of number
     
        
if __name__ == '__main__':
    pass

