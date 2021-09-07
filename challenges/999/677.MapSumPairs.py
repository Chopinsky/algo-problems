'''
Implement the MapSum class:

MapSum() Initializes the MapSum object.
void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.

Example 1:

Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)

Constraints:

1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase English letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.
'''


class trie:
  '''
  A better solution will be implementing the insert such that self.val == (the 
  sum of all subtree values); when inserting, we update `self.val` to either:
  1) add the val if it's a new node, or 2) add the diff between val and old node's
  val.

  Then self.sum() will be run in O(n) time, where n == length of the key. 
  '''
  def __init__(self, key: str, val: int):
    self.val = val if not key else 0
    self.children = [None] * 26
    
    if key:
      idx = ord(key[0]) - ord('a')
      self.children[idx] = trie(key[1:], val)
      
  
  def insert(self, key: str, val: int):
    if not key:
      self.val = val
      return
    
    idx = ord(key[0]) - ord('a')
    if self.children[idx]:
      self.children[idx].insert(key[1:], val)
    else:
      self.children[idx] = trie(key[1:], val)
    
    
  def sum(self, key: str) -> int:
    if key:
      idx = ord(key[0]) - ord('a')
      if not self.children[idx]:
        return 0
      
      return self.children[idx].sum(key[1:])
    
    return self.get_subtree_total()
  
    
  def get_subtree_total(self) -> int:
    base = self.val
    for ch in self.children:
      if not ch:
        continue
        
      base += ch.get_subtree_total()
      
    return base
    

class MapSum:
  def __init__(self):
      """
      Initialize your data structure here.
      """
      self.root = trie('', 0)
      # print(self.root.children)
      

  def insert(self, key: str, val: int) -> None:
    self.root.insert(key, val)
  

  def sum(self, prefix: str) -> int:
    return self.root.sum(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)