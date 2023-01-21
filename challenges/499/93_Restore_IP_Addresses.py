'''
93. Restore IP Addresses

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:

1 <= s.length <= 20
s consists of digits only.
'''

from typing import List
from functools import lru_cache


class Solution:
  def restoreIpAddresses(self, s: str) -> List[str]:
    n = len(s)
    
    @lru_cache(None)
    def dp(i: int, j: int) -> List:
      if j >= 4 or i >= n:
        return []
      
      rem_seg = 4 - j
      rem_len = n-i
      
      if rem_len > 3*rem_seg:
        return []

      res = []
      
      # last segment, no need to divide
      if j == 3:
        if (s[i] == '0' and i == n-1) or (s[i] != '0' and int(s[i:]) <= 255):
          res.append((s[i:], ))  
        
        return res
      
      # dynamic programming and update
      if s[i] == '0':
        for rest_part in dp(i+1, j+1):
          res.append(('0', ) + rest_part)
          
      else:
        k = 1
        while k <= 3 and i+k <= n:
          base = int(s[i:i+k])
          if base > 255:
            break
            
          for rest_part in dp(i+k, j+1):
            res.append((s[i:i+k], ) + rest_part)
          
          k += 1
      
      return res
      
    return [".".join(ip) for ip in dp(0, 0)]
    