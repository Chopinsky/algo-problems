'''
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
Example 2:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
Example 3:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.

Constraints:

1 <= s.length <= 5 * 10^5
s[i] is either '0' or '1'.
1 <= k <= 20
'''


class Solution:
  def hasAllCodes(self, s: str, k: int) -> bool:
    n = len(s)
    if n < k:
      return False

    val = int(s[:k], 2)
    seen = set([val])
    target = 1 << k
    top = 1 << (k-1)

    for i in range(k, n):
      if s[i-k] == '1':
        val -= top

      val <<= 1
      val |= int(s[i])
      seen.add(val)

      if len(seen) == target:
        return True

    return False


class Solution:
  def hasAllCodes(self, s: str, k: int) -> bool:
    base = set()
    for i in range(len(s)-k+1):
      # print(s[i:i+k])  
      base.add(s[i:i+k])
      if len(base) >= (1 << k):
        break
      
    return len(base) == (1<<k)
    