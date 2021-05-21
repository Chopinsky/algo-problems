'''
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.

Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]

Constraints:

1 <= pattern.length <= 20
1 <= words.length <= 50
words[i].length == pattern.length
pattern and words[i] are lowercase English letters.
'''

from typing import List

class Solution:
  def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
    n = len(pattern)
    ans = []
    pat_chars = {}
    pat = []

    for ch in pattern:
      if ch not in pat_chars:
        idx = len(pat_chars)
        pat_chars[ch] = idx
      else:
        idx = pat_chars[ch]

      pat.append(idx)

    # print(pat)

    d = {}
    for w in words:
      if len(w) < n:
        continue

      n0 = len(w)
      for start in range(n0-n+1):
        d.clear()
        match = True

        for j in range(start, start+n):
          ch = w[j]

          if ch in d:
            idx = d[ch]
          else:
            idx = len(d)
            d[ch] = idx

          if idx != pat[j]:
            match = False
            break

        if match:
          ans.append(w)
          break

    return ans
