'''
A sequence x1, x2, ..., xn is Fibonacci-like if:

n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

 

Example 1:

Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:

Input: arr = [1,3,7,11,12,14,18]
Output: 3
Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
 

Constraints:

3 <= arr.length <= 1000
1 <= arr[i] < arr[i + 1] <= 10^9
'''


from typing import List
from collections import defaultdict


class Solution:
  def lenLongestFibSubseq(self, arr: List[int]) -> int:
    n = len(arr)
    lookup = {}
    for val in arr:
      lookup[val] = i

    chain_len = defaultdict(lambda: 2)
    max_len = 2

    for i in range(n):
      a = arr[i]
      for j in range(i+1, n):
        b = arr[j]
        c = a + b
        if c not in lookup:
          continue
          
        k = lookup[c]
        chain_len[(j, k)] = chain_len[(i, j)] + 1
        max_len = max(max_len, chain_len[(j, k)])
          
    return max_len if max_len != 2 else 0
      
      
  def lenLongestFibSubseq0(self, arr: List[int]) -> int:
    n = len(arr)
    vals = set(arr)
    cand = defaultdict(list)
    seen = set()
    longest = 0
    
    for i in range(0, len(arr)):
      seen.clear()
      chains = cand.pop(arr[i], [])
      
      for j, ln in chains:
        seen.add(j)
        tgt = arr[i]+arr[j]
        cand[tgt].append((i, ln+1))
        longest = max(longest, ln+1)
        
      if n-i+1 <= longest:
        continue
        # pass

      for j in range(i):
        if j in seen:
          continue

        tgt = arr[i] + arr[j]
        if tgt in vals:
          cand[tgt].append((i, 2))
    
    return longest
      