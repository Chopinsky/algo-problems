'''
2901. Longest Unequal Adjacent Groups Subsequence II

You are given an integer n, a 0-indexed string array words, and a 0-indexed array groups, both arrays having length n.

The hamming distance between two strings of equal length is the number of positions at which the corresponding characters are different.

You need to select the longest subsequence from an array of indices [0, 1, ..., n - 1], such that for the subsequence denoted as [i0, i1, ..., ik - 1] having length k, the following holds:

For adjacent indices in the subsequence, their corresponding groups are unequal, i.e., groups[ij] != groups[ij + 1], for each j where 0 < j + 1 < k.
words[ij] and words[ij + 1] are equal in length, and the hamming distance between them is 1, where 0 < j + 1 < k, for all indices in the subsequence.
Return a string array containing the words corresponding to the indices (in order) in the selected subsequence. If there are multiple answers, return any of them.

A subsequence of an array is a new array that is formed from the original array by deleting some (possibly none) of the elements without disturbing the relative positions of the remaining elements.

Note: strings in words may be unequal in length.

Example 1:

Input: n = 3, words = ["bab","dab","cab"], groups = [1,2,2]
Output: ["bab","cab"]
Explanation: A subsequence that can be selected is [0,2].
- groups[0] != groups[2]
- words[0].length == words[2].length, and the hamming distance between them is 1.
So, a valid answer is [words[0],words[2]] = ["bab","cab"].
Another subsequence that can be selected is [0,1].
- groups[0] != groups[1]
- words[0].length == words[1].length, and the hamming distance between them is 1.
So, another valid answer is [words[0],words[1]] = ["bab","dab"].
It can be shown that the length of the longest subsequence of indices that satisfies the conditions is 2.  
Example 2:

Input: n = 4, words = ["a","b","c","d"], groups = [1,2,3,4]
Output: ["a","b","c","d"]
Explanation: We can select the subsequence [0,1,2,3].
It satisfies both conditions.
Hence, the answer is [words[0],words[1],words[2],words[3]] = ["a","b","c","d"].
It has the longest length among all subsequences of indices that satisfy the conditions.
Hence, it is the only answer.
 
Constraints:

1 <= n == words.length == groups.length <= 1000
1 <= words[i].length <= 10
1 <= groups[i] <= n
words consists of distinct strings.
words[i] consists of lowercase English letters.
'''

from typing import List
from functools import lru_cache


class Solution:
  def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
    @lru_cache(None)
    def within_dist(i: int, j: int):
      if i == j:
        return True
      
      w0, w1 = words[i], words[j]
      if len(w0) != len(w1):
        return False

      found = False
      for pos in range(len(w0)):
        if w0[pos] == w1[pos]:
          continue
          
        if found:
          return False
        
        found = True
        
      return True
    
    @lru_cache(None)
    def find_seq(i: int) -> int:
      if i >= n:
        return []
      
      a0 = []
      s = len(words[i])
      g = groups[i]
      
      for j in range(i+1, n):
        if len(words[j]) != s or groups[j] == g:
          continue
        
        if not within_dist(i, j):
          continue
          
        a1 = find_seq(j)
        if len(a1) > len(a0):
          a0 = a1
        
      return [i] + a0
    
    s0 = []
    for i in range(n):
      s1 = find_seq(i)
      if len(s1) > len(s0):
        s0 = s1
      
    return [words[i] for i in s0]
    