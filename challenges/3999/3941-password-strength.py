'''
3941-password-strength
'''


class Solution:
  def passwordStrength(self, password: str) -> int:
    chars = set(list(password))
    score = 0

    for ch in chars:
      if 'a' <= ch <= 'z':
        score += 1
        continue

      if 'A' <= ch <= 'Z':
        score += 2
        continue

      if '0' <= ch <= '9':
        score += 3
        continue

      score += 5

    return score
        