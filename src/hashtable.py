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

        # hash key
        index = self._hash_mod(key)

        # create way to go to node corresponding to the hashed key
        node = self.storage[index]

        # check if bucket location (index) is empty
        if node is None:
            self.storage[index] = LinkedPair(key,value)
            return

        else: 
            # handle collision
            # assign current node to temp var; which will become the previous node
            prev = node

            # while the basket location is occupied; not None
            while node is not None:
                print(f"WARNING!  A Collision has Occurred!  Assigning to index: {index} Linked List.")
                # check if the key already exists; if so, overwrite it.
                if node.key is key:
                    oldvalue = node.value
                    print(f"WARNING!  Existing key: {key}, value Reassignment Occurred! Changed from {oldvalue} to {value}.")
                    node.key = LinkedPair(key, value)
                    break

                # assign current node to prev var so once the node with None is found we can create the node and assign it key, value
                prev = node 
                # assign node to next node in Linked List
                node = node.next
            
            # once node is None, create the node and assign it to the next None node. aka add to the end of Linked List
            prev.next = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # reference to the array location potentially containing Linked List node of hashed key
        node = self.storage[index]
        # initilizing temp var holding previous node
        prev = None 
        # while array index location/node isn't empty and the key in Linked List does NOT match the requested key, traverse Linked List
        while node is not None and node.key != key:
            # hold the current node in temp var; prev
            prev = node
            # assign node to next to check for match
            node = node.next

        # node should now evaluate to either the FOUND node or None.
        if node is None:
            # print error
            print(f"ERROR: {key} not found.")
            return 
        # Found the node; remove it
        else: 
            self.count -= 1
            found_node = node.value

            if prev is None:
                self.storage[index] = node.next
                return
            
            else: 
                '''
                    point prev.next(deleted node pointer) to NEXT NEXT node from the KNOWN prev node
                    i.e. p = prev node, d = deleted node, n = next node
                    p -> d -> n
                    # next next 
                    p  ->   ->  n
                '''
                prev.next = prev.next.next
            
            return found_node
        
        # if self.storage[index] and self.storage[index] is not None:
        #     self.storage[index] = None
        # else:
        #     print(f"WARNING! {key} was not found.")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        # hashing key
        index = self._hash_mod(key)

        # hold the array index of hashed key
        node = self.storage[index]

        # traversing nodes at node/array basket/index location.  if the basket has something in it and it doesn't match the key we are seeking; reassign node var to the next node in the basket.
        while node is not None and node.key != key:
            node = node.next

        # if node is None, return None
        if node is None:
            return None

        # if node found, return the node value
        else: 
            print(f"FOUND IT!  Key: {node.key}, Value: {node.value}.")
            return node.value


        # if self.storage[index] and self.storage[index] is not None:
            # return self.storage[index][0], self.storage[index][1]
            # print(f"key: {self.storage[index][0]}, value: {self.storage[index][1]}")
            # return f"key: {self.storage[index][0]}, value: {self.storage[index][1]}"


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        print("\n")
        # item is the node within the array[index] location/basket.
        for item in old_storage:
            while item is not None:
                print(f"Key: {item.key}, Value: {item.value}.")
            # if item is not None:
                self.insert(item.key, item.value)
                item = item.next


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
