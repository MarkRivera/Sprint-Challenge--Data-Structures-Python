class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self.prev, current_next)
        if current_next:
            current_next.prev = self.next
    
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def add_to_head(self, value):
        self.length += 1
        node = ListNode(value)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def remove_from_head(self):
        self.length -= 1
        if not self.head and not self.tail:
            return
        elif self.head == self.tail:
            removed_value = self.head.value
            self.head = None
            self.tail = None
            return removed_value
        else:
            next_node = self.head.next
            self.head = next_node
        return self.head.value        
            
    def add_to_tail(self, value):
        self.length += 1
        node = ListNode(value)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            
    def remove_from_tail(self):
        self.length -= 1
        if not self.head and not self.tail:
            return
        elif self.head == self.tail:
            removed_value = self.head.value
            self.head = None
            self.tail = None
            return removed_value
        else:
            prev_node = self.tail.prev
            # The Switch to the prev node happens here:
            self.tail = prev_node
        return self.tail.value
            
    def move_to_front(self, node):
        self.add_to_head(node.value)
        self.delete(node)
        return self.head.value
        
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    def delete(self, node):
        if not self.head and not self.tail:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.head == node:
            self.head = node.next
            self.length -= 1
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            self.length -= 1
            node.delete()
        else:
            self.length -= 1
            node.delete()

    def get_max(self):
        current_node = self.head
        highest_value = 0

        if self.head == self.tail:
            highest_value = self.head.value
            return highest_value

        while current_node.next is not None:
            current_node = current_node.next
            if current_node.value > highest_value:
                highest_value = current_node.value

        return highest_value