'''
2384. Largest Palindromic Number

You are given a string num consisting of digits only.

Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

Notes:

You do not need to use all the digits of num, but you must use at least one digit.
The digits can be reordered.

Example 1:

Input: num = "444947137"
Output: "7449447"
Explanation: 
Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
It can be shown that "7449447" is the largest palindromic integer that can be formed.
Example 2:

Input: num = "00009"
Output: "9"
Explanation: 
It can be shown that "9" is the largest palindromic integer that can be formed.
Note that the integer returned should not contain leading zeroes.

Constraints:

1 <= num.length <= 10^5
num consists of digits.
'''

from collections import Counter


class Solution:
  def largestPalindromic(self, num: str) -> str:
    c = Counter(num)
    cand = []
    single = -1
    
    for val in sorted(c, reverse=True):
      if c[val] % 2 == 1:
        single = max(single, int(val))
        
      if c[val] > 1:
        cand.append((val, c[val]//2))
    
    base = ''
    if cand[0][0] == '0':
      return str(single) if single >= 0 else '0'

    # print(cand)
    
    for val, cnt in cand:
      base += val * cnt
      
    return base + ('' if single < 0 else str(single)) + base[::-1] 
  