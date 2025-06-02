'''
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".

Constraints:

1 <= words.length <= 10^5
words[i].length == 2
words[i] consists of lowercase English letters.
'''

from typing import List
from collections import Counter


class Solution:
  def longestPalindrome(self, words: List[str]) -> int:
    c = Counter(words)
    has_mid = False
    seen = set()
    pairs = 0
    # print('init:', c)

    for w, c0 in c.items():
      if w in seen:
        continue

      if w[0] != w[1]:
        rev = w[1]+w[0]
        if rev in c:
          pairs += min(c0, c[rev])
          seen.add(rev)
      else:
        pairs += c0 // 2
        if c0 % 2 == 1:
          has_mid = True

      seen.add(w)

    return 4*pairs + (2 if has_mid else 0)
        
  def longestPalindrome(self, words: List[str]) -> int:
    c = Counter(words)
    ln = 0
    double = False
    seen = set()
    # print(c)
    
    for w, cnt in c.items():
      if w in seen:
        continue
        
      rev = w[::-1]
      if w == rev:
        ln += 4 * (cnt // 2)
        # print("same", w, cnt)
        
        if not double and cnt % 2 == 1:
          double = True
          ln += 2
        
      elif rev in c:
        seen.add(rev)
        ln += 4 * min(cnt, c[rev])
        # print("match", w, cnt, rev, c[rev])
        
    return ln

    
  def longestPalindrome(self, words: List[str]) -> int:
    counter = Counter(words)
    checked = set()
    cnt = 0
    mid = 0
    
    for val, c in counter.items():
      if val in checked:
        continue
        
      if val[0] == val[1]:
        if c % 2 == 1:
          mid = 1
          
        cnt += c // 2
        continue
        
      rev = val[1] + val[0]
      if rev not in counter:
        continue
        
      checked.add(rev)
      cnt += min(c, counter[rev])
    
    # print(cnt, mid)
    return (cnt*2 + mid) * 2
    