'''
There is a garden withNslots. In each slot, there is a flower. The N flowers 
will bloom one by one in N days. In each day, there will beexactlyone flower 
blooming and it will be in the status of blooming since then.

Given an arrayflowersconsists of number from1toN. Each number in the array 
represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i 
will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers
 in the status of blooming, and also the number of flowers between them is k and 
 these flowers are not blooming.

If there isn't such day, output -1.

Example 1:

Input:

flowers: [1,3,2], k: 1

Output: 2

Explanation:
In the second day, the first and the third flower have become blooming.

Example 2:

Input:

flowers: [1,2,3], k: 1

Output: -1

Note:
The given array will be in the range [1, 20000].
'''


from typing import List
import math


class Solution:
  def k_empty_slots(self, flowers: List[int], k: int) -> int:
    n = len(flowers)
    days = [0] * n

    for i, f in enumerate(flowers):
      days[f-1] = i+1

    left, right = 0, k+1
    ans = math.inf
    idx = 0

    while right < n:
      if idx == right:
        # we haven't encountered a day that flower @ idx blooms 
        # before flowers @ left/right, then [left, right] is the
        # desired range
        ans = min(ans, max(days[left], days[right]))

        # begin with a new search
        left = idx
        right = idx + k + 1

      elif days[idx] < days[left] or days[idx] < days[right]:
        # a flower will bloom before flowers @ left/right, this
        # will invalidate the [left, right] hypopthesis and any
        # range between [left, idx], so start a new search with
        # [idx, idx+k+1]
        left = idx
        right = idx + k + 1

      idx += 1
    
    return -1 if ans == math.inf else ans


  def k_empty_slots0(self, flowers: List[int], k: int) -> int:
    n = max(flowers)
    arr = [0] * (n+1)
    seen = set()

    def update(x: int, val: int):
      while x <= n:
        arr[x] += val
        x += x & -x

    def query(x: int) -> int:
      s = 0
      while x > 0:
        s += arr[x]
        x -= x & -x

      return s

    for i, pos in enumerate(flowers):
      seen.add(pos)
      if i == 0:
        update(pos, 1)
        continue

      base = query(pos)

      if pos-k-1 >= 1:
        lc = query(pos-k-1)
        rc = base

        if lc == rc and pos-k-1 in seen:
          # print('left', i)
          return i+1

      if pos+k+1 <= n:
        lc = base
        rc = query(pos+k+1)

        if lc == rc and pos+k+1 in seen:
          # print('right', i)
          return i+1

      update(pos, 1)

    return -1


s = Solution()
t = [
  [[1,3,2], 1, 2],
  [[1,3,2,6,4,5], 2, 4],
  [[1,2,3], 1, -1],
]

for f, k, ans in t:
  print('\n======\nTest case:', f, k)
  print('Expected:', ans)
  print('Gotten  :', s.k_empty_slots(f, k))
