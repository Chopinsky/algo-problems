'''
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]

Constraints:

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.
'''

from typing import List
from collections import defaultdict

class Solution:
  def palindromePairs(self, words: List[str]) -> List[List[int]]:
    # 0 means the word is not reversed, 1 means the word is reversed; sort to bring
    # shared suffix/prefix words together
    w = sorted([(w, 0, i, len(w)) for i, w in enumerate(words)] +
               [(w[::-1], 1, i, len(w)) for i, w in enumerate(words)])
    
    length = len(w)
    result = []
    
    for i, (word1, rev1, ind1, len1) in enumerate(w):
      for j in range(i+1, length):
        word2, rev2, ind2, _ = w[j]

        # early short-circuit if we're not going to find any more "shared" 
        # prefix/suffix
        if not word2.startswith(word1):
          break

        # check if different words and can form a palindrome
        if ind1 != ind2 and rev1 ^ rev2:
          rest = word2[len1:]

          if rest == rest[::-1]: 
            result.append([ind1, ind2] if rev2 else [ind2, ind1])

    return result


  def palindromePairs0(self, words: List[str]) -> List[List[int]]:
    def is_pal(w: str) -> bool:
      n = len(w)
      if n <= 1:
        return True
      
      for i in range(n//2):
        if w[i] != w[n-i-1]:
          return False
        
      return True
    
    d = defaultdict(list)
    blank = -1
    low = 5001
    
    for i, w in enumerate(words):
      if len(w) == 0:
        blank = i
      elif len(w) < low:
        low = len(w)
    
    low -= 1
    
    for i, w in enumerate(words):
      rev = w[::-1]
      
      for j in range(len(w), low, -1):
        d[rev[:j]].append(i)
    
    # print(d, low)
    
    ans = []
    seen = set()
    
    for i, w in enumerate(words):
      n0 = len(w)
      if blank >= 0 and i != blank and is_pal(w):
        # print('blank', i, blank)
        ans.append([i, blank])
        ans.append([blank, i])
      
      for l in range(1, len(w)+1):
        # print(w[:l], l, w[:l] in d)
        
        if w[:l] not in d:
          continue
          
        for j in d[w[:l]]:
          l0 = len(words[j])
          
          # print(w, words[j])
            
          if l0 == n0 and i != j and ((i,j) not in seen):
            if w == words[j][::-1]:
              seen.add((i,j))
              ans.append([i, j])
              # print('adding 3:', i, j, seen, (i,j) in seen)
            
            continue
          
          if j == i or l0 != l or ((i,j) in seen):
            continue
            
          if is_pal(w[l:]):
            # print('adding 2:', i, j, l, w[l:])
            seen.add((i,j))
            ans.append([i, j])
      
      if w not in d:
        continue
      
      for j in d[w]:
        l = len(words[j])
        if j == i or l <= n0 or ((i,j) in seen):
          continue
          
        if is_pal(words[j][:l-n0]):
          seen.add((i,j))
          ans.append([i, j])
          # print('adding 1:', i, j, words[j][n0:])
      
    return ans


  def palindromePairs1(self, words: List[str]) -> List[List[int]]:
    # compare = [w[::-1] for w in words]

    def is_pal(w: str) -> bool:
      n = len(w)
      if n <= 1:
        return True

      for i in range(n//2):
        if w[i] != w[n-i-1]:
          return False

      return True

    ans = []

    def pal_check(w0: str, w1: str, i: int, j: int) -> bool:
      n0, n1 = len(w0), len(w1)
      if n0 == 0 or n1 == 0:
        if (n0 == 0 and is_pal(w1)) or (n1 == 0) and is_pal(w0):
          ans.append([i, j])

        return

      if n0 == n1 and w0 == w1:
        ans.append([i, j])
      elif n0 < n1:
        if w0 == w1[:n0] and is_pal(w1[n0:]):
          ans.append([i, j])
      else:
        if w0[:n1] == w1 and is_pal(w0[n1:]):
          ans.append([i, j])

      return

    for i, w0 in enumerate(words[:len(words)-1]):
      for j, w1 in enumerate(words[i+1:]):          
        pal_check(w0, w1[::-1], i, j+i+1)
        pal_check(w1, w0[::-1], j+i+1, i)

    return ans
