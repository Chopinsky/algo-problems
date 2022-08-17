'''
1754. Largest Merge Of Two Strings

You are given two strings word1 and word2. You want to construct a string merge in the following way: while either word1 or word2 are non-empty, choose one of the following options:

If word1 is non-empty, append the first character in word1 to merge and delete it from word1.
For example, if word1 = "abc" and merge = "dv", then after choosing this operation, word1 = "bc" and merge = "dva".
If word2 is non-empty, append the first character in word2 to merge and delete it from word2.
For example, if word2 = "abc" and merge = "", then after choosing this operation, word2 = "bc" and merge = "a".
Return the lexicographically largest merge you can construct.

A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b. For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c.

Example 1:

Input: word1 = "cabaa", word2 = "bcaaa"
Output: "cbcabaaaaa"
Explanation: One way to get the lexicographically largest merge is:
- Take from word1: merge = "c", word1 = "abaa", word2 = "bcaaa"
- Take from word2: merge = "cb", word1 = "abaa", word2 = "caaa"
- Take from word2: merge = "cbc", word1 = "abaa", word2 = "aaa"
- Take from word1: merge = "cbca", word1 = "baa", word2 = "aaa"
- Take from word1: merge = "cbcab", word1 = "aa", word2 = "aaa"
- Append the remaining 5 a's from word1 and word2 at the end of merge.

Example 2:

Input: word1 = "abcabc", word2 = "abdcaba"
Output: "abdcabcabcaba"

Constraints:

1 <= word1.length, word2.length <= 3000
word1 and word2 consist only of lowercase English letters.
'''


class Solution:
  '''
  should choose the char from the larger remainder strings
  '''
  def largestMerge(self, word1: str, word2: str) -> str:
    m, n = len(word1), len(word2)
    ans = ''
    
    def search(i: int, j: int):
      while i < m and j < n and word1[i] == word2[j]:
        i += 1
        j += 1
      
      if i >= m:
        return 1
      
      if j >= n:
        return 0
      
      return 0 if word1[i] > word2[j] else 1
    
    idx, jdx = 0, 0
    while idx < m or jdx < n:
      if idx >= m:
        ans += word2[jdx:]
        break
        
      if jdx >= n:
        ans += word1[idx:]
        break
      
      if word1[idx] > word2[jdx]:
        ans += word1[idx]
        idx += 1
        continue
        
      if word2[jdx] > word1[idx]:
        ans += word2[jdx]
        jdx += 1
        continue
        
      choice = search(idx, jdx)
      if choice == 0:
        ans += word1[idx]
        idx += 1
        
      else:
        ans += word2[jdx]
        jdx += 1
        
    return ans
            