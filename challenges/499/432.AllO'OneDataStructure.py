'''
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
 

Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 10^4 calls will be made to inc, dec, getMaxKey, and getMinKey.
'''

class Node:
  def __init__(self, lvl: int):
    self.lvl = lvl
    self.keys = set()
    self.nxt = None
    self.prev = None
    
  def append(self, node):
    if not node:
      return
    
    nxt = self.nxt
    self.nxt = node
    node.prev = self
    
    if nxt:
      node.nxt = nxt
      nxt.prev = node
      
  def remove(self):
    prev = self.prev
    nxt = self.nxt
    self.prev = None
    self.nxt = None
    
    if prev:
      prev.nxt = nxt
      
    if nxt:
      nxt.prev = prev

  def __repr__(self):
    return f'Node(lvl={self.lvl},key={self.keys})'
      
      
class AllOne:
  def __init__(self):
    self.key = {}
    self.head = Node(lvl=0)
    self.tail = Node(lvl=-1)
    self.head.append(self.tail)
    # self._print('init:')

  def inc(self, key: str) -> None:
    if key not in self.key:
      old_lvl = self.head
    else:
      old_lvl = self.key[key]
      
    if not old_lvl.nxt or old_lvl.nxt.lvl != old_lvl.lvl+1:
      nxt_lvl = Node(lvl=old_lvl.lvl+1)
      old_lvl.append(nxt_lvl)
    else:
      nxt_lvl = old_lvl.nxt
      
    self.key[key] = nxt_lvl
    
    old_lvl.keys.discard(key)
    nxt_lvl.keys.add(key)
    if not old_lvl.keys and old_lvl != self.head:
      old_lvl.remove()
    
    # print(self.key)
    # self._print(f'inc:{key}')

  def dec(self, key: str) -> None:
    if key not in self.key:
      return
    
    old_lvl = self.key[key]
    if not old_lvl.prev or old_lvl.prev.lvl != old_lvl.lvl-1:
      prev_lvl = None if old_lvl.lvl == 1 else Node(lvl=old_lvl.lvl-1)
      if old_lvl.prev and prev_lvl:
        old_lvl.prev.append(prev_lvl)
    else:
      prev_lvl = old_lvl.prev
    
    if prev_lvl:
      if prev_lvl != self.head:
        self.key[key] = prev_lvl
        prev_lvl.keys.add(key)
      else:
        del self.key[key]
    else:
      del self.key[key]
      
    old_lvl.keys.discard(key)
    if not old_lvl.keys:
      old_lvl.remove()
    
    # self._print(f'dec:{key}')
    
  def getMaxKey(self) -> str:
    # self._print('max ==>')
    if not self.key or self.tail.prev == self.head:
      return ""
    
    return next(iter(self.tail.prev.keys))

  def getMinKey(self) -> str:
    # self._print('min ==>')
    if not self.key or self.tail.prev == self.head:
      return ""
        
    return next(iter(self.head.nxt.keys))

  def _print(self, title=""):
    if title:
      print(title)
    
    curr = self.head
    while curr:
      print(curr)
      curr = curr.nxt
    
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
