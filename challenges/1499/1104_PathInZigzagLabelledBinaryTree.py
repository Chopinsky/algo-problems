'''
1104. Path In Zigzag Labelled Binary Tree

In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]

Constraints:

1 <= label <= 10^6
'''

from typing import List


class Solution:
  def pathInZigZagTree(self, label: int) -> List[int]:
    upper = 2
    level = 1
    
    while upper-1 < label:
      upper <<= 1
      level += 1
      
    # print(upper, level)
    ans = [label]
    
    while level > 1:
      if level % 2 == 1:
        offset = ((upper-1) - ans[-1]) // 2
        ans.append((upper//4) + offset)
        
      else:
        offset = (ans[-1] - (upper//2)) // 2
        ans.append((upper//2)-1-offset)
      
      upper >>= 1
      level -= 1
      # print(ans, offset, upper)
      
    ans.reverse()
    return ans
    