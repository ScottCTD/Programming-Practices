# 705. Design HashSet
# Easy
# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
#
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet,
# do nothing.

# 2023-05-29 22:24:11
# original
# time 22.2% space 58.91%
class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.hash_set = [[]] * self.size

    def add(self, key: int) -> None:
        if not self.contains(key):
            hashed = key % self.size
            self.hash_set[hashed].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            hashed = key % self.size
            self.hash_set[hashed].remove(key)

    def contains(self, key: int) -> bool:
        hashed = key % self.size
        return key in self.hash_set[hashed]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)