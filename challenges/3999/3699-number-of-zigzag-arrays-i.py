'''
3699-number-of-zigzag-arrays-i
'''


class Solution:
  def zigZagArrays(self, n: int, l: int, r: int) -> int:
    r -= l
    dp = [1] * (r+1)
    mod = 10**9 + 7
    
    for i in range(1, n):
      prefix = 0 

      if i&1:
        # odd steps, goes higher
        for j in range(r+1):
          nxt_prefix = prefix + dp[j]
          dp[j] = prefix
          prefix = nxt_prefix % mod

      else:
        # even steps, goes lower
        for j in range(r, -1, -1):
          nxt_prefix = prefix + dp[j]
          dp[j] = prefix
          prefix = nxt_prefix % mod

    # adding alternate direction
    return (2*sum(dp)) % mod

        