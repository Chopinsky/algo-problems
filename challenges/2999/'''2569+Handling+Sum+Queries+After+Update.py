'''
2569. Handling Sum Queries After Update

You are given two 0-indexed arrays nums1 and nums2 and a 2D array queries of queries. There are three types of queries:

For a query of type 1, queries[i] = [1, l, r]. Flip the values from 0 to 1 and from 1 to 0 in nums1 from index l to index r. Both l and r are 0-indexed.
For a query of type 2, queries[i] = [2, p, 0]. For every index 0 <= i < n, set nums2[i] = nums2[i] + nums1[i] * p.
For a query of type 3, queries[i] = [3, 0, 0]. Find the sum of the elements in nums2.
Return an array containing all the answers to the third type queries.

Example 1:

Input: nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
Output: [3]
Explanation: After the first query nums1 becomes [1,1,1]. After the second query, nums2 becomes [1,1,1], so the answer to the third query is 3. Thus, [3] is returned.
Example 2:

Input: nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
Output: [5]
Explanation: After the first query, nums2 remains [5], so the answer to the second query is 5. Thus, [5] is returned.

Constraints:

1 <= nums1.length,nums2.length <= 10^5
nums1.length = nums2.length
1 <= queries.length <= 10^5
queries[i].length = 3
0 <= l <= r <= nums1.length - 1
0 <= p <= 10^6
0 <= nums1[i] <= 1
0 <= nums2[i] <= 10^9
'''

from typing import List


class SegTree:
  def __init__(self, nums):
    self.n = len(nums)
    level = 1
    l, r = 0, self.n-1

    while l < r:
      m = (l + r) // 2
      l = m+1
      level += 1
    
    self.size = 1 << (level+1)
    # print('tree size:', self.size)
    
    self.count = [0] * self.size
    self.flag = [False] * self.size
    
    def add(idx, sl, sr, pos):
      self.count[idx] += 1
      if sl == sr:
        return
      
      mid = (sl + sr) // 2
      if pos <= mid:
        add(2*idx, sl, mid, pos)
      else:
        add(2*idx+1, mid+1, sr, pos)
      
    for pos, val in enumerate(nums):
      if val == 1:
        add(1, 0, self.n-1, pos)
        
    # print('seg tree counter:', self.count)
  
  
  def total_ones(self):
    return self.count[1]
  
  
  def lazy_propag(self, idx, sl, sr):
    """
    `lazy_propag` will propagate previous flips to 
    the children segments accordingly: update the 
    `1` count, and mark the affected children as
    candidates for future lazy propagations
    """

    # no need to propagate from this node (either not
    # fliped before, or this is leaf)
    if not self.flag[idx] or sl == sr:
      return
    
    # revert the flag
    self.flag[idx] = False
    mid = (sl + sr) // 2
    
    # update left segment: [sl, mid]
    ldx = 2*idx
    if ldx < self.size:
      self.count[ldx] = (mid-sl+1) - self.count[ldx]
      self.flag[ldx] = not self.flag[ldx]
    
    # update right segment: [mid+1, sr]
    rdx = 2*idx + 1
    if rdx < self.size:
      self.count[rdx] = (sr-mid) - self.count[rdx]
      self.flag[rdx] = not self.flag[rdx]
    
  
  def flip(self, l, r):
    """
    `update` is the helper function that will look to 
    flip the segment based on if it's been updated before
    """
    def update(idx, sl, sr):
      # out of bound
      if sr < l or sl > r or idx >= self.size:
        return
      
      # full segment flip, mark it and we'd need
      # lazy propagation later on
      if l <= sl <= sr <= r:
        self.count[idx] = (sr-sl+1) - self.count[idx]
        self.flag[idx] = not self.flag[idx]
        return
      
      # partial segment flip, update each part accordingly
      mid = (sl + sr) // 2
      ldx = 2*idx
      rdx = 2*idx+1
      
      # the sub-segments beflow this node has not been
      # updated yet, do lazy propagation now
      if self.flag[idx]:
        self.lazy_propag(idx, sl, sr)
        self.flag[idx] = False
        
      # update left segment
      if ldx < self.size:
        update(ldx, sl, mid)
        
      # update right segment
      if rdx < self.size:
        update(rdx, mid+1, sr)
      
      # aggregate results after flips
      self.count[idx] = (self.count[ldx] if ldx < self.size else 0) + (self.count[rdx] if rdx < self.size else 0)
    
    update(1, 0, self.n-1)
  

class Solution:
  '''
  need to implement a customized segment tree that won't propagate flips to every
  node if the left/right sub-segment is not affected
  '''
  def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
    tree = SegTree(nums1)
    ans = []
    curr_sum = sum(nums2)
    
    for t, v0, v1 in queries:
      if t == 3:
        ans.append(curr_sum)
        continue
        
      if t == 2:
        curr_sum += v0 * tree.total_ones()
        continue
        
      tree.flip(v0, v1)
    
    return ans
        