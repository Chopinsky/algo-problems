'''
3542-minimum-operations-to-convert-all-elements-to-zero
'''

from collections import defaultdict
from typing import List


class Solution:
  def minOperations(self, nums: List[int]) -> int:
    stack = [0]
    ans = 0 

    for num in nums:
      while num < stack[-1]:
        stack.pop()
        ans += 1
      
      if num != stack[-1]:
        stack.append(num)
    
    # exclude number 0 in the stack
    return ans + len(stack) - 1

  def minOperations0(self, nums: List[int]) -> int:
    n = len(nums)
    used = [0] * (n+1)
    ops = 0

    def update(idx: int):
      if idx == 0:
        used[idx] += 1
        return

      while idx < len(used):
        used[idx] += 1
        idx += idx & -idx

    def query(idx: int) -> int:
      if idx == 0:
        return used[idx]

      s = used[0]
      while idx > 0:
        s += used[idx]
        idx -= idx & -idx

      return s

    vals = defaultdict(list)
    for i in range(n):
      vals[nums[i]].append(i)

    for val in sorted(vals):
      # print('top:', val, ops)

      # first val must be eliminated
      cand = vals[val]
      prev = cand[0]
      if val > 0:
        ops += 1

      for idx in cand[1:]:
        cnt = query(idx) - query(prev)
        # print('iter:', val, (prev, idx), cnt)
        prev = idx

        # contains 0 in-between, must start
        # a nuew subarray
        if cnt > 0 and val > 0:
          ops += 1

      for idx in cand:
        update(idx)

    return ops
        