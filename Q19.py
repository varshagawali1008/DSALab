size = 10
hash_table = [None] * size

def hash_function(key):
    return key % size

def insert(key):
    index = hash_function(key)
    while hash_table[index] is not None:
        index = (index + 1) % size
    hash_table[index] = key

keys = [23, 43, 13, 27]
for k in keys:
    insert(k)

print("Hash Table:", hash_table)
