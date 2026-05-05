'''
3324-find-the-sequence-of-strings-appeared-on-the-screen
'''


class Solution:
  def stringSequence(self, target: str) -> list[str]:
    res = []
    base = ord('a')

    def gen(idx: int):
      prev = target[:idx]
      i = 0
      j = ord(target[idx]) - base
      # print('gen:', i, target[idx], j)

      while i <= j:
        res.append(prev + chr(base+i))
        i += 1

    for idx in range(len(target)):
      gen(idx)

    return res
        