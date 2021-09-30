'''
Find the smallest prime palindrome greater than or equal to n.

Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1.

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right as it does from right to left.

For example, 12321 is a palindrome.

Example 1:

Input: n = 6
Output: 7

Example 2:

Input: n = 8
Output: 11

Example 3:

Input: n = 13
Output: 101

Note:

1 <= n <= 10 ** 8
The answer is guaranteed to exist and be less than 2 * (10 ** 8).
'''

class Solution:
  def primePalindrome(self, n: int) -> int:
    if n <= 11:
      arr = [2, 3, 5, 7, 11]
      idx = bisect.bisect_left(arr, n)
      return arr[idx]

    def is_prime(num: int) -> bool:
      upper = floor(sqrt(num)) + 1
      for i in range(2, upper):
        if num % i == 0:
          return False

      return True

    n_str = str(n)
    k = (len(n_str)+1) // 2
    num = int(n_str[0] + '0' * (k-1))
    # print(num, k)

    while num < 20000:
      base = str(num)
      if int(base[0]) % 2 == 0:
        num += int('1' + '0' * (len(base)-1))

      # only odd length is possible for palindorme primes above 11
      rev_odd = int(base + base[::-1][1:])
      num += 1

      if rev_odd < n:
        continue

      if rev_odd >= n and is_prime(rev_odd):
        return rev_odd

    return -1
