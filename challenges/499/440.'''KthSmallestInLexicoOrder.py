'''
Given two integers n and k, return the kth lexicographically 
smallest integer in the range [1, n].

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], 
so the second smallest number is 10.

Example 2:

Input: n = 1, k = 1
Output: 1
 

Constraints:

1 <= k <= n <= 10^9
'''


class Solution:
  def findKthNumber(self, n: int, k: int) -> int:
    def cnt_nodes(val: int) -> int: 
      #Return node counts in denary trie.
      cnt, base = 0, 1
      while val <= n: 
        # if len(n) == len(val), only count those in the interval
        cnt += min(n-val+1, base)
        val *= 10    # moving down a level
        base *= 10   # for every level, there are 10 times more nodes under
        
      return cnt 

    res = 1
    while k > 1: 
      # get the nodes count under the 
      # current trie prefix 
      cnt = cnt_nodes(res)
      
      if k > cnt: 
        # moving to the right
        k -= cnt
        res += 1
        
      else: 
        # moving down the trie
        k -= 1
        res *= 10 
        
    return res
  