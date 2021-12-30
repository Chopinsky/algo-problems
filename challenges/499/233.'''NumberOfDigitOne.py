'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example 1:

Input: n = 13
Output: 6

Example 2:

Input: n = 0
Output: 0

Constraints:

0 <= n <= 10^9
'''


from functools import lru_cache


class Solution:
  def countDigitOne(self, n: int) -> int:
    def count_ones(num: int) -> int:
      if num <= 0:
        return 0

      base, top = 1, num
      
      while top >= 10:
        top = top // 10
        base *= 10

      if top > 1:
        # all 1xxx are possible, count top 1s from all these numbers
        res = base 
        
      else:
        # only `1000 ~ 1abc` counts are available, get the counts for the 
        # number top 1s from these
        res = (num % base) + 1
        
      # 3 parts: 1) top 1s for all possible numbers with k-digits
      #          2) if top is 3 (e.g. 3abc), we want to count 1s from all 2xxx, 
      #             1xxx, and 0xxx numbers, where xxx range from 0 ~ 999 for 3 
      #             any-digits in this example, i.e., get one counts for `base-1`
      #          3) keep top digits, and the amount of 1s from the `abc` part in
      #             the 3abc example, i.e. count all the 1s fitting to the original
      #             71203abc number.
      return res + top * count_ones(base - 1) + count_ones(num % base)
      
    return count_ones(n)
  
  
  def countDigitOne0(self, n: int) -> int:
    if n < 10:
      return 1 if n > 0 else 0
    
    @lru_cache(None)
    def full_counts(d: int) -> int:
      if d <= 1:
        return 1 if d > 0 else 0
      
      val = 10 * full_counts(d-1) + 10 ** (d-1)
      # print(d, val)
      
      return val
      
    digits = [int(d) for d in str(n)]
    ln = len(digits)
    curr = n
    total = 0
    base = 10 ** (ln-1)
    # print('init', digits, total, base)
    
    for i in range(ln):
      # the last digit, a special case
      if i == ln-1:
        total += 1 if digits[i] > 0 else 0
        continue
      
      if digits[i] == 0:
        base //= 10
        continue
        
      # print('before:', digits[i], digits[i] * full_counts(ln-1-i), base, curr-base+1)
      total += digits[i] * full_counts(ln-1-i)
      
      if digits[i] > 1:
        total += base
      else:
        total += (curr - base + 1)
        
      # print('after:', total)
      curr -= digits[i] * base
      base //= 10
    
    return total
    