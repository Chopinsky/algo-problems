'''
Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. The two subsequences are disjoint if they do not both pick a character at the same index.

Return the maximum possible product of the lengths of the two palindromic subsequences.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.

Example 1:

example-1
Input: s = "leetcodecom"
Output: 9
Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
The product of their lengths is: 3 * 3 = 9.
Example 2:

Input: s = "bb"
Output: 1
Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
The product of their lengths is: 1 * 1 = 1.
Example 3:

Input: s = "accbcaxxcxx"
Output: 25
Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
The product of their lengths is: 5 * 5 = 25.

Constraints:

2 <= s.length <= 12
s consists of lowercase English letters only.
'''

class Solution:
  '''
  essentially need to build the enumeration of the palindrome subseq, then try to find the max
  product between 2 subseq that aren't intersected with each other.
  '''
  def maxProduct(self, s: str) -> int:
    n = len(s)
    
    def find(l: int, r: int):
      lst = set([(0, 0)])
      if l > r:
        return lst

      if l == r:
        lst.add((1 << l, 1))
        return lst
      
      base = find(l+1, r) | find(l, r-1)
      if s[l] == s[r]:
        src = find(l+1, r-1)
        for mask, cnt in src:
          nxt_mask = mask | (1 << l) | (1 << r)
          nxt_cnt = cnt + (2 if l != r else 1)
          lst.add((nxt_mask, nxt_cnt))
          
        lst |= src
          
      return lst | base
      
    base = list(find(0, n-1))
    best = 0
    # print(len(base), base)
    
    for i in range(1, len(base)):
      m0, c0 = base[i]
      for j in range(i):
        m1, c1 = base[j]
        if m0 & m1 > 0:
          continue
          
        best = max(best, c0 * c1)
    
    return best
        