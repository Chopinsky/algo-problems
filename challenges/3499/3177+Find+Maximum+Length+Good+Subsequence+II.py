'''
3177. Find the Maximum Length of a Good Subsequence II

You are given an integer array nums and a non-negative integer k. A sequence of integers seq is called good if there are at most k indices i in the range [0, seq.length - 2] such that seq[i] != seq[i + 1].

Return the maximum possible length of a good subsequence of nums.

Example 1:

Input: nums = [1,2,1,1,3], k = 2

Output: 4

Explanation:

The maximum length subsequence is [1,2,1,1,3].

Example 2:

Input: nums = [1,2,3,4,5,1], k = 0

Output: 2

Explanation:

The maximum length subsequence is [1,2,3,4,5,1].

Constraints:

1 <= nums.length <= 5 * 10^3
1 <= nums[i] <= 10^9
0 <= k <= min(50, nums.length)
'''

from typing import List
from collections import Counter

class Solution:
  '''
  given the next value to add, the max length of a seq can be determined by a tuple state: (end_val, rem_k, seq_len),
  where `end_val` represents the last number in the sequence with length of `seq_len` after having `k-rem_k` pairs not
  the same, and we can store these information in a counter array of length `k`, which is at most 50 in size;

  next, for a given sequence, if the `end_val` is the same as the value to add, then `rem_k` is unchanged, just 
  increment the `seq_len` by 1; otherwise, the sequence becomes (val, rem_k-1, seq_len+1), and rem_k-1 must be greater
  than or equal to 0; and the goal of the problem is to find the longest such sequences, aka `max(seq_len)` for any
  possible sequences built this way;

  the key to avoid TLE, is that for each `rem_k`, keep the top 2 sequences' lengths, as we can use these 2 to determine
  the maximum-length-sequences if the sequence ending pair is not the same number; if the ending pair is the same for
  one of the top 2 sequences, just use the other one for `rem_k-1` state.

  Time complexity is O(k*n), and space complexity is also O(k*n)
  '''
  def maximumLength(self, nums: List[int], k: int) -> int:
    if k == 0:
      c = Counter(nums)
      return max(c.values())
    
    ks = [{} for _ in range(k+1)]
    top = [[(-1, 0), (-1, 0)] for _ in range(k+1)]
    long = 1
    # print(ks)
    
    def update_top(i: int, val: int):
      arr = top[i]
      ln = ks[i][val]
      
      if val == arr[0][0]:
        arr[0] = (val, ln)

      elif val == arr[1][0]:
        arr[1] = (val, ln)
        if arr[1][1] > arr[0][1]:
          arr[0], arr[1] = arr[1], arr[0]

      elif ln > arr[1][1]:
        arr.append((val, ln))
        arr.sort(key=lambda x: -x[1])
        arr.pop()
        # print('update top:', (val, ln), top[i])
    
    def update(val: int):
      ln = 0
      
      for i in range(k+1):
        seq = ks[i]

        if i == 0:
          if val in seq:
            seq[val] += 1
            ln = max(ln, seq[val])
            update_top(i, val)
          
          continue

        l0 = 0
        seq_top = top[i]

        if val != seq_top[0][0] and seq_top[0][0] > 0:
          l0 = max(l0, seq_top[0][1])
        elif val != seq_top[1][0] and seq_top[1][0] > 0:
          l0 = max(l0, seq_top[1][1])
          
        if l0 > 0:
          ks[i-1][val] = max(ks[i-1].get(val, 0), l0+1)
          ln = max(ln, ks[i-1][val])
          update_top(i-1, val)
        
        if val in ks[i] or i == k:
          seq[val] = seq.get(val, 0) + 1
          ln = max(ln, seq[val])
          update_top(i, val)
        
      return ln
    
    for val in nums:
      long = max(long, update(val))
      # print(val, ks)
      
    return long
        