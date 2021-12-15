'''
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

Example 1:

Input: s = "banana"
Output: "ana"

Example 2:

Input: s = "abcd"
Output: ""

Constraints:

2 <= s.length <= 3 * 10^4
s consists of lowercase English letters.
'''


class Solution:
  def longestDupSubstring(self, s: str) -> str:
    n = len(s)
    suffix = []
    
    for i in range(0, n):
      suffix.append(s[i:])
      
    # sort the suffix string such that the first few 
    # chars that are the same will be adjacent to each
    # other
    suffix.sort()
    curr_len = 0
    lrs = ''
    
    # find the longest common pattern between s0 and s1
    def lcp(s0: str, s1: str) -> int:
      # get the upper limit
      bound = len(s0) if len(s0) <= len(s1) else len(s1)
      
      # not going to provide a better solution
      if bound <= curr_len:
        return -1
      
      # maximum match
      if s0[:bound] == s1[:bound]:
        return bound
      
      # base case: compare substr with length `curr_len`, if
      # we have a match, then we can extend from here; otherwise,
      # we won't provide a better solution, stop right here.
      ln = curr_len
      if s0[:ln] != s1[:ln]:
        return -1
      
      # increase the size to find the matching pattern -- possible
      # improvement: use binary search for this part
      while s0[ln] == s1[ln] and ln <= bound:
        ln += 1
        
      return ln if ln > curr_len else -1
    
    for i in range(n-1):
      # get new longest common pattern
      length = lcp(suffix[i], suffix[i+1])
      
      # if the length is longer, update the result string
      if length > curr_len:
        lrs = suffix[i][:length]
        curr_len = length
        
    return lrs
  
    
  def longestDupSubstring0(self, s: str) -> str:
    n = len(s)

    def search(ln: int) -> str:
      base = s[:ln]
      seen = set([base])
      
      for i in range(ln, n):
        nxt = base[1:] + s[i]
        if nxt in seen:
          # print(i, seen, nxt)
          return nxt
        
        seen.add(nxt)
        base = nxt
        
      return ''
        
    l, r = 0, n
    ans = ''
    
    while l < r:
      m = (l + r) // 2
      substr = search(m)
      # print(l, r, m, substr)
      
      if substr:
        ans = substr
        l = m+1
      else:
        r = m-1
    
    substr = search(l)
    if substr:
      ans = substr
      
    return ans
  