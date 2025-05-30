'''
3412-find-mirror-score-of-a-string
'''


class Solution:
  def calculateScore(self, s: str) -> int:
    pos = [[] for _ in range(26)]
    score = 0

    for i in range(len(s)):
      idx = ord(s[i])-ord('a')
      rev = 25-idx
      # print('iter:', idx, rev)
      if pos[rev]:
        j = pos[rev].pop()
        score += i-j
      else:
        pos[idx].append(i)

    return score
        