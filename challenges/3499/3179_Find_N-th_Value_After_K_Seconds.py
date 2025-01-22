'''
3179. Find the N-th Value After K Seconds
'''


class Solution:
  def valueAfterKSeconds(self, n: int, k: int) -> int:
    mod = 10**9+7
    arr = [1]*n

    while k > 0:
      prefix = arr[0]
      for i in range(1, n):
        prefix = (prefix + arr[i]) % mod
        arr[i] = prefix

      k -= 1

    return arr[-1]
        