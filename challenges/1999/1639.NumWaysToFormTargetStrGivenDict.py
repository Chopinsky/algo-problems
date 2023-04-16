'''
You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

target should be formed from left to right.
To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")

Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")

Example 3:

Input: words = ["abcd"], target = "abcd"
Output: 1

Example 4:

Input: words = ["abab","baba","abba","baab"], target = "abba"
Output: 16

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 1000
All strings in words have the same length.
1 <= target.length <= 1000
words[i] and target contain only lowercase English letters.
'''


from typing import List
from collections import defaultdict
from functools import lru_cache


class Solution:
  def numWays(self, words: List[str], target: str) -> int:
    n = len(words[0])
    m = len(target)
    # print('problem:', n, m)
    
    store = [[0]*26 for _ in range(n)]
    mod = 10**9 + 7
    
    for w in words:
      for i in range(n):
        idx = ord(w[i]) - ord('a')
        store[i][idx] += 1
        
    cnt = 0
    # print(store)
    
    @lru_cache(None)
    def dp(i, j):
      # print('test:', (i, j), (n-i, m-j))
      if (n-i) < (m-j) or i >= n:
        return 0
      
      k = ord(target[j]) - ord('a')
      # print((i, j), (k, target[j]), store[i][k])
      
      if j == m-1:
        return (store[i][k] + dp(i+1, j)) % mod
      
      base = dp(i+1, j)
      if store[i][k] == 0:
        return base
      
      curr = store[i][k] * dp(i+1, j+1)
      # print('curr:', (i,j), dp(i+1, j+1))
      # print('res:', (i,j), curr, base)
      
      return (curr + base) % mod
    
    return dp(0, 0)
        
        
  def numWays(self, words: List[str], target: str) -> int:
    mod = 1_000_000_007
    n, nw, m = len(target), len(words[0]), len(words)
    if nw < n:
      return 0
    
    # preprocess -- get char counts in each column
    src = [defaultdict(int) for _ in range(nw)]
    for i in range(nw):
      for j in range(m):
        ch = words[j][i]
        src[i][ch] += 1
        
    # print(src)
    
    @lru_cache(None)
    def form_str(i: int, j: int) -> int:
      # end conditions
      if j >= n:
        return 1 if i <= nw else 0
      
      # not enough chars left to form the remainder of the string
      if nw-i < n-j:
        return 0
      
      # if we skip column-i
      count = form_str(i+1, j)
      if target[j] not in src[i]:
        return count
      
      # if we use column-i
      count += src[i][target[j]] * form_str(i+1, j+1)
      
      # mod the result
      return count % mod
    
    return form_str(0, 0)
    