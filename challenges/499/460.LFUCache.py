'''
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3

Constraints:

0 <= capacity <= 10^4
0 <= key <= 10^5
0 <= value <= 10^9
At most 2 * 10^5 calls will be made to get and put.
'''


from collections import defaultdict, OrderedDict
from heapq import heappush, heappop


class LFUCache0:
  '''
  used internal library, i.e. OrderedDict, to help with the implementation
  '''
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.freq_to_key = defaultdict(OrderedDict)
    self.key_to_freq = defaultdict(int)
    self.min_freq = 1


  def get(self, key: int) -> int:
    if key not in self.key_to_freq:
      return -1
    
    freq = self.key_to_freq[key]
    self.key_to_freq[key] = freq + 1
    
    value = self.freq_to_key[freq][key]
    self.freq_to_key[freq].pop(key, None)
    self.freq_to_key[freq+1][key] = value
    
    if self.min_freq == freq and not self.freq_to_key[freq]:
      self.min_freq += 1
      
    return value


  def put(self, key: int, value: int) -> None:
    if key in self.key_to_freq:
      # update the freq as well
      self.get(key)
      freq = self.key_to_freq[key]
      self.freq_to_key[freq][key] = value

    else:
      self.capacity -= 1
      self.key_to_freq[key] = 1
      self.freq_to_key[1][key] = value
      
      if self.capacity < 0:
        self.capacity += 1
        k, v = self.freq_to_key[self.min_freq].popitem(False)
        self.key_to_freq.pop(k, None)

      self.min_freq = 1


class LFUCache:
  def __init__(self, capacity: int):
    self.store = {}
    self.cap = capacity
    self.counter = defaultdict(list)
    self.freq = []
    self.id = 0
    
    
  def update_counter(self, key: int):
    self.id += 1
    
    if key in self.store:
      old_cnt = self.store[key][1]
      self.store[key][1] += 1
      self.store[key][2] = self.id
      
      # pop out all stale states first
      while self.counter[old_cnt]:
        top_id, top_key = self.counter[old_cnt][0]
        if top_key not in self.store:
          heappop(self.counter[old_cnt])
          continue
          
        top_cnt, key_id = self.store[top_key][1], self.store[top_key][2]
        if top_cnt != old_cnt or top_id != key_id:
          heappop(self.counter[old_cnt])
          continue
          
        break
        
      if not self.counter[old_cnt]:
        self.counter.pop(old_cnt, None)
        if self.freq and self.freq[0] == old_cnt:
          heappop(self.freq)
          
      heappush(self.counter[old_cnt+1], (self.id, key))
      if (not self.freq) or (self.freq[0] != old_cnt+1):
        heappush(self.freq, old_cnt+1)
      
    else:
      self.evict()
      self.store[key] = [0, 1, self.id]
      
      heappush(self.counter[1], (self.id, key))
      if (not self.freq) or (self.freq[0] != 1):
        heappush(self.freq, 1)
      
      
  def evict(self):
    if len(self.store) < self.cap:
      return
    
    while (self.freq) and (self.freq[0] not in self.counter):
      heappop(self.freq)
      
    if not self.freq:
      return
    
    done = False
    while not done and self.freq and self.counter:
      curr_freq = self.freq[0]
      key_id, key = heappop(self.counter[curr_freq])

      if key in self.store and self.store[key][2] == key_id and self.store[key][1] == curr_freq:
        self.store.pop(key, None)
        done = True

      if not self.counter[curr_freq]:
        self.counter.pop(curr_freq, None)
        while (self.freq) and (self.freq[0] not in self.counter):
          heappop(self.freq)


  def get(self, key: int) -> int:
    if not self.cap:
      return -1
    
    if key in self.store:
      self.update_counter(key)
      # print('get', key, self.store, self.counter, self.freq)
      return self.store[key][0]
    
    # print('get: none', key, self.store, self.counter, self.freq)
    return -1


  def put(self, key: int, value: int) -> None:
    if not self.cap:
      return
    
    self.update_counter(key)
    self.store[key][0] = value
    # print('put', key, value, self.store, self.counter, self.freq)

    
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)