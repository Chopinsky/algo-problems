'''
2697-lexicographically-smallest-palindrome
'''


class Solution:
  def makeSmallestPalindrome(self, s: str) -> str:
    arr = list(s)
    n = len(arr)
    l, r = 0, n-1

    while l < r:
      if s[l] != s[r]:
        ch = min(s[l], s[r])
        arr[l] = ch
        arr[r] = ch

      l += 1
      r -= 1

    return "".join(arr)
        