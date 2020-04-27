"""
 Implement an algorithm to delete a node in the middle 
 (i.e., any node but the first and last node, not necessarily the exact middle) 
 of a singly linked list, given only access to that node.
"""

def deleteMiddle(node):
    # fast and slow pointer
    fast = node
    slow = node
    while fast and slow:
        slow = slow.next
        fast = fast.next.next
        if fast == None:
            slow = slow.next.next
    return node


if __name__ == '__main__':
    pass
