"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""
class linkedList:
    def __init__(self):
        self.value = value
        self.next = next


def kthLast(linkedlist, place):
    length = 0
    while linkedlist:
        linkedlist = linkedlist.next
        length += 1
        
    while linkedlist:
        linkedlist = linkedlist.next
        length -= 1
        if length == place:
            return linkedlist.value
    return None

if __name__ == '__main__':
    pass

