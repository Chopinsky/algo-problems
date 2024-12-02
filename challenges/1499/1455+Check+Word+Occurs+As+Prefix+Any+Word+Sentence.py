'''
1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
'''

class Solution:
  def isPrefixOfWord(self, sentence: str, word: str) -> int:
    words = sentence.split(' ')
    for i, w in enumerate(words):
      if w.startswith(word):
        return i+1
    
    return -1
        