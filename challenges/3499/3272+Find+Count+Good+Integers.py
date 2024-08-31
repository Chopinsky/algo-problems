'''
3272. Find the Count of Good Integers

You are given two positive integers n and k.

An integer x is called k-palindromic if:

x is a palindrome.
x is divisible by k.
An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.

Return the count of good integers containing n digits.

Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.

Example 1:

Input: n = 3, k = 5

Output: 27

Explanation:

Some of the good integers are:

551 because it can be rearranged to form 515.
525 because it is already k-palindromic.
Example 2:

Input: n = 1, k = 4

Output: 2

Explanation:

The two good integers are 4 and 8.

Example 3:

Input: n = 5, k = 6

Output: 2468

Constraints:

1 <= n <= 10
1 <= k <= 9
'''

from collections import Counter
from math import comb

class Solution:
  def countGoodIntegers(self, n: int, k: int) -> int:
    hn = (n+1) // 2
    low = int('1' + '0'*(hn-1))
    high = int('1' + '0'*hn)
    count = 0
    seen = set()
    
    def calc(d, s):
      total = 1
      for cnt in d.values():
        total *= comb(s, cnt)
        s -= cnt
        
      return total
    
    def count_all(base: tuple) -> int:
      dic = Counter(base)
      slot = len(base)
      
      c0 = calc(dic, slot)
      if '0' in dic:
        dic['0'] -= 1
        c1 = calc(dic, slot-1)
      else:
        c1 = 0
      
      return c0 - c1
    
    for prefix in range(low, high):
      s = str(prefix)
      rev = (s if n%2 == 0 else s[:-1])[::-1]
      sval = s + rev
      if int(sval) % k != 0:
        continue
        
      shash = tuple(sorted(list(sval)))
      if shash in seen:
        continue
      
      # print('check:', s, sval)
      seen.add(shash)
      count += count_all(shash)
      
    return count
  