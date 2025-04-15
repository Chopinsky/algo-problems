'''
You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].

A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.

Return the total number of good triplets.

Example 1:

Input: nums1 = [2,0,1,3], nums2 = [0,1,2,3]
Output: 1
Explanation: 
There are 4 triplets (x,y,z) such that pos1x < pos1y < pos1z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3). 
Out of those triplets, only the triplet (0,1,3) satisfies pos2x < pos2y < pos2z. Hence, there is only 1 good triplet.
Example 2:

Input: nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
Output: 4
Explanation: The 4 good triplets are (4,0,3), (4,0,2), (4,1,3), and (4,1,2).
 

Constraints:

n == nums1.length == nums2.length
3 <= n <= 10^5
0 <= nums1[i], nums2[i] <= n - 1
nums1 and nums2 are permutations of [0, 1, ..., n - 1].
'''

from typing import List


class Solution:
  def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    pv1 = {val:i for i, val in enumerate(nums1)}

    def query(f, idx):
      c = f[0]
      while idx > 0:
        c += f[idx]
        idx -= (idx & -idx)

      return c

    def fill(f, idx):
      if idx == 0:
        f[idx] += 1
        return

      while idx < n+1:
        f[idx] += 1
        idx += (idx & -idx)

    before = [0]*n
    after = [0]*n
    fw = [0]*(n+1)

    for val in nums2:
      before[val] = query(fw, pv1[val])
      fill(fw, pv1[val])

    fw = [0]*(n+1)
    for val in nums2[::-1]:
      after[val] = query(fw, n-pv1[val])
      fill(fw, n-pv1[val])

    # print('init:', before, after)
    
    return sum(before[i]*after[i] for i in range(n))

  def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    pos = {v:i for i, v in enumerate(nums1)}
    n2 = [pos[v] for v in nums2]
    cnt = 0
    pairs = [0] * n
    fenwick = [0] * (n+1)
    
    def update(idx: int):
      idx += 1
      while idx < n+1:
        fenwick[idx] += 1
        idx += (idx & -idx)
        
    def query(idx: int):
      total = 0
      idx += 1
      if idx > n:
        idx = n
      
      while idx > 0:
        total += fenwick[idx]
        idx -= (idx & -idx)
        
      return total
    
    for val in n2:
      pairs[val] = query(val)
      update(val)
    
    # print(n2, pairs)
    
    def merge_sort(src: List[int]) -> List[int]:
      nonlocal cnt
      
      ln = len(src)
      if ln <= 1:
        return src
      
      res = []
      l, r = merge_sort(src[:ln//2]), merge_sort(src[ln//2:])
      # print('merge', src, l, r)
      
      l_size, r_size = ln//2, ln-ln//2
      i, j = 0, 0
      
      while i < l_size or j < r_size:
        if i >= l_size:
          res += r[j:]
          break
          
        if j >= r_size:
          res += l[i:]
          break
          
        if r[j] <= l[i]:
          res.append(r[j])
          j += 1
          continue
          
        # found good triplets
        cnt += pairs[l[i]] * (r_size - j)
        res.append(l[i])
        i += 1
        
      return res
    
    arr = merge_sort(n2)
    # print(arr)
    
    return cnt
    