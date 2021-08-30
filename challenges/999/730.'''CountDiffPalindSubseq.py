'''
Given a string s, return the number of different non-empty palindromic subsequences in s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is obtained by deleting zero or more characters from the string.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences a1, a2, ... and b1, b2, ... are different if there is some i for which ai != bi.

Example 1:

Input: s = "bccb"
Output: 6
Explanation: The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.

Example 2:

Input: s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
Output: 104860361
Explanation: There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 109 + 7.

Constraints:

1 <= s.length <= 1000
s[i] is either 'a', 'b', 'c', or 'd'.
'''

class Solution:
  def countPalindromicSubsequences(self, src: str) -> int:
    cache = {}
    mod = 1000000007
    
    def dp(s: int, e: int) -> int:
      if (s, e) in cache:
        return cache[s, e]
      
      # not a valid string, skip
      if s > e:
        return 0
      
      if s == e:
        return 1
      
      # get the substring for iteration
      curr = src[s:e+1]
      count = 0
      
      # get all a..a, b..b, c..c, d..d substrings from the 
      # current one
      for ch in 'abcd':
        io = curr.find(ch)
        jo = curr.rfind(ch)
        
        # not finding the corresponding char, skip, meaning 
        # from this point on, we guarantee that i <= j
        if io < 0 or jo < 0:
          continue
          
        # get the sub-problem going
        i, j = s+io, s+jo
        
        # trick: if i==j, meaning we find a single char, then
        # it is the answer -- only 1 palin exists for this char;
        # if i<j, we count {'x', 'xx', 'x..x'} as the addition
        # of the unique palin from the `curr` substring
        count += dp(i+1, j-1) + 2 if i != j else 1
        
      cache[s, e] = count
      return count
      
    return dp(0, len(src)-1) % mod