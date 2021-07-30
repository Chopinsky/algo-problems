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