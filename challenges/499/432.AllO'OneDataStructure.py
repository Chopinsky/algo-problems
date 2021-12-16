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


from typing import Optional
from bisect import bisect_right


class DLNode:
  def __init__(self, val: int, nxt: Optional['DLNode'] = None, prev: Optional['DLNode'] = None):
    self.val = val
    self.next = nxt
    if nxt:
      nxt.prev = self
      
    self.prev = prev
    if prev:
      prev.next = self
    
    
class AllOne:
  def __init__(self):
    self.index = {}
    self.counts = []
    self.keys = []
    

  def inc(self, key: str) -> None:
    if key not in self.index:
      idx = bisect_right(self.counts, 1)
      
      self.counts.insert(idx, 1)
      self.keys.insert(idx, key)
      self.index[key] = idx

      for i in range(idx+1, len(self.counts)):
        self.index[self.keys[i]] += 1
        
    else:
      idx = self.index[key]
      count = self.counts[idx]
      
      if idx == len(self.counts) - 1:
        self.counts[-1] += 1
        
      else:
        j = idx
        while j < len(self.counts) and self.counts[j] == count:
          j += 1
          
        self.index[self.keys[j-1]], self.index[key] = self.index[key], self.index[self.keys[j-1]]
        self.counts[idx], self.counts[j-1] = self.counts[j-1], self.counts[idx]
        self.keys[idx], self.keys[j-1] = self.keys[j-1], self.keys[idx]
        self.counts[j-1] += 1


  def dec(self, key: str) -> None:
    idx = self.index[key]
    count = self.counts[idx]

    if count == 1:
      self.counts.pop(idx)
      self.keys.pop(idx)
      del self.index[key]
      for i in range(idx, len(self.keys)):
        self.index[self.keys[i]] -= 1

    else:
      if idx == 0:
        self.counts[0] -= 1
        
      else:
        j = idx
        while j >= 0 and self.counts[j] == count:
          j -= 1

        self.index[self.keys[j+1]], self.index[key] = self.index[key], self.index[self.keys[j+1]]
        self.counts[idx], self.counts[j+1] = self.counts[j+1], self.counts[idx]
        self.keys[idx], self.keys[j+1] = self.keys[j+1], self.keys[idx]
        self.counts[j+1] -= 1


  def getMaxKey(self) -> str:
      if self.counts: 
        return self.keys[-1]

      return ""

  def getMinKey(self) -> str:
      if self.counts: 
        return self.keys[0]

      return ""
        

class AllOne0:
  def __init__(self):
    self.counts = {}
    self.nums = {}
    self.head = None
    self.tail = None


  def inc(self, key: str) -> None:
    if key not in self.counts:
      # this is a new key
      self.counts[key] = 1
        
      if 1 not in self.nums:
        # curr is the head
        self.head = DLNode(1, self.head)
        self.nums[1] = [self.head, set([key])]
        
        if not self.tail:
          self.tail = self.head
        
      else:
        # curr is a duplciate head
        self.nums[1][1].add(key)
        
    else:
      old_cnt = self.counts[key]
      nxt_cnt = old_cnt + 1
      self.counts[key] = nxt_cnt
      
      # if old_cnt not in self.nums:
      #   print(key, old_cnt, self.nums)

      # remove from the old count
      if len(self.nums[old_cnt][1]) == 1:
        node = self.nums[old_cnt][0]
        node.val += 1
        self.nums.pop(old_cnt, None)

      else:
        self.nums[old_cnt][1].discard(key)
        node = DLNode(nxt_cnt)
        node.prev = self.nums[old_cnt][0]
        
      if nxt_cnt not in self.nums:
        # create a new count
        self.nums[nxt_cnt] = [node, set([key])]
        if node.prev:
          node.prev.next = node
        
        if node.val > self.tail.val:
          self.tail = node
          
      else:
        # the next node exists
        self.nums[nxt_cnt][1].add(key)
        curr = self.nums[nxt_cnt][0]
        curr.prev = node.prev
        
        if node.prev:
          node.prev.next = curr
          

  def dec(self, key: str) -> None:
    if key not in self.counts:
      return
    
    old_cnt = self.counts[key]
    nxt_cnt = old_cnt - 1
    
    if nxt_cnt > 0:
      self.counts[key] = nxt_cnt
    else:
      self.counts.pop(key, None)
    
    if len(self.nums[old_cnt][1]) == 1:
      node = self.nums[old_cnt][0]
      node.val -= 1
      self.nums.pop(old_cnt, None)
      
    else:
      self.nums[old_cnt][1].discard(key)
      node = DLNode(nxt_cnt)
      node.next = self.nums[old_cnt][0]
      
    if nxt_cnt > 0:
      if nxt_cnt not in self.nums:
        # create a new count
        self.nums[nxt_cnt] = [node, set([key])]
        if node.next:
          node.next.prev = node

        if node.val < self.head.val:
          self.head = node

      else:
        # the next node exists
        self.nums[nxt_cnt][1].add(key)
        curr = self.nums[nxt_cnt][0]
        curr.next = node.next

        if node.next:
          node.next.prev = curr
          
    else:
      # print('popping:', key, self.head.val)
      if (1 not in self.nums) and (self.head.val <= 1):
        self.head = self.head.next
        
        if self.head:
          self.head.prev = None
        else:
          self.tail = None
        

  def getMaxKey(self) -> str:
    if not self.tail:
      return ''
    
    return list(self.nums[self.tail.val][1])[0]


  def getMinKey(self) -> str:
    if not self.head:
      return ''
    
    # print(self.head.val, self.nums)
    return list(self.nums[self.head.val][1])[0]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()