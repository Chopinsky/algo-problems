'''
146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 
Constraints:

1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.
'''


class Node:
  def __init__(self, key=0, val=0, prev=None, nxt=None):
    self.key = key
    self.val = val
    self.prev = prev
    self.nxt = nxt
    
    
  def remove(self) -> 'Node':
    prev = self.prev
    nxt = self.nxt
    
    if prev:
      prev.nxt = nxt
      
    if nxt:
      nxt.prev = prev
      
    self.prev = None
    self.nxt = None
    
    return self

    
  def insert(self, node: 'Node'):
    if not node:
      return
    
    prev = self.prev
    self.prev = node
    
    if prev:
      prev.nxt = node
    
    node.prev = prev
    node.nxt = self


class LRUCache:
  def __init__(self, capacity: int):
    self.cap = capacity
    self.store = {}
    self.head = Node()
    self.tail = Node()
    self.tail.insert(self.head)


  def get(self, key: int) -> int:
    if key not in self.store:
      return -1
    
    self.touch(key)
    return self.store[key].val


  def put(self, key: int, value: int) -> None:
    if key not in self.store:
      node = Node(key=key, val=value)
      self.store[key] = node
      self.tail.insert(node)
      
    else:
      self.store[key].val = value
      
    self.touch(key)
    
    
  def touch(self, key: int):
    if key not in self.store:
      return
    
    node = self.store[key]
    node.remove()
    self.tail.insert(node)
    
    if len(self.store) > self.cap:
      removed = self.head.nxt.remove()
      self.store.pop(removed.key, None)

      
  def debug(self, key):
    curr = self.head
    print('chain', key, self.store.keys())
    while curr:
      print(curr.val)
      curr = curr.nxt


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)