'''
1935-maximum-number-of-words-you-can-type
'''


class Solution:
  def canBeTypedWords(self, text: str, broken: str) -> int:
    words = text.split(' ')
    count = 0

    for w in words:
      chars = set(list(w))
      found = False
      # print('iter:', chars)

      for ch in broken:
        if ch in chars:
          found = True
          break

      if not found:
        count += 1

    return count
        