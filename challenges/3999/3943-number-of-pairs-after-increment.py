'''
3943-number-of-pairs-after-increment
'''

from typing import List
from collections import defaultdict


class Solution:
  def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
    freq: dict[int, int] = defaultdict(int)
    for val in nums2:
      freq[val] += 1

    offset = 0
    n2 = len(nums2)
    ans = []

    for query in queries:
      # type 2, count pairs
      if len(query) == 2:
        cnt = 0
        for val in nums1:
          # the targeting nums2 value is:
          #   target = nums1_val + (nums2_val + comp_range_offset)
          cnt += freq[query[1] - val - offset]

        ans.append(cnt)
        continue

      # type 1, update range
      _, l, r, val = query

      if r-l > n2//2:
        # reduce the complementary range but raise 
        # the overall offset
        offset += val
        for i in range(l):
          freq[nums2[i]] -= 1
          nums2[i] -= val
          freq[nums2[i]] += 1

        for i in range(r+1, n2):
          freq[nums2[i]] -= 1
          nums2[i] -= val
          freq[nums2[i]] += 1

      else:
        # direct range update
        for i in range(l, r+1):
          freq[nums2[i]] -= 1
          nums2[i] += val
          freq[nums2[i]] += 1

    return ans
        