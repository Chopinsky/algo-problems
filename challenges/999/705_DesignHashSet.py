'''
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)

Constraints:

0 <= key <= 10^6
At most 10^4 calls will be made to add, remove, and contains.
'''

from bisect import bisect_left


class MyHashSet:
  def __init__(self):
    self.nums = [0]*(10**6+1)


  def add(self, key: int) -> None:
    self.nums[key] |= 1


  def remove(self, key: int) -> None:
    self.nums[key] = 0


  def contains(self, key: int) -> bool:
    return self.nums[key] == 1
        

class MyHashSet:
  def __init__(self):
    self.buckets = [[]] * 1009


  def add(self, key: int) -> None:
    idx = key % 1009
    jdx = bisect_left(self.buckets[idx], key)
    if jdx < len(self.buckets[idx]) and self.buckets[idx][jdx] == key:
      return
    
    self.buckets[idx].insert(jdx, key)


  def remove(self, key: int) -> None:
    idx = key % 1009
    jdx = bisect_left(self.buckets[idx], key)
    if jdx >= len(self.buckets[idx]) or self.buckets[idx][jdx] != key:
      return
    
    self.buckets[idx].pop(jdx)


  def contains(self, key: int) -> bool:
    idx = key % 1009
    jdx = bisect_left(self.buckets[idx], key)
    return jdx < len(self.buckets[idx]) and self.buckets[idx][jdx] == key
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)