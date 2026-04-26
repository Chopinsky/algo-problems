'''
3915-maximum-sum-of-alternating-subsequence-with-distance-at-least-k
'''

import math


class Solution:
  def maxAlternatingSum(self, nums: list[int], k: int) -> int:
    top = 10**5+1
    low = -math.inf

    def update(i: int, v: int, arr: list[int]):
      while i <= top:
        arr[i] = max(arr[i], v)
        i += i & -i

    def query(i: int, arr: list[int]) -> int:
      r = low
      while i > 0:
        r = max(arr[i], r)
        i -= i & -i

      return r

    n = len(nums)
    up = [0]*n              # best sums of the seq previously going up at the index value
    down = [0]*n            # best sums of the seq previously going down at the index value
    prefix = [low]*(top+1)  # prefix, saving values smaller than the indexed value
    suffix = [low]*(top+1)  # reverse-suffix, saving values larger than the indexed value
    ans = low

    for i in range(n):
      if i >= k:
        # nums[i-k] becomes available, update
        # prefix and suffix with the available
        # up/down seq tail values
        v = nums[i-k]
        update(v, down[i-k], prefix)
        update(top+1-v, up[i-k], suffix)

      # find the last valid tail of the seq
      v = nums[i]
      prev_down = query(v-1, prefix) if v-1 > 0 else low
      prev_up = query((top+1)-(v+1), suffix) if (top+1) - (v+1) > 0 else low

      # append v to the valid seq
      up[i] = v + max(0, prev_down)
      down[i] = v + max(0, prev_up)

      ans = max(ans, up[i], down[i])
    
    return ans

  def maxAlternatingSum(self, nums: list[int], k: int) -> int:
    bralvoteni = nums
    n = len(bralvoteni)
    
    # Coordinate compression for the Fenwick Tree (since nums[i] up to 10^5)
    # We need to map values to ranks to handle the "strictly" constraint
    unique_vals = sorted(list(set(bralvoteni)))
    rank = {val: i+1 for i, val in enumerate(unique_vals)}
    m = len(unique_vals)

    # bit_up[rank] stores max dp_up for a value with that rank
    # bit_down[rank] stores max dp_down for a value with that rank
    bit_up = [0] * (m+1)
    bit_down = [0] * (m+1)

    def update(bit: list[int], idx: int, val: int):
      while idx <= m:
        bit[idx] = max(bit[idx], val)
        idx += idx & (-idx)

    def query(bit: list[int], idx: int):
      res = 0
      while idx > 0:
        res = max(res, bit[idx])
        idx -= idx & (-idx)
        
      return res
    
    # To query values strictly GREATER, we use a reversed BIT or m - rank
    bit_up_rev = [0] * (m+1)
    def update_rev(bit: list[int], idx: int, val: int):
      idx = m-idx+1
      while idx <= m:
        bit[idx] = max(bit[idx], val)
        idx += idx & (-idx)
    
    def query_rev(bit: list[int], idx: int) -> int:
      idx = m-idx+1
      res = 0
      while idx > 0:
        res = max(res, bit[idx])
        idx -= idx & (-idx)

      return res

    dp_up = [0] * n
    dp_down = [0] * n
    ans = 0

    for i in range(n):
      curr_val = bralvoteni[i]
      curr_rank = rank[curr_val]
      
      # Step 1: Elements at index i-k just became available
      if i >= k:
        prev_idx = i - k
        update(bit_down, rank[bralvoteni[prev_idx]], dp_down[prev_idx])
        update_rev(bit_up_rev, rank[bralvoteni[prev_idx]], dp_up[prev_idx])
      
      # Step 2: Calculate DP for current index
      # To be an 'up' (peak), we need a 'down' (valley) that is strictly smaller
      max_prev_down = query(bit_down, curr_rank - 1)
      dp_up[i] = curr_val + max_prev_down
      
      # To be a 'down' (valley), we need an 'up' (peak) that is strictly larger
      max_prev_up = query_rev(bit_up_rev, curr_rank + 1)
      dp_down[i] = curr_val + max_prev_up
      
      # A subsequence of length 1 is always valid
      dp_up[i] = max(dp_up[i], curr_val)
      dp_down[i] = max(dp_down[i], curr_val)
      
      ans = max(ans, dp_up[i], dp_down[i])

    return ans