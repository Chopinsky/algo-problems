'''
3277. Maximum XOR Score Subarray Queries

You are given an array nums of n integers, and a 2D integer array queries of size q, where queries[i] = [li, ri].

For each query, you must find the maximum XOR score of any subarray of nums[li..ri].

The XOR score of an array a is found by repeatedly applying the following operations on a so that only one element remains, that is the score:

Simultaneously replace a[i] with a[i] XOR a[i + 1] for all indices i except the last one.
Remove the last element of a.
Return an array answer of size q where answer[i] is the answer to query i.

Example 1:

Input: nums = [2,8,4,32,16,1], queries = [[0,2],[1,4],[0,5]]

Output: [12,60,60]

Explanation:

In the first query, nums[0..2] has 6 subarrays [2], [8], [4], [2, 8], [8, 4], and [2, 8, 4] each with a respective XOR score of 2, 8, 4, 10, 12, and 6. The answer for the query is 12, the largest of all XOR scores.

In the second query, the subarray of nums[1..4] with the largest XOR score is nums[1..4] with a score of 60.

In the third query, the subarray of nums[0..5] with the largest XOR score is nums[1..4] with a score of 60.

Example 2:

Input: nums = [0,7,3,2,8,5,1], queries = [[0,3],[1,5],[2,4],[2,6],[5,6]]

Output: [7,14,11,14,5]

Explanation:

Index	nums[li..ri]	Maximum XOR Score Subarray	Maximum Subarray XOR Score
0	[0, 7, 3, 2]	[7]	7
1	[7, 3, 2, 8, 5]	[7, 3, 2, 8]	14
2	[3, 2, 8]	[3, 2, 8]	11
3	[3, 2, 8, 5, 1]	[2, 8, 5, 1]	14
4	[5, 1]	[5]	5

Constraints:

1 <= n == nums.length <= 2000
0 <= nums[i] <= 2^31 - 1
1 <= q == queries.length <= 10^5
queries[i].length == 2
queries[i] = [li, ri]
0 <= li <= ri <= n - 1
'''

from typing import List

class Solution:
  '''
  the trick is to maintain a list of xor sums for the intervals: subarr=[[0, j], [1, j], ..., [j, j]], then
  when we move from j to j+1, we append `nums[j]` to this list, then recursively updating the tail
  value with: subarr[i] = subarr[i]^subarr[i+1], then we can update the segment query tree for this new
  range [i, j]; note that another optimization to avoid LTE is that XOR subarray almost always decrease
  the values, so we only need to update the tree if we have a better value becoming available for the
  starting index of i;
  '''
  def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums)
    lq = len(queries)
    q = sorted([(queries[i][0], queries[i][1], i) for i in range(lq)], key=lambda x: (x[1], x[0], x[2]))
    nodes = [[] for _ in range(4*n)]
    
    def make(idx: int, l: int, r: int):
      lc = 2*idx+1
      rc = 2*idx+2
      nodes[idx] = [l, r, 0, lc, rc]
    
    make(0, 0, n-1)
    subarr = []
    best = [0]*n
    
    def update(idx: int, i: int, val: int):
      l, r, cval, lc, rc = nodes[idx]
      nodes[idx][2] = max(cval, val)
      
      if l == r:
        return
      
      mid = (l+r)//2
      if i <= mid:
        if lc < len(nodes) and len(nodes[lc]) == 0:
          make(lc, l, mid) 
        
        child = lc
        
      else:
        if rc < len(nodes) and len(nodes[rc]) == 0:
          make(rc, mid+1, r)
        
        child = rc
        
      update(child, i, val)
      
    def query(idx: int, i: int) -> int:
      if idx >= len(nodes) or len(nodes[idx]) == 0:
        return 0
      
      l, r, val, lc, rc = nodes[idx]
      if i > r:
        return 0
      
      if i <= l or l == r:
        return val
      
      rval = query(rc, i)
      lval = 0
      mid = (l+r)//2
      
      if i <= mid:
        lval = query(lc, i)
          
      return max(rval, lval)
    
    def add(i: int):
      if i >= n or i+1 <= len(subarr):
        return
    
      subarr.append(nums[i])
      update(0, i, nums[i])
      best[i] = nums[i]
      j = len(subarr)-2
      
      while j >= 0:
        subarr[j] ^= subarr[j+1]
        if subarr[j] > best[j]:
          update(0, j, subarr[j])
          best[j] = subarr[j]
          
        j -= 1
        
      # print('added:', (i, nums[i]), subarr)
        
    ans = [0]*lq
    for l, r, idx in q:
      ptr = len(subarr)
      while ptr <= r:
        add(ptr)
        ptr += 1
        
      # print('q:', (l, r, idx), subarr)
      ans[idx] = max(ans[idx], query(0, l))
    
    return ans
        