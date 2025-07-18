'''
3136-valid-word
'''


class Solution:
  def isValid(self, word: str) -> bool:
    if len(word) < 3:
      return False

    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    vc = 0
    cc = 0

    for ch in word:
      if '0' <= ch <= '9':
        continue

      if ch in vowels:
        vc += 1
        continue

      if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
        cc += 1
        continue

      return False

    return vc >= 1 and cc >= 1
        