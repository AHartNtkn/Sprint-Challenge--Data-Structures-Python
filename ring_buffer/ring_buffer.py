from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) == 1:
           self.current = self.storage.head

        if len(self.storage) == self.capacity:
            self.current.value = item 
            if self.current is self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        flag = self.storage.head
        while flag is not None:
            list_buffer_contents.append(flag.value)
            flag = flag.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.current] = item
            if self.current is len(self.storage) - 1:
              self.current = 0
            else:
              self.current += 1
        else:
            self.storage.append(item)

    def get(self):
        return [ x for x in self.storage if x is not None ]
