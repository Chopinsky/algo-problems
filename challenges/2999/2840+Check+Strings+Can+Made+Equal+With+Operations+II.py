'''
2840. Check if Strings Can be Made Equal With Operations II

You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.

Example 1:

Input: s1 = "abcdba", s2 = "cabdab"
Output: true
Explanation: We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
- Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
- Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.
Example 2:

Input: s1 = "abe", s2 = "bea"
Output: false
Explanation: It is not possible to make the two strings equal.
 

Constraints:

n == s1.length == s2.length
1 <= n <= 10^5
s1 and s2 consist only of lowercase English letters.
'''

from collections import defaultdict


class Solution:
  def checkStrings(self, s1: str, s2: str) -> bool:
    e1, e2 = defaultdict(int), defaultdict(int)
    o1, o2 = defaultdict(int), defaultdict(int)
    
    for i in range(len(s1)):
      c1, c2 = s1[i], s2[i]
      if i % 2 == 0:
        e1[c1] += 1
        e2[c2] += 1
      else:
        o1[c1] += 1
        o2[c2] += 1
        
    if len(e1) != len(e2) or len(o1) != len(o2):
      return False
    
    # print(e1, e2)
    # print(o1, o2)
    
    for ch, cnt in e1.items():
      if e2[ch] != cnt:
        return False
      
    for ch, cnt in o1.items():
      if o2[ch] != cnt:
        return False
      
    return True
        