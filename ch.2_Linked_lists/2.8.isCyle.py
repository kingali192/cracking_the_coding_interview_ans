"""
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head == None or head.next == None:
        return False
        
    slow = fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
                
    if fast == None or fast.next == None:
        return False
    elif fast == slow:
        return True
        
    return False