class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.index = 0

    def append(self, item):
        self.storage[self.index] = item
        self.index += 1
        if self.index >= self.capacity: self.index = 0


    def get(self):
        return [item for item in self.storage if item is not None]

