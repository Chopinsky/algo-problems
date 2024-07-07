'''
You are given a string target, an array of strings words, and an integer array costs, both arrays of the same length.

Imagine an empty string s.

You can perform the following operation any number of times (including zero):

Choose an index i in the range [0, words.length - 1].
Append words[i] to s.
The cost of operation is costs[i].
Return the minimum cost to make s equal to target. If it's not possible, return -1.

 

Example 1:

Input: target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5]

Output: 7

Explanation:

The minimum cost can be achieved by performing the following operations:

Select index 1 and append "abc" to s at a cost of 1, resulting in s = "abc".
Select index 2 and append "d" to s at a cost of 1, resulting in s = "abcd".
Select index 4 and append "ef" to s at a cost of 5, resulting in s = "abcdef".
Example 2:

Input: target = "aaaa", words = ["z","zz","zzz"], costs = [1,10,100]

Output: -1

Explanation:

It is impossible to make s equal to target, so we return -1.

Constraints:

1 <= target.length <= 5 * 10^4
1 <= words.length == costs.length <= 5 * 10^4
1 <= words[i].length <= target.length
The total sum of words[i].length is less than or equal to 5 * 10^4.
target and words[i] consist only of lowercase English letters.
1 <= costs[i] <= 10^4
'''

from typing import List
from functools import lru_cache

class Solution:
  def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
    root = [None]*27
    n = len(target)
    
    def add(w: str, c: int):
      curr = root
      
      for ch in w:
        idx = ord(ch) - ord('a')
        if curr[idx] is None:
          curr[idx] = [None]*27
          
        curr = curr[idx]
        
      if curr[26] is None:
        curr[26] = c
      else:
        curr[26] = min(curr[26], c)
      
    for w, c in zip(words, costs):
      add(w, c)
      
    # print(root)
    
    @lru_cache(None)
    def dp(start: int):
      if start >= n:
        return 0
      
      curr = root
      cost = -1
      
      for i in range(start, n):
        idx = ord(target[i]) - ord('a')
        if curr[idx] is None:
          break
          
        curr = curr[idx]
        
        # not a matching word
        if curr[26] is None:
          continue
          
        c0 = curr[26]
        c1 = dp(i+1)
        if c1 < 0:
          continue
        
        c2 = c0+c1
        if cost < 0 or c2 < cost:
          cost = c2
      
      return cost
    
    return dp(0)
        