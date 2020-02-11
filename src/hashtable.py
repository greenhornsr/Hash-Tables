# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # print(hash(key))
        # breakpoint()
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # increment count
        self.count += 1

        # hash the key
        hashed_k = self._hash_mod(key)

        # create way to go to node corresponding to the hashed key
        node = self.storage[hashed_k]

        # checking if bucket location is empty
        if node is None:
            # create node, add it to location of hashed key
            self.storage[hashed_k] = LinkedPair(key, value)
            return

        # HANDLE Collision 
        # assign node to temp var
        prev = node
        
        # while the insertion node location is occupied, 
        while node is not None: 
            # hold current node in prev so once the node with None is found we can create the node and assign
            prev = node
            # assign node to next node in LL
            node = node.next
        
        # once node IS None, create the node and assign it to the next None node...aka add to end of LL
        prev.next = LinkedPair(key, value)
        # breakpoint()
        # pass



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashed_k = self._hash_mod(key)

        if not self.storage[hashed_k]:
            return f"ERROR: key not found!"

        del self.storage[hashed_k]




    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # hash key
        hashed_k = self._hash_mod(key)

        # got to storage node
        node = self.storage[hashed_k]

        # traverse LL at node
        while node is not None and node.key != key:
            node = node.next
        
        # if node is None, return None
        if node is None:
            return None
        
        # if node is found, return Node VALUE
        else: 
            return node.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        if self.count != self.capacity:
            return f"ERROR: Max capacity hasn't been reached: {self.capacity}"
        
        self.storage = [None] * self.capacity



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
