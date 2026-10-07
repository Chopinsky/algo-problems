'''
3877-minimum-removals-to-achieve-target-xor
'''


class Solution:
  def minRemovals(self, nums: list[int], target: int) -> int:
    dp = {0:0}
    nxt = {0:0}

    for v0 in nums:
      for v1, ln in dp.items():
        v2 = v0^v1
        nxt[v2] = max(nxt.get(v2, 0), ln+1)
        nxt[v1] = max(nxt.get(v1, 0), ln)

      dp, nxt = nxt, dp
      nxt.clear()
      nxt[0] = nxt.get(0, 0)
      # print('iter:', v0, dp)
    
    return len(nums)-dp[target] if target in dp else -1
        