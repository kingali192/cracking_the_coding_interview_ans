"""
Write code to remove duplicates from an unsorted linked list.
"""
class linkedList:
    def __init__(self):
        self.value = value
        self.next = next
        
def removeDups(List):
    elements = {}
    while List:
        if List.value not in elements:
            elements[List.value] = 1
            List = List.next
        else:
            List.next = List.next.next
    return List

if __name__ == '__main__':
    pass

