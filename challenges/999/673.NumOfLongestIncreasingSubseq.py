'''
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Constraints:

1 <= nums.length <= 2000
-106 <= nums[i] <= 10^6
'''


from typing import List


class Solution:
  def findNumberOfLIS(self, nums: List[int]) -> int:
    ln = {}
    
    for v0 in nums:
      l0 = 1
      c0 = 1
      
      for v1, [l1, c1] in ln.items():
        if v1 >= v0 or 1+l1 < l0:
          continue
          
        if 1+l1 == l0:
          c0 += c1
          continue
          
        l0 = 1+l1
        c0 = c1
        
      # print(v0, (l0, c0), ln)
      
      if (v0 not in ln) or (l0 > ln[v0][0]):
        ln[v0] = [l0, c0]
        continue
        
      if l0 == ln[v0][0]:
        ln[v0][1] += c0
    
    # print('fin:', ln)
    count = 0
    max_ln = 1
    
    for l, c in ln.values():
      # print(l, c, count)
      if l > max_ln:
        max_ln = l
        count = c
        continue
        
      if l == max_ln:
        count += c
    
    return count
        
        
  def findNumberOfLIS(self, nums: List[int]) -> int:
    counter = []
    longest = [0, 0]
    
    for v0 in nums:
      long = 1
      cnt = 1
      
      for v1, l0, c0 in counter:
        if v1 >= v0:
          continue
        
        if l0 + 1 == long:
          cnt += c0
          
        elif l0 + 1 > long:
          long = l0 + 1
          cnt = c0
          
      counter.append((v0, long, cnt))
      
      if long > longest[0]:
        longest[0] = long
        longest[1] = cnt
      elif long == longest[0]:
        # print(v0, long, cnt)
        longest[1] += cnt
        
    # print(counter)
    return longest[1]
  