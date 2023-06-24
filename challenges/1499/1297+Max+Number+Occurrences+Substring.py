'''
1297. Maximum Number of Occurrences of a Substring

Given a string s, return the maximum number of ocurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.

Example 1:

Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
Example 2:

Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.

Constraints:

1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s consists of only lowercase English letters.
'''

from collections import defaultdict


class Solution:
  def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    store = defaultdict(int)
    freq = defaultdict(int)
    cnt = 0
    n = len(s)
    
    def check(s, size):
      store.clear()
      freq.clear()
      l, r = 0, 0
      
      while r-l < size:
        freq[s[r]] += 1
        r += 1
      
      # print('check:', size, s[l:r])
      if len(freq) <= maxLetters:
        store[s[l:r]] += 1
      
      while r < n:
        freq[s[l]] -= 1
        freq[s[r]] += 1
        
        if not freq[s[l]]:
          del freq[s[l]]
          
        l += 1
        r += 1
        
        if len(freq) <= maxLetters:
          store[s[l:r]] += 1
      
      return max(store.values()) if store else 0
    
    for size in range(minSize, maxSize+1):
      cnt = max(cnt, check(s, size))
      
    return cnt
  