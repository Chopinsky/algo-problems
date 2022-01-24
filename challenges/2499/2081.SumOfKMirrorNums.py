'''
A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
Given the base k and the number n, return the sum of the n smallest k-mirror numbers.

 

Example 1:

Input: k = 2, n = 5
Output: 25
Explanation:
The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
  base-10    base-2
    1          1
    3          11
    5          101
    7          111
    9          1001
Their sum = 1 + 3 + 5 + 7 + 9 = 25. 
Example 2:

Input: k = 3, n = 7
Output: 499
Explanation:
The 7 smallest 3-mirror numbers are and their representations in base-3 are listed as follows:
  base-10    base-3
    1          1
    2          2
    4          11
    8          22
    121        11111
    151        12121
    212        21212
Their sum = 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499.
Example 3:

Input: k = 7, n = 17
Output: 20379000
Explanation: The 17 smallest 7-mirror numbers are:
1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596

Constraints:

2 <= k <= 9
1 <= n <= 30
'''


from typing import List


class Solution:
  def kMirror(self, k: int, n: int) -> int:
    if n < k:
      return sum(i for i in range(1, n+1))
    
    def is_k_mirr(val: int) -> bool:
      if val < k:
        return True
      
      digits = []
      while val > 0:
        digits.append(val % k)
        val //= k
        
      l, r = 0, len(digits)-1
      while l < r:
        if digits[l] != digits[r]:
          return False
        
        l += 1
        r -= 1
        
      return True
    
    def form_num(d: List[int], ln: int) -> int:
      base = 0
      for val in d[::-1]:
        base = base*10 + val
        
      if ln%2 == 1:
        d = d[1:]
        
      for val in d:
        base = base*10 + val
        
      return base
    
    def nxt_pal(ln: int) -> int:
      size = ln // 2 if ln % 2 == 0 else (ln+1) // 2
      d = [0]*(size-1) + [1]
      yield form_num(d, ln)
      
      while True:
        idx = 0
        while idx < len(d):
          if d[idx] != 9:
            break
            
          idx += 1
          
        if idx == len(d):
          break
          
        d[idx] += 1
        for jdx in range(idx):
          d[jdx] = 0
          
        yield form_num(d, ln)
    
    count = 0
    sums = 0
    ln = 0
    
    while count < n:
      ln += 1
      for num in nxt_pal(ln):
        if is_k_mirr(num):
          sums += num
          count += 1
          
        if count >= n:
          break
      
    return sums
    