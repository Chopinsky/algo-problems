'''
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.

For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.

Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.

It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid.

For example, it could never contain two consecutive commas, such as "1,,3".
Note: You are not allowed to reconstruct the tree.

Example 1:

Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true

Example 2:

Input: preorder = "1,#"
Output: false

Example 3:

Input: preorder = "9,#,#,1"
Output: false
 

Constraints:

1 <= preorder.length <= 10 ** 4
preoder consist of integers in the range [0, 100] and '#' separated by commas ','.
'''


class Solution:
  def isValidSerialization(self, preorder: str) -> bool:
    if not preorder:
      return True
    
    stack = []
    for val in preorder.split(','):
      while val == '#' and stack and stack[-1] == '#':
        # pop the 'left' branch
        stack.pop()
        
        # if there's no parent node to the 2 null nodes, invalid tree
        if not stack:
          return False
        
        # pop the parent, since it's valid from this node blow
        stack.pop()
        
      # use the placeholder to mark the tree as either valid (i.e. '#'), or
      # has a value to the left
      stack.append(val)
    
    return stack == ['#']
  
    
  def isValidSerialization0(self, preorder: str) -> bool:
    arr = [int(s) if s != '#' else -1 for s in preorder.split(',')]
    # print(arr)
    
    def is_valid(i: int) -> Tuple[bool, int]:
      j = len(arr)-1
      
      if i > j:
        return (False, i)
      
      if i == j and arr[i] == -1:
        return (True, i)
      
      if arr[i] == -1:
        return (True, i)
      
      lv, li = is_valid(i+1)
      
      if not lv:
        return (False, li)
      
      return is_valid(li+1)
      
    valid, end = is_valid(0)
    # print(valid, end)
    
    return (valid and end == len(arr)-1)
  
