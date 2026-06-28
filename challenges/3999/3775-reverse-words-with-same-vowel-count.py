'''
3775-reverse-words-with-same-vowel-count
'''


class Solution:
  def reverseWords(self, s: str) -> str:
    words = s.split(' ')
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    # print('init:', words)

    if not words or len(words) <= 1:
      return s
    
    def count(w: str) -> int:
      return sum(1 if ch in vowels else 0 for ch in w)

    c0 = 0
    for i, w in enumerate(words):
      c1 = count(w)
      if i == 0:
        c0 = c1
      elif c0 == c1:
        words[i] = w[::-1]

    return ' '.join(words)
        