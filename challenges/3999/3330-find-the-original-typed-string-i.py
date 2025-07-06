'''
3330-find-the-original-typed-string-i
'''


class Solution:
  def possibleStringCount(self, word: str) -> int:
    last = ''
    repeat = 1
    count = 1

    for ch in (word+'$'):
      if ch == last:
        repeat += 1
      else:
        count += repeat-1
        # print('add:', last, ch, repeat, count)
        last = ch
        repeat = 1

    return count
        