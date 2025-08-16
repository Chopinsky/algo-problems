'''
2264-largest-3-same-digit-number-in-string
'''


class Solution:
  def largestGoodInteger(self, num: str) -> str:
    ans = ""
    last = ""
    cnt = 0

    for ch in num:
      if ch == last:
        cnt += 1
        if cnt == 3:
          s = ch*3
          if not ans or s > ans:
            ans = s

      else:
        last = ch
        cnt = 1

    return ans
        