'''
3120-count-the-number-of-special-characters-i
'''


class Solution:
  def numberOfSpecialChars(self, word: str) -> int:
    seen: set[str] = set(word)
    offset: int = ord('A') - ord('a')
    count: int = 0

    for ch in seen:
      if chr(ord(ch)+offset) in seen:
        count += 1

    return count
        