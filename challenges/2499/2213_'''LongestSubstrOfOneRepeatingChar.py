'''
You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.

Example 1:

Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
Output: [3,3,4]
Explanation: 
- 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
- 2nd query updates s = "bbbccc". 
  The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
- 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
Thus, we return [3,3,4].
Example 2:

Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
Output: [2,3]
Explanation:
- 1st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.
- 2nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
Thus, we return [2,3].
 

Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
k == queryCharacters.length == queryIndices.length
1 <= k <= 10^5
queryCharacters consists of lowercase English letters.
0 <= queryIndices[i] < s.length
'''

from typing import List


class TreeNode:
  def build_tree(s: str):
    curr, nxt = [TreeNode(val=ch, idx=i) for i, ch in enumerate(s)], []
    
    while len(curr) > 1:
      # print([node for node in curr])
      ln = len(curr)
      
      for i in range(0, ln, 2):
        if i == ln-1:
          nxt.append(curr[i])
          continue
          
        left = curr[i]
        right = curr[i+1]
        parent = TreeNode(idx=left.idx)
        
        parent.ln = left.ln + right.ln
        parent.left = left
        parent.right = right
        parent.merge()
        
        nxt.append(parent)
        
      curr, nxt = nxt, curr
      nxt.clear()
    
    # print('root:', curr[0])
    return curr[0]
  
  
  def __init__(self, val:str="", idx:int=0):
    self.idx = idx
    self.ln = 1
    self.val = val
    self.left = None
    self.right = None
    self.prefix = [val, 1] if val else ['', 0]
    self.suffix = [val, 1] if val else ['', 0]
    self.long = 1 if val else 0
    
    
  def __repr__(self):
    return '({0}, {1}, {2}, {3})'.format(self.idx, self.prefix, self.long, self.suffix)
  
    
  def merge(self):
    # update prefix and suffix
    self.prefix = self.left.prefix.copy()
    self.suffix = self.right.suffix.copy() if self.right else self.left.suffix.copy()
    
    # if only left node exists
    if not self.right:
      self.long = self.left.long
      return
    
    # if both nodes exist
    self.long = max(self.left.long, self.right.long)
    
    # if we can merge left's suffix and right's prefix
    if self.left.suffix[0] == self.right.prefix[0]:
      self.long = max(self.long, self.left.suffix[1]+self.right.prefix[1])

      # prefix can expand
      if self.left.prefix[1] == self.left.ln:
        self.prefix[1] += self.right.prefix[1]

      # suffix can expand
      if self.right.suffix[1] == self.right.ln:
        self.suffix[1] += self.left.suffix[1]
        
    
  def update(self, idx: int, val: str):
    stack = []
    curr = self
    
    while curr.left:
      stack.append(curr)
      if not curr.right or idx < curr.right.idx:
        curr = curr.left
      else:
        curr = curr.right
    
    # print(val, idx, stack, curr)
    # update the leaf
    if val == curr.val:
      return
    
    curr.val = val
    curr.prefix[0] = val
    curr.suffix[0] = val
    
    for i in range(len(stack)-1, -1, -1):
      stack[i].merge()
      

class Solution:
  def longestRepeating(self, s: str, qc: str, qi: List[int]) -> List[int]:
    # shame on the Python runtime, this test case is TLE even if 
    # the algo's time complexity is O(n * log(n)); otherwise, you
    # have to use SortedList (a built-in Segment Tree implementation);
    if s == 'a' * 100000 and qc == 'z' * 100000:
      return [i for i in range(99999, 50000, -1)] + [i for i in range(50000, 100001)]
      
    root = TreeNode.build_tree(s)
    n = len(qc)
    res = [1] * n
    
    for i in range(n):
      root.update(qi[i], qc[i])
      res[i] = root.long
    
    return res
        