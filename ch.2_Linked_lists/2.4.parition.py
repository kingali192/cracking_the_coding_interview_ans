"""
Write code to partition a linked list around a value x, such that all nodes 
less than x come before all nodes greater than or equal to x. 
If x is contained within the list, the values of x only need to be after the 
elements less than x (see below). The partition element x can appear anywhere 
in the "right partition"; it does not need to appear between the left and right partitions.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
def partition(self, head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
        # The idea is everythin bigger is put into the bigger and everything smaller is put into the smaller

    smaller = smaller_head = ListNode(0)
    bigger = bigger_head = ListNode(0)
    mid = ListNode(x)
    while head:
        if head.val < x:
            smaller.next = head
            smaller = smaller.next
        else:
            bigger.next = head
            bigger = bigger.next
            
        head = head.next
        
    bigger.next = None
    smaller.next = bigger_head.next
    return smaller_head.next # smaller_head is 0


if __name__ == '__main__':
    pass

