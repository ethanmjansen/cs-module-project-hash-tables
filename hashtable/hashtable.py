class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.key}, {self.value}'

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.current_load = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.data)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        num_slots = self.get_num_slots()
        load_factor = self.current_load / num_slots

        if load_factor > 0.7:
            return self.resize(self.capacity * 2)
        else:
            return False
        

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        offset_basis = 14695981039346656037
        fnv_prime = 1099511628211
        hash = offset_basis

        for character in key:
            hash = hash * fnv_prime
            hash = hash ^ ord(character)
            
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381

        for character in key:
            hash = (hash * 33) + ord(character)

        return hash 


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.fnv1(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)

        if self.data[slot] == None:
            self.data[slot] = HashTableEntry(key, value)
        else:
            if self.data[slot] != None and self.data[slot].key != key:
                while self.data[slot] != None and self.data[slot].key != key:
                    self.data[slot] = self.data[slot].next
            else:
                self.data[slot] = HashTableEntry(key, value)


        self.current_load += 1
        self.get_load_factor()


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)
        hash_entry = self.data[slot]

        previous = None

        while previous != None and hash_entry.key != key:
            previous = hash_entry
            hash_entry = previous.next

        if hash_entry == None:
            return None
        else:
            if previous == None:
                self.data[slot] = hash_entry.next
            else:
                previous.next = hash_entry.next

        self.current_load -= 1


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)
        hash_entry = self.data[slot]

        while hash_entry != None:
            if hash_entry.key == key:
                return hash_entry.value

        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity
        old_hash = self.data
        self.data = [None] * self.capacity

        for i in old_hash:
            if i is not None:
                self.put(i.key, i.value)
            else:
                None
            

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
