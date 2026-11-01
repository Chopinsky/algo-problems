'''
3963-create-grid-with-exactly-one-path
'''


class Solution:
  def createGrid(self, m: int, n: int) -> list[str]:
    ans = []
    for i in range(m):
      if i == 0:
        ans.append('.'*n)
      else:
        ans.append('#'*(n-1) + '.')

    return ans
