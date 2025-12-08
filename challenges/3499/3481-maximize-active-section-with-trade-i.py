'''
3481-maximize-active-section-with-trade-i
'''


class Solution:
  def maxActiveSectionsAfterTrade(self, s: str) -> int:
    curr = ''
    cnt = 0
    arr = []
    total = s.count('1')

    for val in s:
      if val != curr:
        if curr and cnt > 0:
          arr.append((curr, cnt))

        curr = val
        cnt = 1

      else:
        cnt += 1

    if cnt > 0:
      arr.append((curr, cnt))

    # print('init:', arr)
    res = total
    n = len(arr)

    for i in range(n):
      if arr[i][0] == '0':
        continue

      if i == 0 or i == n-1:
        continue

      res = max(res, total+arr[i-1][1]+arr[i+1][1])
      # print('iter:', i, arr[i], total+arr[i-1][1]+arr[i+1][1])

    return res
