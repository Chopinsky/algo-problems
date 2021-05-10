from math import sqrt, floor

'''
Count the number of prime numbers less than a non-negative number, n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:

Input: n = 0
Output: 0

Example 3:

Input: n = 1
Output: 0

Constraints:

0 <= n <= 5 * 106
'''

class Solution:
  def countPrimes(self, n: int) -> int:
    n -= 1
    if n < 2:
      return 0

    r = int(n ** 0.5)

    V = [n//d for d in range(1, r + 1)]
    V += list(range(V[-1] - 1, 0, -1))

    S = {v: v - 1 for v in V}

    for p in range(2, r + 1):
      if S[p] == S[p - 1]:
        continue

      p2 = p * p
      sp_1 = S[p - 1]

      for v in V:
        if v < p2:
          break

        S[v] -= S[v//p] - sp_1

    return S[n]


  def countPrimes1(self, n: int) -> int:
    if n <= 1:
      return 0

    nums = [True] * n
    nums[0] = False
    nums[1] = False

    for i in range(4, n, 2):
      nums[i] = False

    bound = floor(sqrt(n))
    # print(bound)

    for i in range(3, bound+1):
      upper = n // i
      for j in range(i, upper+1):
        if i*j >= n:
          break

        nums[i*j] = False

    count = 0
    for i in range(2, n):
      count += 1 if nums[i] else 0

    # print(nums)

    return count
