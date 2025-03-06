'''
3325-count-substrings-with-k-frequency-characters-i
'''


class Solution:
  def numberOfSubstrings(self, s: str, k: int) -> int:
    l, r = 0, 0
    n = len(s)
    count = 0
    cc = [0]*26

    def check(idx: int) -> bool:
      cnt = 0
      for i in range(26):
        val = cc[i]
        if i == idx:
          val -= 1

        cnt += 1 if val >= k else 0

      return cnt > 0

    while r < n:
      idx = ord(s[r]) - ord('a')
      cc[idx] += 1

      while l < r and check(ord(s[l]) - ord('a')):
        idx = ord(s[l]) - ord('a')
        cc[idx] -= 1
        l += 1

      if any(val >= k for val in cc):
        count += l+1
        # print('add:', (l, r))

      r += 1

    return count
        