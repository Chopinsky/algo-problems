'''
Given a list of ascending three-digits integers representing a 
binary with the depth smaller than 5. You need to return the 
sum of all paths from the root towards the leaves.

If the depth of a tree is smaller than 5, then this tree can 
be represented by a list of three-digits integers.

For each integer in this list:

- The hundreds digit represents the depth D of this node, 1 <= D <= 4.
- The tens digit represents the position P of this node in the level 
  it belongs to, 1 <= P <= 8. The position is the same as that in a 
  full binary tree.
- The units digit represents the value V of this node, 0 <= V <= 9.

Example 1:

Input: [113, 215, 221]
Output: 12

Explanation: 
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.

Example 2:

Input: [113, 221]
Output: 4

Explanation: 
The tree that the list represents is: 
    3
     \
      1

The path sum is (3 + 1) = 4.
'''


from typing import DefaultDict, List


class Solution:
  def path_sum_iv(self, arr: List[int]) -> int:
    if not arr:
      return 0

    total = 0
    tree = {}

    for val in arr:
      lvl = val // 100
      val -= lvl * 100

      pos = val // 10
      val -= pos * 10
      
      if lvl not in tree:
        tree[lvl] = [-1] * 8

      tree[lvl][pos-1] = val

    # print(tree)

    def get_path_sum(level: int, pos: int, s: int):
      nonlocal total

      # illegal cases
      if (level not in tree) or (tree[level][pos] < 0):
        return

      # get children nodes
      l, r = 2*pos, 2*pos+1
      curr_sum = s + tree[level][pos]

      # we're at the leaf
      if (level+1 not in tree) or (tree[level+1][l] < 0 and tree[level+1][r] < 0):
        total += curr_sum
        return

      # iterate left branch if it exists
      if tree[level+1][l] >= 0:
        get_path_sum(level+1, l, curr_sum)
      
      # iterate right branch if it exists
      if tree[level+1][r] >= 0:
        get_path_sum(level+1, r, curr_sum)

    get_path_sum(1, 0, 0)

    return total


s = Solution()
t = [
  [[113, 215, 221], 12],
  [[113, 221], 4],
]

for arr, ans in t:
  res = s.path_sum_iv(arr)
  print('\n========\nTest Case:', arr)
  print('Expected:', ans)
  print('Result  :', res)
