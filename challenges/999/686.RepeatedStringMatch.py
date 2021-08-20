'''
Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "",  repeated 1 time is "abc" and repeated 2 times is "abcabc".

Example 1:

Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.

Example 2:

Input: a = "a", b = "aa"
Output: 2

Example 3:

Input: a = "a", b = "a"
Output: 1

Example 4:

Input: a = "abc", b = "wxyz"
Output: -1

Constraints:

1 <= a.length <= 10 ** 4
1 <= b.length <= 10 ** 4
a and b consist of lower-case English letters.

'''

class Solution:
  def repeatedStringMatch(self, a: str, b: str) -> int:
    if not b:
      return 0
    
    if not a:
      return -1
    
    la, lb = len(a), len(b)
    if la >= lb:
      if b in a:
        return 1
      
      if b in a+a:
        return 2
      
      return -1
    
    repeat = ceil((la + lb) / la)
    base = a * repeat
    
    for s in range(la):
      if base[s:s+lb] == b:
        return (s+lb-1) // la + 1

    return -1
    
