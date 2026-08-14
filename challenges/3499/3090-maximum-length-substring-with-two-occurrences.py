'''
3090-maximum-length-substring-with-two-occurrences
'''


class Solution:
  def maximumLengthSubstring(self, s: str) -> int:
    cnt = [0]*26

    def valid() -> bool:
      return all(val <= 2 for val in cnt)

    l = 0
    ln = 1
    for r in range(len(s)):
      idx = ord(s[r]) - ord('a')
      cnt[idx] += 1

      while not valid():
        idx = ord(s[l]) - ord('a')
        cnt[idx] -= 1
        l += 1

      ln = max(ln, r-l+1)

    return ln

      

        