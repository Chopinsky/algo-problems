'''
You are given two integer arrays nums1 and nums2 of lengths m and n respectively. nums1 and nums2 represent the digits of two numbers. You are also given an integer k.

Create the maximum number of length k <= m + n from digits of the two numbers. The relative order of the digits from the same array must be preserved.

Return an array of the k digits representing the answer.

Example 1:

Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
Output: [9,8,6,5,3]
Example 2:

Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
Output: [6,7,6,0,4]
Example 3:

Input: nums1 = [3,9], nums2 = [8,9], k = 3
Output: [9,8,9]

Constraints:

m == nums1.length
n == nums2.length
1 <= m, n <= 500
0 <= nums1[i], nums2[i] <= 9
1 <= k <= m + n
'''


from typing import List


class Solution:
  def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
    # build the monotonic stack in greedy mode: make it monotonically
    # decrease, until the point that we need to feel the array with the
    # rest of the numers
    def build_stack(nums: List[int], count: int) -> List[int]:
      stack = []
      drop = len(nums) - count
      
      for val in nums:
        while drop and stack and val > stack[-1]:
          stack.pop()
          drop -= 1
          
        stack.append(val)
      
      return stack[:count]
    
    # merge the 2 arrays, with the larger subseq will 
    # win the next spot
    def merge(a: List, b: List) -> List:
      i, j = 0, 0
      res = []
      
      while i < len(a) or j < len(b):
        if i >= len(a):
          res.extend(b[j:])
          break
          
        elif j >= len(b):
          res.extend(a[i:])
          break
          
        if (a[i] > b[j]) or (a[i] == b[j] and a[i:] > b[j:]):
          res.append(a[i])
          i += 1
        else:
          res.append(b[j])
          j += 1
      
      return res
    
    best = (nums1+nums2)[:k]
    start = max(0, k-len(nums2))
    end = min(k, len(nums1))+1
    
    # try all valid lengths: 
    for ln0 in range(start, end):
      a = build_stack(nums1, ln0)
      b = build_stack(nums2, k-ln0)
      c = merge(a, b)
      # print((a, ln0), (b, k-ln0), c, best)

      if c > best:
        best = c
    
    return best
  