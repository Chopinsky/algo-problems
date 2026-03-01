'''
3855-sum-of-k-digit-numbers-in-a-range
'''


class Solution:
  def sumOfNumbers(self, l: int, r: int, k: int) -> int:
    mod = 10**9 + 7

    # all digits sum: each digit has a different val
    digit_sum = sum(val for val in range(l, r+1)) % mod

    # each digit appears: (r-l+1)^(k-1) -> count^(k-1)
    part1 = pow(r-l+1, k-1, mod)

    # sum of weights for all appearance: (10^k-1) / 9
    top_part = (pow(10, k, mod)-1) % mod
    inv9 = pow(9, mod-2, mod)
    part2 = (top_part * inv9) % mod

    # final formula
    return (digit_sum * part1 * part2) % mod


        