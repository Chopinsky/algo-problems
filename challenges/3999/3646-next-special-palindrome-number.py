'''
3646-next-special-palindrome-number
'''

from bisect import bisect_right


p = [0]*20
cnt = [0]*10
ans = []
init_called = [False]

def dfs(ln: int, mid: int, d: int, curr: int):
  if d == ln//2:
    for i in range(2, 10):
      if cnt[i] > 0 and cnt[i] != i//2:
        return

    if mid > 0 and cnt[mid] != mid//2:
      return

    ans.append(curr)
    return

  for i in range(2, 10, 2):
    if cnt[i] >= i//2:
      continue

    cnt[i] += 1
    dfs(ln, mid, d+1, curr+i*p[ln-1-d]+i*p[d])
    cnt[i] -= 1

  if mid > 0 and cnt[mid] < mid//2:
    cnt[mid] += 1
    dfs(ln, mid, d+1, curr+mid*p[ln-1-d]+mid*p[d])
    cnt[mid] -= 1


def init():
  if init_called[0]:
    return

  init_called[0] = True
  p[0] = 1
  for i in range(1, 17):
    p[i] = p[i-1]*10

  ans.append(1)

  for ln in range(2, 17, 2):
    dfs(ln, 0, 0, 0)

  for ln in range(3, 17, 2):
    for mid in range(1, 10, 2):
      dfs(ln, mid, 0, mid*p[ln//2])

  ans.sort()


class Solution:
  def specialPalindrome(self, n: int) -> int:
    init()
    idx = bisect_right(ans, n)
    # print('done:', ans, n, idx)

    return ans[idx]
