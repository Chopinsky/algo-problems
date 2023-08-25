'''
Serialization is the process of converting a data structure or object 
into a sequence of bits so that it can be stored in a file or memory 
buffer, or transmitted across a network connection link to be reconstructed 
later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no 
restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and 
this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes 
a binary tree. You do not necessarily need to follow this format, so please be 
creative and come up with different approaches yourself.

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Example 4:

Input: root = [1,2]
Output: [1,2]

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-1000 <= Node.val <= 1000
'''


from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Codec:
  def serialize(self, root: Optional[TreeNode]) -> str:
    """Encodes a tree to a single string.
    :type root: TreeNode
    :rtype: str
    """
    
    if not root:
      return "null"
    
    ans = ""
    stack = [root]
    nxt = []
    
    while stack:
      for node in stack:
        if node:
          ans += f'{node.val},'
          nxt.append(node.left)
          nxt.append(node.right)

        else:
          ans += 'null,'
          
      if all(node == None for node in nxt):
        break
        
      stack, nxt = nxt, stack
      nxt.clear()
      
    # print(ans[:-1])
    return ans[:-1]


  def deserialize(self, data: str) -> Optional[TreeNode]:
    """Decodes your encoded data to tree.
    :type data: str
    :rtype: TreeNode
    """
    
    src = data.split(",")
    # print(src)
    
    def build(val: str) -> Optional[TreeNode]:
      if val == 'null':
        return None
      
      return TreeNode(int(val))
    
    if len(src) == 1:
      return build(src[0])
    
    root = TreeNode(int(src[0]))
    curr, nxt = [root], []
    idx = 1
    
    while idx < len(src):
      for node in curr:
        node.left = build(src[idx])
        node.right = build(src[idx+1])
        idx += 2
        
        if node.left:
          nxt.append(node.left)
          
        if node.right:
          nxt.append(node.right)
      
      curr, nxt = nxt, curr
      nxt.clear()
    
    return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))