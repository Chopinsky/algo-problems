'''
3304-find-the-k-th-character-in-string-game-i
'''


class Solution:
  def kthCharacter(self, k: int) -> str:
    if k == 1:
      return "a"

    mask = 1
    k -= 1
    while mask < k:
      mask <<= 1

    if mask > k:
      mask >>= 1

    step = 0
    while k > 0:
      if mask & k > 0:
        k -= mask
        step += 1

      mask >>= 1

    # print('done:', step)
    idx = step % 26

    return chr(ord('a') + idx)

  def kthCharacter0(self, k: int) -> str:
    if k == 1:
      return "a"

    def iterate(curr: str) -> str:
      nxt = ""

      for ch in curr:
        idx = (ord(ch) - ord('a') + 1) % 26
        nxt += chr(ord('a') + idx)
      
      curr += nxt
      if len(curr) >= k:
        curr = curr[:k]

      return curr

    word = "a"
    while len(word) < k:
      word = iterate(word)

    # print('done:', word)
    return word[k-1]
        