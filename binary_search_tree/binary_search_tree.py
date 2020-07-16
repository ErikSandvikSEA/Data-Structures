"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the input value with the value of the Node
        # if value < Node's value
        if value < self.value:
            # we need to go left
            # if we see that there is no left child,
            if self.left is None:
                # then we can wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there is a child
            else:
                # call the left child's 'insert' method
                self.left.insert(value)
        # otherwise, value >- Node's value
        else:
            # we need to go right
            # if we see there is no right child,
            if self.right is None:
                # then we can wrap the value in a BSTNode and park it
                self.right = BSTNode(value)
            # otherwise there is a child
            else:
                # call the right child's 'insert' method
                self.right.insert(value)

    # Search logic
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.right is None and self.left is None:
            return False
        elif self.value < target:
            # check for a right to traverse to
            if self.right is not None:
                # traverse right
                if self.right.value == target:
                    return True
                else:
                    self.right.contains(target)
            else:
                return False
        else:
            # check for a left to traverse to
            if self.left is not None:
                # traverse left
                if self.left.value == target:
                    return True
                else:
                    self.left.contains(target)
            else:
                return false

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    # def for_each(self, fn):
    #     fn(self.value)
    #     if self.left is None and self.right is None:
    #         return
    #     else:
    #         if self.left is None:
    #             self.right.for_each(fn)
    #         elif self.right is None:
    #             self.left.for_each(fn)
    #         else:
    #             self.left.for_each(fn)
    #             self.right.for_each(fn)

    # lecture alt (recursive)
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        from collections import deque

        queue = deque()
        queue.append(self)

        # continue to traverse so long as there are nodes in the queue
        while len(queue) > 0:
            current_node = queue.popleft()
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # use a stack
        stack = []
        # add self to the stack
        stack.append(self)

        # so long as our stack has nodes in it, there are more nodes to traverse
        while len(stack) > 0:
            # pop the top node from the stack
            current_node = stack.pop()

            # add the current node's right child first
            if current_node.right:
                stack.append(current_node.right)

            # then add the current node's left
            if current_node.left:
                stack.append(current_node.left)

            # print
            print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

