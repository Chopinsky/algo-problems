'''
Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).
 
Example 1:

Input: strs = ["aba","cdc","eae"]
Output: 3

Example 2:

Input: strs = ["aaa","aaa","aa"]
Output: -1

Constraints:

1 <= strs.length <= 50
1 <= strs[i].length <= 10
strs[i] consists of lowercase English letters.
'''


from typing import List


class Solution:
  def findLUSlength(self, strs: List[str]) -> int:
    # check if w1 is the subsequence of w2 by going over char
    # by char
    def is_subseq(w1, w2):
      i0 = 0
      for c in w2:
        if i0 < len(w1) and w1[i0] == c:
          i0 += 1
          
        if i0 == len(w1):
          return True
        
      return False
      
    # iterating over longer strings first
    strs.sort(key=len, reverse=True)
    
    # check if w1 is subseq of w2, if not, we've found
    # the longest subseq
    for i, w1 in enumerate(strs):
      done = True
      
      for j, w2 in enumerate(strs):
        if i == j:
          continue
          
        if len(w1) > len(w2):
          break
          
        if is_subseq(w1, w2):
          done = False
          break
          
      if done:
        return len(w1)
    
    return -1
  
    
  def findLUSlength1(self, strs: List[str]) -> int:
    n = len(strs)
    idx = 0
    seq = [defaultdict(list) for _ in range(n)]
    
    for i, s in enumerate(strs):
      if len(s) < len(strs[idx]):
        idx = i
        
      for j, ch in enumerate(s):
        seq[i][ch].append(j)
        
    dp = [[] for _ in range(n)]    
    # print(seq, strs[idx])
    
    for ch in strs[idx]:
      for i in range(n):
        if i == idx:
          continue
          
        arr = seq[i][ch]
        if not arr:
          continue
          
        j, seq[i][ch] = arr[0], arr[1:]
        if not dp[i] or j > dp[i][-1]:
          dp[i].append(j)
          continue
        
        rj = bisect_left(dp[i], j)
        if rj >= len(dp[i]):
          dp[i].append(j)
        else:
          dp[i][rj] = j
    
    print(dp)
    long = float('inf')
    
    for i in range(n):
      if i == idx:
        continue
        
      if len(dp[i]) < long:
        long = len(dp[i])
    
    diff = len(strs[idx]) - long
    return diff if diff > 0 else -1
  