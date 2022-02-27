'''
You are given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
Example 2:

Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
Example 3:

Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 1000
1 <= target <= 10^8
'''


from typing import List
import math


class Solution:
  def minSumOfLengths(self, arr: List[int], target: int) -> int:
    prefix = {0:-1}
    cand = []
    idx = 0
    
    psum = 0
    short = math.inf
    ans = -1
    
    for i, val in enumerate(arr):
      psum += val
      
      # not a matching yet or won't find a 
      # subarray whose sum equals target
      if psum < target or psum-target not in prefix:
        prefix[psum] = i
        continue
        
      j = prefix[psum-target]
      while idx < len(cand) and cand[idx][0] <= j:
        short = min(short, cand[idx][1])
        idx += 1
      
      if short < math.inf:
        res = i-j+short 
        ans = res if ans < 0 else min(ans, res)
      
      prefix[psum] = i
      cand.append((i, i-j))
      
    return ans
  