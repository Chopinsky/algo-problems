'''
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

Constraints:

1 <= arr.length <= 1000
2 <= arr[i] <= 10^9
All the values of arr are unique.
'''

from typing import List


class Solution:
  def numFactoredBinaryTrees(self, arr: List[int]) -> int:
    counter = {val:1 for val in arr}
    arr.sort()
    mod = 10**9 + 7
    
    for v0 in arr:
      if v0*v0 in counter:
        counter[v0*v0] = (counter[v0*v0] + counter[v0]*counter[v0]) % mod
      
      for v1 in arr:
        if v1 >= v0:
          break
          
        val = v0*v1
        if val not in counter:
          continue
          
        counter[val] = (counter[val] + 2*counter[v0]*counter[v1]) % mod
        
    return sum(counter.values()) % mod
        
        
  def numFactoredBinaryTrees(self, arr: List[int]) -> int:
    mod = 10**9 + 7
    subtree = {}
    arr.sort()
    
    for v0 in arr:
      subtree[v0] = 1
      
      for v1 in arr:
        if v1*v1 >= v0:
          if v1*v1 == v0:
            subtree[v0] += subtree[v1] * subtree[v1]
                             
          break
          
        if v0 % v1 == 0 and v0 // v1 in subtree:
          subtree[v0] += 2 * subtree[v1] * subtree[v0//v1]
      
      subtree[v0] %= mod
    
    return sum(subtree.values()) % mod