"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from stack_singly_linked_list import LinkedList
from stack_singly_linked_list import Node


# LINKED LIST IMPLEMENTATION -------------------------------------------------
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        # count = 0
        # current = self.storage.head
        # while current:
        #     current = current.get_next()
        #     count += 1
        # return count
        return self.size

    def push(self, value):
        # set a new node that has the input value
        self.size += 1
        return self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_tail()


# ARRAY IMPLEMENTATION -----------------------------------------------------
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size = len(self.storage)

#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             popped = self.storage.pop()
#             self.size = len(self.storage)
#             return popped

