'''
2423. Remove Letter To Equalize Frequency
'''

class Solution:
  def equalFrequency(self, word: str) -> bool:
    c = Counter(word)
    if len(c) == 1:
      return True
    
    for i in range(len(word)):
      cand = word[:i] + word[i+1:]
      c = set(Counter(cand).values())
      # print(cand, c)
      
      if len(c) == 1:
        return True
      
    return False
    
