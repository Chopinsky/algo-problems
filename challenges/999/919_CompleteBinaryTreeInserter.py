'''
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

Implement the CBTInserter class:

CBTInserter(TreeNode root) Initializes the data structure with the root of the complete binary tree.
int insert(int v) Inserts a TreeNode into the tree with value Node.val == val so that the tree remains complete, and returns the value of the parent of the inserted TreeNode.
TreeNode get_root() Returns the root node of the tree.

Example 1:


Input
["CBTInserter", "insert", "insert", "get_root"]
[[[1, 2]], [3], [4], []]
Output
[null, 1, 2, [1, 2, 3, 4]]

Explanation
CBTInserter cBTInserter = new CBTInserter([1, 2]);
cBTInserter.insert(3);  // return 1
cBTInserter.insert(4);  // return 2
cBTInserter.get_root(); // return [1, 2, 3, 4]
 

Constraints:

The number of nodes in the tree will be in the range [1, 1000].
0 <= Node.val <= 5000
root is a complete binary tree.
0 <= val <= 5000
At most 10^4 calls will be made to insert and get_root.
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class CBTInserter:
  def __init__(self, root: Optional[TreeNode]):
    def count(root: Optional[TreeNode]):
      if not root:
        return 0, 0
      
      if not root.left and not root.right:
        return 1, 1
      
      lh, lc = count(root.left)
      rh, rc = count(root.right)
      
      if lh == rh:
        lc += rc
        
      return lh+1, lc
    
    h, count = count(root) 
    self.root = root
    self.count = 1 << (h-1)
    self.id = count
    
    if self.id == self.count:
      self.count <<= 1
      self.id = 0

    # print(h, count, self.count, self.id)
      
      
  def insert(self, val: int) -> int:
    mask = (self.count >> 1)
    curr = self.root
    
    while mask > 1:
      if mask & self.id == 0:
        curr = curr.left
      else:
        curr = curr.right
      
      mask >>= 1
    
    node = TreeNode(val=val)
    if mask & self.id == 0:
      curr.left = node
    else:
      curr.right = node
    
    self.id += 1
    if self.id == self.count:
      self.count <<= 1
      self.id = 0
      
    return curr.val


  def get_root(self) -> Optional[TreeNode]:
    return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()