# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def LinkedPair_insert(lp, key, value):
    if lp.key == key:
        lp.value = value
    elif lp.next is None:
        lp.next = LinkedPair(key, value)
    else:
        LinkedPair_insert(lp.next, key, value)

def LinkedPair_remove(lp, key):
    if lp.key == key:
        return lp.next

    if lp.next is not None:
        if lp.next.key == key:
            lp.next = lp.next.next
        else:
            LinkedPair_remove(lp.next, key)
    return lp

def LinkedPair_retrieve(lp, key):
    if lp is None:
        return None
    elif lp.key == key:
        return lp.value
    else:
        return LinkedPair_retrieve(lp.next, key)

def dump_LinkedPair(lp, l):
    if lp is None:
        return l
    else:
        l.append((lp.key, lp.value))
        dump_LinkedPair(lp.next, l)


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        '''

        hash = 5381

        for c in key:
            hash = hash * 33 + ord(c)
        
        return hash


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        address = self._hash_mod(key)
        if self.storage[address] is None:
            self.storage[address] = LinkedPair(key, value)
        else:
            LinkedPair_insert(self.storage[address], key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        address = self._hash_mod(key)
        if self.storage[address] is not None:
            self.storage[address] = LinkedPair_remove(self.storage[address], key)


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        address = self._hash_mod(key)
        if self.storage[address] is not None:
            return LinkedPair_retrieve(self.storage[address], key)

        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        temp_list = []
        for l in self.storage:
            dump_LinkedPair(l, temp_list)

        self.capacity *= 2

        self.storage = [None] * self.capacity

        for key, value in temp_list:
            self.insert(key, value)

        del temp_list



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
