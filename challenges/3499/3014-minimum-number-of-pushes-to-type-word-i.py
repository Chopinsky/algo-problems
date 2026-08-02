'''
3014-minimum-number-of-pushes-to-type-word-i
'''


class Solution:
  def minimumPushes(self, word: str) -> int:
    count = len(word)
    # print('init:', count)
    pushes = 0
    curr = 1

    while count > 0:
      batch = 8 if count >= 8 else count
      pushes += curr*batch
      count -= batch
      curr += 1

    return pushes
        