'''
2542. Maximum Subsequence Score

You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

Example 1:

Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation: 
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.
Example 2:

Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation: 
Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.

Constraints:

n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[j] <= 10^5
1 <= k <= n
'''

from typing import List
from heapq import heapify, heappushpop


class Solution:
  '''
  maintain the max-heap for sum(nums1[...]), then keep adding elements into
  nums1[...] and pop out smaller values from the top-k array
  '''
  def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
    if not nums1 or not nums2:
      return 0

    pairs = [(a, b) for a, b in zip(nums1, nums2)]
    pairs.sort(key=lambda x: -x[1])
    print(pairs)
    
    topK = [x[0] for x in pairs[:k]]
    heapify(topK)
    topKSum = sum(topK)

    res = pairs[k-1][1] * topKSum
    
    for i in range(k, len(pairs)):
      smallest = heappushpop(topK, pairs[i][0])
      topKSum += pairs[i][0] - smallest
      res = max(res, topKSum * pairs[i][1])

    return res
  

  def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
    if k == 1:
      return max(v0*v1 for v0, v1 in zip(nums1, nums2))
    
    n = len(nums1)
    if k == n:
      return sum(nums1) * min(nums2)
    
    floor = sorted((val, idx) for idx, val in enumerate(nums2))
    src = sorted((val, idx) for idx, val in enumerate(nums1))
    
    # print(floor, src)
    sums = nums1[floor[0][1]]
    used = set([floor[0][1]])
    
    while len(used) < k:
      val, idx = src.pop()
      if idx in used:
        continue
        
      sums += val 
      used.add(idx)
    
    score = sums * floor[0][0]
    # print(score, sums, floor[0][0], used)
    
    for i in range(1, n):
      _, j0 = floor[i-1]
      sums -= nums1[j0]

      floor_val, j1 = floor[i]
      if j1 in used:
        # the new floor index already in the subseq, add
        # another large number's index instead
        while src and src[-1][1] in used:
          src.pop()
      
        if not src:
          break
          
        val_add, j1 = src.pop()
        
      else:
        # add the floor index to the subseq
        val_add = nums1[j1]

      sums += val_add
      used.add(j1)
        
      # print('pop:', nums1[j], sums*v2)
      score = max(score, sums * floor_val)
      
    return score
    