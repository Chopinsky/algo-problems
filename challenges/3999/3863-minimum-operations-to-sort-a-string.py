'''
3863-minimum-operations-to-sort-a-string
'''


class Solution:
  def minOperations(self, s: str) -> int:
    arr = [ord(ch)-ord('a') for ch in s]
    n = len(arr)

    if n <= 1 or all(val == arr[0] for val in arr) or all(arr[i] >= arr[i-1] for i in range(1, n)):
      return 0

    if n <= 2:
      return -1 if arr[0] > arr[1] else 0

    hi = max(arr)
    hc = arr.count(hi)
    lo = min(arr)
    lc = arr.count(lo)
    # print('init:', arr, (lo, hi))

    if arr[0] == hi and arr[-1] == lo:
      return 3 if lc == 1 and hc == 1 else 2

    if arr[0] == lo or arr[-1] == hi:
      return 1

    return 2
        