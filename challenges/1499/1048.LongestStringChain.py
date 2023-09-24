'''
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2. For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chain is "a","ba","bda","bdca".

Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
'''

from collections import defaultdict
from typing import List
from functools import lru_cache


class Solution:
  def longestStrChain(self, words: List[str]) -> int:
    dic = defaultdict(list)
    n = len(words)
    words.sort(key=lambda x: (len(x), x))
    
    for i, w in enumerate(words):
      for j in range(len(w)):
        w0 = w[:j] + "*" + w[j+1:]
        dic[w0].append(i)
        
    # print(words, dic)
    
    @lru_cache(None)
    def dp(i: int):
      if i >= n:
        return 0
      
      w = words[i]
      if len(w) == len(words[-1]):
        return 1
      
      cnt = 1
      for i in range(len(w)):
        w0 = w[:i] + "*" + w[i:]
        for j in dic[w0]:
          cnt = max(cnt, 1+dp(j))
          
      for j in dic[w+"*"]:
        cnt = max(cnt, 1+dp(j))
      
      return cnt
    
    return max(dp(i) for i in range(n))
        

  def longestStrChain(self, words: List[str]) -> int:
    words.sort(key=lambda x: len(x))

    wl = defaultdict(list)
    dp = {}
    pre = {}

    for w in words:
      n = len(w)
      wl[n].append(w)
      pre[w] = []
      dp[w] = 1

    for k, v in wl.items():
      if (k-1) not in wl:
        continue

      for w in v:
        for i in range(1, k+1):
          w0 = w[:i-1] + w[i:]
          if w0 in pre:
            pre[w].append(w0)

    ans = 1
    for w in words:
      for w0 in pre[w]:
        dp[w] = max(dp[w], dp[w0]+1)
        if dp[w] > ans:
          ans = dp[w]

    return ans
