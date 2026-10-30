'''
3988-create-grid-with-exactly-k-paths-i
'''


class Solution:
  def createGrid(self, m: int, n: int, k: int) -> list[str]:
    if m == 1 or n == 1:
      return [] if k > 1 else (['.'*n] if m == 1 else ['.']*m)

    if k == 1:
      ans = ['.'*n]
      ans.extend(['#'*(n-1) + '.']*(m-1))
      # print('k=1', ans)
      return ans
    
    if k == 2:
      ans = [
        '.'*2 + '#'*(n-2),
        '.'*n,
      ]
      ans.extend(['#'*(n-1) + '.']*(m-2))

      return ans

    if k == 3:
      if m == 2 and n == 2:
        return []

      if m == 2:
        return [
          '.'*3 + '#'*(n-3),
          '.'*n,
        ]

      ans = [
        '..' + '#'*(n-2),
        '..' + '#'*(n-2),
        '.'*(n),
      ]
      ans.extend(['#'*(n-1) + '.']*(m-3))

      return ans

    # k == 4
    if m == 2:
      if  n < 4:
        return []

      return [
        '.'*4 + '#'*(n-4),
        '.'*n,
      ]

    if n == 2:
      if m < 4:
        return []

      ans = ['..']*4
      ans.extend(['#'*(n-1) + '.']*(m-4))

      return ans

    if (m == 3 and n < 3) or (n == 3 and m < 3):
      return []

    ans = [
      '.'*2 + '#'*(n-2),
      '.'*3 + '#'*(n-3),
      '#' + '.'*(n-1),
    ]
    ans.extend(['#'*(n-1) + '.']*(m-3))

    return ans
