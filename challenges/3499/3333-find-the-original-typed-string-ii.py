'''
3333-find-the-original-typed-string-ii
'''


class Solution:
  def possibleStringCount(self, word: str, k: int) -> int:
    mod = 10**9 + 7
    word_len = len(word)
    chars = []
    index = 0
    
    while index < word_len:
      char_count = 0
      start_char = word[index]

      while index < word_len and word[index] == start_char:
        char_count += 1
        index += 1

      chars.append(char_count)

    total_comb = 1
    for group_count in chars:
      total_comb = (total_comb * group_count) % mod

    if k <= len(chars):
      return total_comb

    max_size = k - 1
    dp = [0]*(max_size + 1)
    dp[0] = 1

    for count in chars:
      next_dp = [0]*(max_size+1)
      cum_sum = 0
      
      for s in range(max_size+1):
        if s-1 >= 0:
          cum_sum = (cum_sum + dp[s-1]) % mod

        if s-count-1 >= 0:
          cum_sum = (cum_sum - dp[s-count-1] + mod) % mod
        
        next_dp[s] = cum_sum
      
      dp = next_dp

    total = 0
    for s in range(len(chars), max_size+1):
      total = (total + dp[s]) % mod

    return ((total_comb - total + mod) % mod)
    