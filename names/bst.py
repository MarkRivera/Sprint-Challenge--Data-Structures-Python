
from queue import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        
        found = False
        if self.value > target:
            if self.left is None:
                return False
            found = self.left.contains(target)

        if self.value < target:
            if self.right is None:
                return False
            found = self.right.contains(target)
        
        return found

    def get_max(self):
        max = None
        if self.right is None:
            max = self.value
        else:
            if self.value > self.right.value:
                max = self.value
            else:
                max = self.right.get_max()
        return max

    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)

        fn(self.value)


        if self.right:
            self.right.for_each(fn)

    def in_order_print(self):
        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()

    def bft_print(self):
        q = Queue()
        q.enqueue(self)
        while len(q) != 0:
            current = q.dequeue().value
            print(current.value)
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)

    def dft_print(self):
        print(self.value)
        if self.left:
            self.left.dft_print()
        if self.right:
            self.right.dft_print()