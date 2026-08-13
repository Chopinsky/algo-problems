'''
2215. Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

Constraints:

1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000
'''

from typing import List


class Solution:
  def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
    n = len(s)
    pre = [0] * (4*n)
    suf = [0] * (4*n)
    max_ln = [0] * (4*n)
    left_ch = [""] * (4*n)
    right_ch = [""] * (4*n)

    def push_up(u: int, l: int, r: int):
      mid = (l+r) // 2
      left_ln = mid-l+1
      right_ln = r-mid

      left = 2*u
      right = 2*u + 1
      left_ch[u] = left_ch[left]
      right_ch[u] = right_ch[right]
      
      pre[u] = pre[left]
      if pre[left] == left_ln and right_ch[left] == left_ch[right]:
        pre[u] = pre[left] + pre[right]

      suf[u] = suf[right]
      if suf[right] == right_ln and right_ch[left] == left_ch[right]:
        suf[u] = suf[right] + suf[left]

      max_ln[u] = max(max_ln[left], max_ln[right])
      if right_ch[left] == left_ch[right]:
        max_ln[u] = max(max_ln[u], suf[left]+pre[right])

    def build(u: int, l: int, r: int):
      # leaf
      if l == r:
        pre[u] = 1
        suf[u] = 1
        max_ln[u] = 1
        left_ch[u] = s[l]
        right_ch[u] = s[l]
        return

      mid = (l+r) // 2
      build(2*u, l, mid)
      build(2*u+1, mid+1, r)
      push_up(u, l, r)

    def update(u: int, l: int, r: int, pos: int, ch: str):
      if l == r:
        left_ch[u] = ch
        right_ch[u] = ch
        return

      mid = (l+r) // 2
      if pos <= mid:
        update(2*u, l, mid, pos, ch)
      else:
        update(2*u+1, mid+1, r, pos, ch)

      push_up(u, l, r)

    build(1, 0, n-1)
    # k = len(queryIndices)
    ans = []

    for pos, ch in zip(queryIndices, queryCharacters):
      update(1, 0, n-1, pos, ch)
      ans.append(max_ln[1])

    return ans

  def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    s1, s2 = set(nums1), set(nums2)
    s0 = s1 & s2
    return [list(s1 - s0), list(s2 - s0)]    
    
