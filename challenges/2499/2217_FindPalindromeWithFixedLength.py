'''
2217. Find Palindrome With Fixed Length

Given an integer array queries and a positive integer intLength, return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if no such palindrome exists.

A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.

Example 1:

Input: queries = [1,2,3,4,5,90], intLength = 3
Output: [101,111,121,131,141,999]
Explanation:
The first few palindromes of length 3 are:
101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
The 90th palindrome of length 3 is 999.
Example 2:

Input: queries = [2,4,6], intLength = 4
Output: [1111,1331,1551]
Explanation:
The first six palindromes of length 4 are:
1001, 1111, 1221, 1331, 1441, and 1551.

Constraints:

1 <= queries.length <= 5 * 10^4
1 <= queries[i] <= 10^9
1 <= intLength <= 15
'''

from typing import List


class Solution:
  def kthPalindrome(self, queries: List[int], int_len: int) -> List[int]:
    ans = []
    size = (int_len+1) // 2
    base = int('1' + '0'*(size-1))
    upper = int('9'*size)
    # print(size, base, upper)
    
    for q in queries:
      src = base + (q-1)
      if src > upper:
        ans.append(-1)
        continue
        
      src = str(src)
      rev = src[::-1]
      
      if int_len % 2 == 1:
        res = src + rev[1:]
      else:
        res = src + rev
        
      ans.append(int(res))
    
    return ans
    