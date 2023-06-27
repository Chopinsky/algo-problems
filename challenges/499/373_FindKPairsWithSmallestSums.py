'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
 

Constraints:

1 <= nums1.length, nums2.length <= 10^5
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 10^4
'''


from typing import List
from heapq import heappop, heappush


class Solution:
  def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    ans = []
    n1, n2 = len(nums1), len(nums2)
    stack = sorted([(nums1[i]+nums2[0], i, 0) for i in range(n1)])
    idx = [1]*n1
    
    while len(ans) < k and stack:
      _, i, j = heappop(stack)
      ans.append((nums1[i], nums2[j]))
      # print('add', (i, j), (nums1[i], nums2[j]))
      
      if idx[i] < n2:
        heappush(stack, (nums1[i]+nums2[idx[i]], i, idx[i]))
        idx[i] += 1
        
      # print(stack)
      
    return ans
    
    
  def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    m, n = len(nums1), len(nums2)
    if m == 1:
      return [[nums1[0], nums2[j]] for j in range(min(n, k))]
    
    if n == 1:
      return [[nums1[i], nums2[0]] for i in range(min(m, k))]
    
    ans = []
    heap = [(nums1[0]+nums2[0], 0, 0)]
    seen = set([(0, 0)])
    
    while len(ans) < k and heap:
      # print(ans, heap)
      _, i, j = heappop(heap)
      ans.append([nums1[i], nums2[j]])
      
      if len(ans)+len(heap) < 2*k:
        if j < n-1 and (i, j+1) not in seen:
          heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
          seen.add((i, j+1))
          
        if i < m-1 and (i+1, j) not in seen:
          heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
          seen.add((i+1, j))
      
    return ans
  