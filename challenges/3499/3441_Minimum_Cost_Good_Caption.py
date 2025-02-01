'''
3441. Minimum Cost Good Caption
'''

from functools import cache


class Solution:
  def minCostGoodCaption(self, caption: str) -> str:
    n = len(caption)
    if n < 3: 
      return ""
    
    # [score, [(number_of_chars, char), ...]]
    dp = [
      [0, []],  # empty string 
      [float('inf'), []], 
      [float('inf'), []],
    ]
    
    def char_to_index(char):
      return ord(char) - 97
    
    def index_to_char(index):
      return chr(index + 97)
            
    def calc(i: int):
      is_four = i >= 3
      is_five = i >= 4
      
      a = b = float('inf')
      if is_five:
        a = char_to_index(caption[i - 4])
        
      if is_four:
        b = char_to_index(caption[i - 3])

      c = char_to_index(caption[i - 2])
      d = char_to_index(caption[i - 1])
      e = char_to_index(caption[i])
      
      score_3 = score_4 = score_5 = float('inf')
      char_3 = char_4 = char_5 = None
      
      for index in range(26):
        current_3 = abs(index - c) + abs(index - d) + abs(index - e)
        if current_3 < score_3:
          score_3 = current_3
          char_3 = index
        
        current_4 = current_3 + abs(index - b)
        if current_4 < score_4:
          score_4 = current_4
          char_4 = index
        
        current_5 = current_4 + abs(index - a)
        if current_5 < score_5:
          score_5 = current_5
          char_5 = index
      
      return score_3, score_4, score_5, char_3, char_4, char_5
    
    for i in range(2, n):
      score_3, score_4, score_5, char_3, char_4, char_5 = calc(i)
      
      full_score_3 = score_3 + dp[i - 2][0]
      full_score_4 = score_4 + dp[i - 3][0]
      full_score_5 = score_5 + dp[i - 4][0]
      
      data = sorted((
        (full_score_3, 3, char_3),
        (full_score_4, 4, char_4),
        (full_score_5, 5, char_5),
      ))

      best_score = data[0][0]
      options = [
        (elem[1], elem[2]) for elem in data if elem[0] == best_score
      ]

      dp.append([best_score, options])

    @cache
    def rec(i: int):
      if i == 0:
        return ''
      
      result = []
      for cnt, index in dp[i][1]:                    
        char = index_to_char(index)
        current = rec(i - cnt)
        result.append(current + char*cnt)
      
      return min(result)
            
    return rec(n)
        