'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 10^5
num consists of only digits.
num does not have any leading zeros except for the zero itself.
'''


class Solution:
  def removeKdigits(self, num: str, k: int) -> str:
    n = len(num)
    if k == n:
      return '0'

    res = []
    final_len = n-k
    
    for val in num:
      while k and res and val < res[-1]:
        res.pop()
        k -= 1
        
      res.append(val)
    
    # print('init', res)
    if len(res) > final_len:
      res = res[:final_len]
      
    # print('1', res)
    idx = 0
    while idx < len(res) and res[idx] == '0':
      idx += 1

    return '0' if (not res or idx == len(res)) else ''.join(res[idx:])
    