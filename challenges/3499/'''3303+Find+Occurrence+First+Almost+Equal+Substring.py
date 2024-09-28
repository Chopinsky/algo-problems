'''
3303. Find the Occurrence of First Almost Equal Substring

"abcdefg"
"bcdffg"
"ababbababa"
"bacaba"
"abcd"
"dba"
"dde"
"d"
"ede"
"d"
"ffggf"
"gg"
"cbccbcccb"
"bcb"
"mllllll"
"lll"
'''

class Solution:
  '''
  use z-func to calculate the length of the substring (e.g., ln) starting at index-i, such that this substring
  also matches the prefix of the string (e.g., s[0:ln] == s[i:i+ln]); use z-func, we can construct two strings:
  - pattern+s (-> s1), and use z-func, we can know the longest substring from index-i that matches the prefix
    of the pattern (i.e., for i in s1[m:], where m = len(s), s1[i] is the length of the prefix match len);
  - pattern_rev+s_rev (-> s2), and use z-func, we know the longest substring from index-n to index-i that also
    matches the suffix of the pattern (i.e., for i in s2[m:], s2[i] is the length of the suffix match len), 
    and the tail match for i from the front will be (m+n-i) - m = n-i;
  '''
  def minStartingIndex(self, s: str, pattern: str) -> int:
    m = len(pattern)
    n = len(s)
    if m == 1:
      return 0
    
    def z_func(s):
      z = [0] * n
      l, r = 0, 0
      
      for i in range(1, n):
        if i <= r:
          z[i] = min(r-i+1, z[i-l])
          
        while i+z[i] < n and s[z[i]] == s[i+z[i]]:
          z[i] += 1
          
        if i+z[i]-1 > r:
          l, r = i, i+z[i]-1
          
      return z
      
    z1 = z_func(pattern + s)
    z2 = z_func(pattern[::-1] + s[::-1])
    
    for i in range(n - m + 1):
      if z1[m+i] + 1 + z2[n-i] >= m:
        return i
      
    return -1
        