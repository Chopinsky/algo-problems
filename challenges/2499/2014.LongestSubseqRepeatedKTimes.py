'''
You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, where seq * k represents a string constructed by concatenating seq k times.

For example, "bba" is repeated 2 times in the string "bababcba", because the string "bbabba", constructed by concatenating "bba" 2 times, is a subsequence of the string "bababcba".
Return the longest subsequence repeated k times in string s. If multiple such subsequences are found, return the lexicographically largest one. If there is no such subsequence, return an empty string.

Example 1:

example 1
Input: s = "letsleetcode", k = 2
Output: "let"
Explanation: There are two longest subsequences repeated 2 times: "let" and "ete".
"let" is the lexicographically largest one.
Example 2:

Input: s = "bb", k = 2
Output: "b"
Explanation: The longest subsequence repeated 2 times is "b".
Example 3:

Input: s = "ab", k = 2
Output: ""
Explanation: There is no subsequence repeated 2 times. Empty string is returned.
Example 4:

Input: s = "bbabbabbbbabaababab", k = 3
Output: "bbbb"
Explanation: The longest subsequence "bbbb" is repeated 3 times in "bbabbabbbbabaababab".
 

Constraints:

n == s.length
2 <= n, k <= 2000
2 <= n < k * 8
s consists of lowercase English letters.
'''


from bisect import bisect_right


class Solution:
  def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
    pos = [[] for _ in range(26)]
    cand, pat = [], []
    n = len(s)
    
    # build char positions
    for i, ch in enumerate(s):
      pos[ord(ch) - ord('a')].append(i)

    # find all possible chars for the pattern
    for i in range(26):
      if len(pos[i]) >= k:
        cand.append(i)
        
    if not cand:
      return ''
    
    if n == k:
      return chr(ord('a')+cand[0]) if (len(cand) == 1) else ''
      
    count = {i: len(pos[i]) for i in cand}
    # print(count, pos)
    cand.reverse()
    long = ''
    
    # find the next subseq in s[start:], and return the last index of the 
    # final subseq char
    def find(start: int) -> int:
      curr = start
      for idx in pat:
        jdx = bisect_right(pos[idx], curr)
        if jdx >= len(pos[idx]):
          return -1
        
        curr = pos[idx][jdx]
      
      return curr
    
    # check if we can obtain k subseq of the repeating `pat` in the source
    # string
    def check() -> bool:
      nonlocal long
      curr = -1
      
      for i in range(k):
        nxt = find(curr)
        if nxt < 0 or nxt >= n:
          return False
        
        curr = nxt
      
      # print(pat, curr)
      if len(pat) > len(long):
        long = ''.join(chr(ord('a')+idx) for idx in pat)
        
      return True
    
    # try all combos
    def try_append(i: int):
      if len(pat) >= n//k:
        return
      
      pat.append(i)
      count[i] -= k
      # print('before check', pat)
      
      if count[i] >= 0 and check():
        for j in cand:
          try_append(j)
      
      pat.pop()
      count[i] += k
    
    for i in cand:
      try_append(i)
    
    return long
    