'''
Given a positive integer n, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: n = 5
Output: 2
Explanation: 5 = 5 = 2 + 3

Example 2:

Input: n = 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4

Example 3:

Input: n = 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

Note: 1 <= n <= 10 ^ 9.
'''

class Solution:
  def consecutiveNumbersSum(self, n: int) -> int:
    count = 0
    i = 1

    while n > i * (i-1) // 2:
      if (n - i * (i-1) // 2) % i == 0:
        count += 1

      i += 1

    return count


  def consecutiveNumbersSum0(self, N: int) -> int:
    # solution with prime factorisation
    res = 1 # default - number itself
    i = 3

    while N%2 == 0:
      N //= 2

    while i*i <= N:
      count = 0

      while N%i == 0:
        N //= i
        count += 1

      res *= count + 1
      i += 2

    return res if N == 1 else res *2


  def consecutiveNumbersSum1(self, n: int) -> int:
    if n <= 1:
      return n

    l, r = 1, 1
    s = 1
    count = 0

    while l < n:
      while s < n:
        r += 1
        s += r

      # print(l, r, s)

      if s == n:
        print(l, r, s)
        count += 1

      while s >= n:
        s -= l
        l += 1

        if s == n:
          print(l, r, s)
          count += 1

    return count
