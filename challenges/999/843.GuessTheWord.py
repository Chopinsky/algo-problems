# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """

from typing import List
from collections import defaultdict
from random import shuffle, choice


def word_pair_score(w0: str, w1: str) -> int:
  score = 0
  for i in range(len(w0)):
    if w0[i] == w1[i]:
      score += 1
    
  return score


class Master:
  def __init__(self) -> None:
    self.base = ''

  def guess(self, word: str) -> int:
    return word_pair_score(word, self.base)


class Solution:
  def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
    shuffle(wordlist)
    nxt_list = []

    for _ in range(10):
      curr = choice(wordlist)
      score = master.guess(curr)
      
      for w in wordlist:
        if word_pair_score(curr, w) == score:
          nxt_list.append(w)

      wordlist, nxt_list = nxt_list, wordlist
      nxt_list.clear()


  def findSecretWord0(self, wordlist: List[str], master: 'Master') -> None:
    n = len(wordlist)
    word_scores = {}
    
    for i in range(n-1):
      a = wordlist[i]
      if a not in word_scores:
        word_scores[a] = defaultdict(set)
        
      for j in range(i+1, n):
        b = wordlist[j]
        if b not in word_scores:
          word_scores[b] = defaultdict(set)
          
        score = word_pair_score(a, b)
        word_scores[a][score].add(b)
        word_scores[b][score].add(a)
    
    curr = wordlist[0]
    trials = 10
    words = set(wordlist)
    words.discard(curr)
    # print(word_scores['yxudiu'][0])
    
    while curr and trials > 0:
      score = master.guess(curr)
      # print(trials, curr, words, score)
      if score == 6:
        break
        
      if words == word_scores[curr][score]:
        for w in words:
          if master.guess(w) == 6:
            return

      else:
        words &= word_scores[curr][score]
        curr = words.pop() if words else ''
        trials -= 1
        