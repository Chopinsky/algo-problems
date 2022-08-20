'''
2382. Maximum Segment Sum After Removals

You are given two 0-indexed integer arrays nums and removeQueries, both of length n. For the ith query, the element in nums at the index removeQueries[i] is removed, splitting nums into different segments.

A segment is a contiguous sequence of positive integers in nums. A segment sum is the sum of every element in a segment.

Return an integer array answer, of length n, where answer[i] is the maximum segment sum after applying the ith removal.

Note: The same index will not be removed more than once.

Example 1:

Input: nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]
Output: [14,7,2,2,0]
Explanation: Using 0 to indicate a removed element, the answer is as follows:
Query 1: Remove the 0th element, nums becomes [0,2,5,6,1] and the maximum segment sum is 14 for segment [2,5,6,1].
Query 2: Remove the 3rd element, nums becomes [0,2,5,0,1] and the maximum segment sum is 7 for segment [2,5].
Query 3: Remove the 2nd element, nums becomes [0,2,0,0,1] and the maximum segment sum is 2 for segment [2]. 
Query 4: Remove the 4th element, nums becomes [0,2,0,0,0] and the maximum segment sum is 2 for segment [2]. 
Query 5: Remove the 1st element, nums becomes [0,0,0,0,0] and the maximum segment sum is 0, since there are no segments.
Finally, we return [14,7,2,2,0].
Example 2:

Input: nums = [3,2,11,1], removeQueries = [3,2,1,0]
Output: [16,5,3,0]
Explanation: Using 0 to indicate a removed element, the answer is as follows:
Query 1: Remove the 3rd element, nums becomes [3,2,11,0] and the maximum segment sum is 16 for segment [3,2,11].
Query 2: Remove the 2nd element, nums becomes [3,2,0,0] and the maximum segment sum is 5 for segment [3,2].
Query 3: Remove the 1st element, nums becomes [3,0,0,0] and the maximum segment sum is 3 for segment [3].
Query 4: Remove the 0th element, nums becomes [0,0,0,0] and the maximum segment sum is 0, since there are no segments.
Finally, we return [16,5,3,0].

Constraints:

n == nums.length == removeQueries.length
1 <= n <= 10^5
1 <= nums[i] <= 10^9
0 <= removeQueries[i] < n
All the values of removeQueries are unique.
'''

from typing import List
from heapq import heappush, heappop
from bisect import insort, bisect_left, bisect_right


class Solution:
  '''
  essentially the problem asks for the largest segment sums if we *add* numbers at the
  indexs in the query back from tail to head; so we can use union-find algorithm for 
  this job: after adding a number from index-i back into the array, union this number
  with the segment that contains index-(i-1), and the segment that contains index-(i+1),
  and we should also update the segment sums of the resulting segment from the unions;
  and we can update the max segment sum in the process, which is the anser to (the next) query.
  '''
  def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
    n = len(nums)
    arr = [i for i in range(n)]
    ans = [0] * n
    seen = set()
    curr_max = 0
    
    def find(x: int) -> int:
      while arr[x] != x:
        x = arr[x]
        
      return x
    
    def union(x: int, y: int) -> int:
      xx, yy = find(x), find(y)
      # print('union', (x, xx), (y, yy))
      # print('before union:', nums)
      
      if xx <= yy:
        arr[yy] = xx
        nums[xx] += nums[yy]
        
      else:
        arr[xx] = yy
        nums[yy] += nums[xx]
        
      return max(nums[xx], nums[yy])
    
    curr_max = 0
    for i in range(n-1, -1, -1):
      q = removeQueries[i]
      ans[i] = curr_max
      curr_max = max(curr_max, nums[q])
      
      if q-1 in seen:
        curr_max = max(curr_max, union(q, q-1))
        
      if q+1 in seen:
        curr_max = max(curr_max, union(q, q+1))
      
      seen.add(q)
      
    return ans
  
  
  def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
    n = len(nums)
    prefix = [val for val in nums]
    for i in range(1, n):
      prefix[i] += prefix[i-1]
      
    ans = []
    heap = [(-prefix[-1], 0, n-1)]
    root = []
    
    for q in removeQueries:
      insort(root, q)
      
      if not heap:
        ans.append(0)
        continue
      
      while heap:
        top, l, r = heappop(heap)
        curr = l
        
        i = bisect_left(root, l)
        j = bisect_right(root, r)
        if i >= len(root) or i >= j:
          heappush(heap, (top, l, r))
          break
          
        # print('cut:', q, top, l, r, root[i:j])
        for k in root[i:j]:
          if k == curr:
            curr += 1
            continue
            
          if k > r:
            break
            
          seg_sum = prefix[k-1] - (prefix[curr-1] if curr > 0 else 0)
          heappush(heap, (-seg_sum, curr, k-1))
          curr = k+1
        
        if curr <= r:
          seg_sum = prefix[r] - (prefix[curr-1] if curr > 0 else 0)
          heappush(heap, (-seg_sum, curr, r))
          
      # print('post', heap)
      if heap:
        ans.append(-heap[0][0])
      else:
        ans.append(0)
    
    return ans
    
  ''' ... segment tree, TLE, but the solution itself is correct ...
  def maximumSegmentSum0(self, nums: List[int], removeQueries: List[int]) -> List[int]:
    n = len(nums)
    prefix = [val for val in nums]
    for i in range(1, n):
      prefix[i] += prefix[i-1]
      
    ans = []
    root = [prefix[-1], 0, n-1, None, None]
    
    def find0(src, k):
      if not src:
        return False, 0
      
      max_sum, i, j, left, right = src
      if k < i or k > j:
        return False, max_sum
      
      if not left and not right:
        if i == j and k == i:
          return True, 0
        
        if k == i:
          src[1] += 1
          src[0] -= nums[k]
          return False, src[0]
        
        if k == j:
          src[2] -= 1
          src[0] -= nums[k]
          return False, src[0]
        
        ls = prefix[k-1] - (prefix[i-1] if i > 0 else 0)
        src[3] = [ls, i, k-1, None, None]
        
        rs = prefix[j] - prefix[k]
        src[4] = [rs, k+1, j, None, None]
        src[0] = max(ls, rs)
        
      else:
        lr, ls = find(left, k)
        rr, rs = find(right, k)
        src[0] = max(ls, rs)
        
        if lr:
          src[3] = None
          
        if rr:
          src[4] = None
        
        if not src[3] and not src[4]:
          return True, 0
        
      return False, src[0]
        
    for q in removeQueries:
      if not root:
        ans.append(0)
        
      else:
        removed, max_seg = find(root, q)
        if removed:
          root = None
          
        ans.append(max_seg)
    
    return ans
  '''