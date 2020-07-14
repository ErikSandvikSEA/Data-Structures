"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # capture the old head
            old_head = self.head

            # change the head to the new value
            self.head = new_node

            # set the new head's next to the old_head
            self.head.next = old_head

            # set the old head's prev to be the new value
            old_head.prev = new_node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.length == 0:
            return None

        elif self.length == 1:
            self.length -= 1
            old_head = self.head
            self.head = None
            self.tail = None

            return old_head.value
        else:
            old_head = self.head
            self.length -= 1
            new_head = self.head.next
            self.head = new_head
            return old_head

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            # set both the head and tail to be the new_node
            self.head = new_node
            self.tail = new_node
        else:
            # capture old_tail
            old_tail = self.tail

            # give the old tail a next pointer that points to the new tail
            old_tail.next = new_node
            # set tail to be new_node
            self.tail = new_node
            # set the new tail's prev to point to the old tail
            self.tail.prev = old_tail

        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.length == 0:
            return None

        # capture old_tail
        old_tail = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
            self.length -= 1
            return old_tail.value
        else:
            self.tail = old_tail.prev
            self.tail.next = None
            self.length -= 1
            return old_tail.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.length == 0:
            return None
        elif node is self.head:
            return
        elif node is self.tail:
            self.remove_from_tail()
            self.add_to_head(node.value)
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
            self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.length == 0:
            return None
        elif node is self.tail:
            return
        elif node is self.head:
            self.remove_from_head()
            self.add_to_tail(node.value)
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
            self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        elif node is self.tail:
            left_node = node.prev
            self.tail = left_node
            self.tail.next = None
            self.length -= 1
        elif node is self.head:
            self.head = node.next
            self.head.prev = None
            self.length -= 1
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.head.value
        else:
            current_node = self.head
            current_max = self.head.value

            while current_node is not None:
                if current_node.value > current_max:
                    current_max = current_node.value
                current_node = current_node.next

            return current_max

