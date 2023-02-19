'''
2573. Find the String with LCP

We define the lcp matrix of any 0-indexed string word of n lowercase English letters as an n x n grid such that:

lcp[i][j] is equal to the length of the longest common prefix between the substrings word[i,n-1] and word[j,n-1].
Given an n x n matrix lcp, return the alphabetically smallest string word that corresponds to lcp. If there is no such string, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "aabd" is lexicographically smaller than "aaca" because the first position they differ is at the third letter, and 'b' comes before 'c'.

Example 1:

Input: lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
Output: "abab"
Explanation: lcp corresponds to any 4 letter string with two alternating letters. The lexicographically smallest of them is "abab".
Example 2:

Input: lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
Output: "aaaa"
Explanation: lcp corresponds to any 4 letter string with a single distinct letter. The lexicographically smallest of them is "aaaa". 
Example 3:

Input: lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
Output: ""
Explanation: lcp[3][3] cannot be equal to 3 since word[3,...,3] consists of only a single letter; Thus, no answer exists.

Constraints:

1 <= n == lcp.length == lcp[i].length <= 1000
0 <= lcp[i][j] <= n
'''

from typing import List


class Solution:
  '''
  the string generation part is easy -- if lcp[i][j] > 0, it means s[i] == s[j]
  and we can group (i, j) to the same group of the chars, then assign chars according
  the group number (i.e., the smallest index of the group);

  harder part is to determine if this is a valid lcp matrix: all cell numbers must be
  highly symmetric, and the suffix matching chain needs to fall into a anti-diagno
  line which should also be valid in length
  '''
  def findTheString(self, lcp: List[List[int]]) -> str:
    n = len(lcp)
    
    for i in range(n):
      if lcp[i][i] != n-i:
        # print(0, i)
        return ""
      
      for j in range(i+1, n):
        if lcp[i][j] != lcp[j][i]:
          # print(1, i, j)
          return ""
          
        # check len
        ln = min(n-i, n-j)
        if lcp[i][j] > ln:
          # print(2, i, j, ln)
          return ""
          
        # from 1st char
        if i == 0 or j == 0:
          continue
          
        # check steps
        step = lcp[i-1][j-1] - lcp[i][j]
        if step > 1 or (lcp[i-1][j-1] > 0 and step < 0) or (step == 0 and lcp[i][j] > 0):
          # print(3, i, j, step)
          return ""
      
    cand = 0
    base = ord('a')
    g = [i for i in range(n)]
    gc = {}
    
    def find(x):
      while g[x] != x:
        x = g[x]
        
      return x
    
    def union(x, y):
      x0, y0 = find(x), find(y)
      if x0 <= y0:
        g[y0] = x0
      else:
        g[x0] = y0
    
    for c in range(n-1):
      for r in range(c+1, n):
        if lcp[r][c] > 0:
          union(r, c)
    
    ans = ''
    for i in range(n):
      root = find(i)
      if root not in gc:
        if cand >= 26:
          return ""
        
        gc[root] = chr(base + cand)
        cand += 1
      
      ans += gc[root]
      
    # print(gc)
    return ans
    