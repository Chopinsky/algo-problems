'''
You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.

To complete the ith replacement operation:

Check if the substring sources[i] occurs at index indices[i] in the original string s.
If it does not occur, do nothing.
Otherwise if it does occur, replace that substring with targets[i].
For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".

All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will not overlap.

For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because the "ab" and "bc" replacements overlap.
Return the resulting string after performing all replacement operations on s.

A substring is a contiguous sequence of characters in a string.

Example 1:

Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"
Explanation:
"a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".

Example 2:

Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation:
"ab" occurs at index 0 in s, so we replace it with "eee".
"ec" does not occur at index 2 in s, so we do nothing.

Constraints:

1 <= s.length <= 1000
k == indices.length == sources.length == targets.length
1 <= k <= 100
0 <= indexes[i] < s.length
1 <= sources[i].length, targets[i].length <= 50
s consists of only lowercase English letters.
sources[i] and targets[i] consist of only lowercase English letters.
'''


from typing import List


class Solution:
  def findReplaceString(self, base: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
    res = ''
    m, n = len(base), len(indices)
    repl = [(indices[i], sources[i], targets[i]) for i in range(n)]
    repl.sort()
    
    for i, (j, s, t) in enumerate(repl):
      if i == 0 and j > 0:
        res += base[:j]
        
      if j >= m:
        break
        
      if j+len(s) > m:
        if i == n-1:
          res += base[j:]
        else:
          end = min(repl[i+1][0], m)
          res += base[j:end]
          
        continue
      
      if base[j:j+len(s)] == s:
        res += t
        start = j+len(s)
      else:
        start = j
        
      if i < n-1:
        end = min(m, repl[i+1][0])
      else:
        end = m
        
      res += base[start:end]
        
    return res
  