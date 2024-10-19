'''
Given two positive integers n and k, the binary string Sn is formed as follows:

S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

Example 1:

Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1st bit is "0".
Example 2:

Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11th bit is "1".

Constraints:

1 <= n <= 20
1 <= k <= 2^n - 1
'''

from typing import List


class Solution:
  def findKthBit(self, n: int, k: int) -> str:
    k -= 1
    vals = ['0']
    
    def extend(vals: List):
      nxt = []
      for val in vals:
        nxt.append('1' if val == '0' else '0')
        
      return vals + ['1'] + nxt[::-1]
    
    while len(vals) <= k:
      vals = extend(vals)
      # print('iter:', vals)
      
    return vals[k]
        
  def findKthBit(self, n: int, k: int) -> str:
    def find(n, k):
      if n == 1 or k == 1: 
        return 0

      ln = 2**n - 1
      mid = (ln + 1) // 2
      if k == mid:
        return 1

      if k < mid:
        return find(n-1, k)

      return 1 - find(n-1, ln-k+1)

    return str(find(n, k))
  
  def findKthBit0(self, n: int, k: int) -> str:
    s = '0'
    idx = 1
    
    while idx < n:
      rev = ''
      for i in range(len(s)-1, -1, -1):
        rev += '1' if s[i] == '0' else '0'
      
      s = s + '1' + rev
      idx += 1
    
    # print(s)
    return s[k-1]
  