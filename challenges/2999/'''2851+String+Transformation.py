'''
2851. String Transformation

You are given two strings s and t of equal length n. You can perform the following operation on the string s:

Remove a suffix of s of length l where 0 < l < n and append it at the start of s.
For example, let s = 'abcd' then in one operation you can remove the suffix 'cd' and append it in front of s making s = 'cdab'.
You are also given an integer k. Return the number of ways in which s can be transformed into t in exactly k operations.

Since the answer can be large, return it modulo 109 + 7.

Example 1:

Input: s = "abcd", t = "cdab", k = 2
Output: 2
Explanation: 
First way:
In first operation, choose suffix from index = 3, so resulting s = "dabc".
In second operation, choose suffix from index = 3, so resulting s = "cdab".

Second way:
In first operation, choose suffix from index = 1, so resulting s = "bcda".
In second operation, choose suffix from index = 1, so resulting s = "cdab".
Example 2:

Input: s = "ababab", t = "ababab", k = 1
Output: 2
Explanation: 
First way:
Choose suffix from index = 2, so resulting s = "ababab".

Second way:
Choose suffix from index = 4, so resulting s = "ababab".

Constraints:

2 <= s.length <= 5 * 10^5
1 <= k <= 10^15
s.length == t.length
s and t consist of only lowercase English alphabets.
'''


class Solution:
  '''
  def kmp(self, s, t):
    pi, res = [0 for i in range(len(s))], []
    for i in range(1, len(s)):
      j = pi[i-1]
      while j > 0 and s[j] != s[i]: j = pi[j-1]
      pi[i] = 0 if j == 0 and s[0] != s[i] else j + 1

    m, n, j = len(s), len(t), 0
    for i in range(m):
      while j >= n or j > 0 and s[i] != t[j]: j = pi[j-1]
      if s[i] == t[j]: j += 1
      if j == n: res.append(i - n + 1)

    return res
  '''
  
  def numberOfWays(self, s: str, t: str, k: int) -> int:
    mod = 10**9 + 7
    
    def z_algo():
      base = t + '$' + s + s
      n = len(base)
      arr = [0] * n
      l, r = 0, 0
      # print(base)
      
      for i in range(1, n):
        # still inside the matching window, set the prefix 
        # length if valid (prefix's remain length must still
        # be inside the current matching window)
        if i <= r and arr[i-l] < r-i+1:
          arr[i] = arr[i-l]
          # print('inherit:', arr[i])
          continue
            
        # set up new prefix window
        l = i
        if i > r:
          r = i
          
        # expand the prefix window, such that base[:r] == base[l:l+r]
        while r < n and base[r-l] == base[r]:
          r += 1

        # back track to make base[:r] == base[l:l+r] be the longest prefix
        # matching the string in the window with the prefix search pattern
        r -= 1
        
        # length of matching prefix, up to len(s)
        arr[i] = r - l + 1
        # print('window:', arr[i])
      
      return arr[len(t)+1:]
    
    n = len(s)
    arr = z_algo()

    # starting index of which it can rotate into `t`
    cand = [i for i, val in enumerate(arr[:n]) if val == len(t)]
    # cand = self.kmp((s+s)[:-1], t)
    # print('kmp:', cand)
    # print('z-array:', arr, cand)

    '''
    the idea is count the number of index rotation path; for example, if
    the starting index is 2, and this character needs to end up at index 0
    after k-operations, say k = 2, then a path is 2 -> 1 -> 0, or 2 -> 3 -> 0;
    in short , the first operation can't go to the same index, and each index
    rotation can't go to the same starting-index
    '''
    
    # calc geometric progression: starts from 0 and other index would
    # yield slightly different result, so handle them differently, too;
    # for non-zero-starting index, total count is: ((n-1)**k - (-1)**k) / n
    gp = (pow(n-1, k, mod) - (-1)**k + mod) * pow(n, mod-2, mod) % mod
    
    # for zero-starting index, need to cancel out the (-1)**k item added to
    # the above equation
    gp_zero = (gp + (-1)**k + mod) % mod
    
    return sum(gp_zero if p == 0 else gp for p in cand) % mod
   