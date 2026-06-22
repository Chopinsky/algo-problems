'''
3811-Number-of-Alternating-XOR-Partitions
'''

from typing import List
from collections import defaultdict


class Solution:
  def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
    mod = 10**9 + 7
    
    cnt1 = defaultdict(int)  # 上一段是target2结尾（下一段需要target1）
    cnt2 = defaultdict(int)  # 上一段是target1结尾（下一段需要target2）
    cnt2[0] = 1              # 空前缀，等待第一段 target1
    
    ans = 0
    pre = 0

    for val in nums:
      pre ^= val

      a = cnt2[pre^target1]  # 新增一段 XOR=target1
      b = cnt1[pre^target2]  # 新增一段 XOR=target2
      
      ans = (a+b) % mod
      cnt1[pre] = (cnt1[pre]+a) % mod
      cnt2[pre] = (cnt2[pre]+b) % mod

    return ans

  def alternatingXOR0(self, nums: List[int], target1: int, target2: int) -> int:
    mod = 10**9 + 7
    n = len(nums)
    prefix = 0
    state = [0, target1, target1^target2, target2]
    
    dp = [0]*4
    dp[0] = 1
    
    pre_dp = [0]*4
    pre_dp[0] = 1

    for i in range(n):
      prefix ^= nums[i]
      if i == n-1:
        break

      for j in range(4):
        if prefix == state[j]:
          dp[j] = (dp[j] + pre_dp[(j+3)%4]) % mod

      pre_dp = dp.copy()

    total = 0
    for j in range(4):
      if prefix == state[j]:
        total = (total + pre_dp[(j+3)%4]) % mod

    return total
    


        