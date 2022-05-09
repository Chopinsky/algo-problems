'''
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

Constraints:

0 <= key, value <= 10^6
At most 10^4 calls will be made to put, get, and remove.
'''

from bisect import bisect_left


class MyHashMap:
  def __init__(self):
    self.keys = [[] for _ in range(1009)]
    self.vals = [[] for _ in range(1009)]


  def put(self, key: int, value: int) -> None:
    k = key % 1009
    idx = bisect_left(self.keys[k], key)
    
    if not self.keys[k] or idx >= len(self.keys[k]):
      self.keys[k].append(key)
      self.vals[k].append(value)
    elif self.keys[k][idx] == key:
      self.vals[k][idx] = value
    else:
      self.keys[k].insert(idx, key)
      self.vals[k].insert(idx, value)


  def get(self, key: int) -> int:
    k = key % 1009
    idx = bisect_left(self.keys[k], key)
    
    if not self.keys[k] or idx >= len(self.keys[k]) or self.keys[k][idx] != key:
      return -1
    
    return self.vals[k][idx]


  def remove(self, key: int) -> None:
    k = key % 1009
    idx = bisect_left(self.keys[k], key)
    
    if not self.keys[k] or idx >= len(self.keys[k]) or self.keys[k][idx] != key:
      return
    
    self.keys[k].pop(idx)
    self.vals[k].pop(idx)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)