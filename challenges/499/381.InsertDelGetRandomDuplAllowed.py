'''
Implement the RandomizedCollection class:

RandomizedCollection() Initializes the RandomizedCollection object.
bool insert(int val) Inserts an item val into the multiset if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the multiset if present. Returns true if the item was present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
int getRandom() Returns a random element from the current multiset of elements (it's guaranteed that at least one element exists when this method is called). The probability of each element being returned is linearly related to the number of same values the multiset contains.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:

Input
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]
Output
[null, true, false, true, 2, true, 1]

Explanation
RandomizedCollection randomizedCollection = new RandomizedCollection();
randomizedCollection.insert(1);   // return True. Inserts 1 to the collection. Returns true as the collection did not contain 1.
randomizedCollection.insert(1);   // return False. Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
randomizedCollection.insert(2);   // return True. Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
randomizedCollection.getRandom(); // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
randomizedCollection.remove(1);   // return True. Removes 1 from the collection, returns true. Collection now contains [1,2].
randomizedCollection.getRandom(); // getRandom should return 1 and 2 both equally likely.

Constraints:

-2^31 <= val <= 2^31 - 1
At most 2 * 10^5  calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
'''


from random import randint
from collections import defaultdict
from heapq import heappushpop, heappush, heappop


class RandomizedCollection:
  def __init__(self):
    self.idx = defaultdict(set)
    self.stack = list()


  def insert(self, val: int) -> bool:
    has_val = (val in self.idx and len(self.idx[val]) > 0)
    # print(self.idx)
    
    self.idx[val].add(len(self.stack))
    self.stack.append(val)
    
    return not has_val
  

  def remove(self, val: int) -> bool:
    if (val not in self.idx) or not self.idx[val]:
      return False
    
    rdx, last = self.idx[val].pop(), len(self.stack)-1
    
    if rdx != last:
      last_val = self.stack[last]
      self.stack[rdx], self.stack[last] = self.stack[last], self.stack[rdx]

      self.idx[last_val].discard(last)
      self.idx[last_val].add(rdx)
    
    self.stack.pop()
    
    return True
    

  def getRandom(self) -> int:
    if len(self.stack) == 1:
      return self.stack[0]
    
    idx = randint(0, len(self.stack)-1)
    return self.stack[idx]
        

class RandomizedCollection0:
  def __init__(self):
    self.container = defaultdict(list)
    self.stack = list()


  def insert(self, val: int) -> bool:
    has_val = (val in self.container and len(self.container[val]) > 0)
    heappush(self.container[val], -len(self.stack))
    self.stack.append(val)
    
    return not has_val
  

  def remove(self, val: int) -> bool:
    if val not in self.container or not self.container[val]:
      return False
    
    idx = -heappop(self.container[val])
    last = len(self.stack)-1
    
    if idx != last:
      vlast = self.stack[last]
      # print('pop', val, vlast, self.stack, self.container, idx, last)
      self.stack[last], self.stack[idx] = self.stack[idx], self.stack[last]
      heappushpop(self.container[vlast], -idx)
    
    self.stack.pop()
    # print(self.stack, self.container)
    
    return True
    

  def getRandom(self) -> int:
    if len(self.stack) == 1:
      return self.stack[0]
    
    idx = randint(0, len(self.stack)-1)
    return self.stack[idx]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()