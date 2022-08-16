
'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 
Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 1000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
'''

from typing import List
from collections import defaultdict
from string import ascii_lowercase
from functools import lru_cache
import math


class Solution:
  def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    if endWord not in wordList:
      return []
    
    dic = defaultdict(list)
    curr, nxt = [], []
    m = len(endWord)
    
    @lru_cache(None)
    def gen_key(w: str) -> List:
      lst = []
      for i in range(m):
        lst.append(w[:i] + '*' + w[i+1:])
        
      return lst
    
    for w in wordList:
      for key in gen_key(w):
        dic[key].append(w)
        
    dist = {endWord: 0}
    d = 1
    curr, nxt = [endWord], []
    
    while curr:
      for w in curr:
        for key in gen_key(w):
          for w0 in dic[key]:
            if w0 in dist:
              continue
              
            dist[w0] = d
            nxt.append(w0)
      
      curr, nxt = nxt, curr
      nxt.clear()
      d += 1
    
    # print(dist)
    total = math.inf
    curr.clear()
    
    # init the answer seed array
    for key in gen_key(beginWord):
      for w in dic[key]:
        # w is not reachable from the endWord
        if w not in dist:
          continue
          
        if dist[w] < total:
          curr.clear()
          total = dist[w]
        
        if dist[w] == total:
          curr.append([beginWord, w])
          
    # print(total, curr)
    if total == math.inf:
      return []
    
    while curr[0][-1] != endWord:
      total -= 1

      for lst in curr:
        for key in gen_key(lst[-1]):
          for w in dic[key]:
            if dist[w] != total:
              continue
              
            nxt.append(lst + [w])
        
      curr, nxt = nxt, curr
      nxt.clear()
    
    return curr
    

  def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    wordSet = set(wordList)
    
    def neighbors(word: str):
      for i in range(len(word)):
        for c in ascii_lowercase:
          nextWord = word[:i] + c + word[i+1:]
          if nextWord in wordSet:
            yield nextWord
            
    stack = {}
    stack[beginWord] = [[beginWord]]
    
    while stack.keys():
      nextStack = defaultdict(list)
      for word in stack.keys():
        if word == endWord:
          return stack[word]
        
        for nw in neighbors(word):
          for path in stack[word]:
            nextStack[nw].append(path + [nw])
            
      wordSet -= set(nextStack.keys())
      stack = nextStack 
      
    return []  
      