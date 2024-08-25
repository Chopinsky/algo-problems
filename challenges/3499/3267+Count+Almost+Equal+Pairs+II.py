'''
3267. Count Almost Equal Pairs II

You are given an array nums consisting of positive integers.

We call two integers x and y almost equal if both integers can become equal after performing the following operation at most twice:

Choose either x or y and swap any two digits within the chosen number.
Return the number of indices i and j in nums where i < j such that nums[i] and nums[j] are almost equal.

Note that it is allowed for an integer to have leading zeros after performing an operation.

Example 1:

Input: nums = [1023,2310,2130,213]

Output: 4

Explanation:

The almost equal pairs of elements are:

1023 and 2310. By swapping the digits 1 and 2, and then the digits 0 and 3 in 1023, you get 2310.
1023 and 213. By swapping the digits 1 and 0, and then the digits 1 and 2 in 1023, you get 0213, which is 213.
2310 and 213. By swapping the digits 2 and 0, and then the digits 3 and 2 in 2310, you get 0213, which is 213.
2310 and 2130. By swapping the digits 3 and 1 in 2310, you get 2130.
Example 2:

Input: nums = [1,10,100]

Output: 3

Explanation:

The almost equal pairs of elements are:

1 and 10. By swapping the digits 1 and 0 in 10, you get 01 which is 1.
1 and 100. By swapping the second 0 with the digit 1 in 100, you get 001, which is 1.
10 and 100. By swapping the first 0 with the digit 1 in 100, you get 010, which is 10.

Constraints:

2 <= nums.length <= 5000
1 <= nums[i] < 10^7
'''

from typing import List
from collections import defaultdict
from itertools import combinations

class Solution:
  def countPairs(self, nums: List[int]) -> int:
    c0 = defaultdict(set)
    c1 = defaultdict(set)
    c2 = defaultdict(set)
    
    def add(res, cand):
      k = 0
      while k < len(cand) and cand[k] == '0':
        k += 1
          
      cand = cand[k:]
      res.add(''.join(cand))
    
    # swap  2 digits in a number
    def s2(d: str):
      n = len(d)
      res = set()
      
      if n <= 1:
        return res
      
      # print('iter-2:', d)
      for index in combinations(range(n), 2):
        cand = list(d)
        i, j = index
        cand[i], cand[j] = cand[j], cand[i]
        add(res, cand)
        
      # print('s2:', res)
      # res.discard(d)
      
      return res
    
    # swap/rotate 3 digits in a number
    def s3(d: str):
      n = len(d)
      res = set()
      
      if n <= 2:
        return res
      
      # get all possibe index of 3 digits
      for index in combinations(range(n), 3):
        cand = list(d)
        for _ in range(2):
          i0, i1, i2 = index
          cand[i0], cand[i1], cand[i2] = cand[i1], cand[i2], cand[i0]
          add(res, cand)
      
      # print('s3:', d, res)
      # res.discard(d)
      
      return res
    
    # swap 2 pairs of 2 digits in a number
    def s4(d: str):
      n = len(d)
      res = set()
      
      if n <= 3:
        return res

      # print('iter-4:', d)
      swaps = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]
      
      # get index of 4 digits and form different 2 pairs
      for index in combinations(range(n), 4):
        # print('pick4:', index)
        for swap in swaps:
          cand = list(d)
          i0 = index[swap[0]]
          j0 = index[swap[1]]
          i1 = index[swap[2]]
          j1 = index[swap[3]]
          cand[i0], cand[j0] = cand[j0], cand[i0]
          cand[i1], cand[j1] = cand[j1], cand[i1]
          add(res, cand)
      
      # print('s4:', d, res)
      # res.discard(d)
      
      return res
    
    def update(val: str, idx: int):
      # 0-0, 0-1, 0-2
      prev = set()
      prev |= c0[val] | c1[val] | c2[val]
            
      # 1-0, 1-1
      swap1 = s2(val)
      for v1 in swap1:
        prev |= (c0[v1] | c1[v1])
        c1[v1].add(idx)
      
      # 2-0
      swap2 = s3(val) | s4(val)
      for v2 in swap2:
        prev |= c0[v2]
        c2[v2].add(idx)
      
      c0[val].add(idx)
      
      return len(prev)
      
    count = 0
    for idx in range(len(nums)):
      count += update(str(nums[idx]), idx)
      
    return count
        