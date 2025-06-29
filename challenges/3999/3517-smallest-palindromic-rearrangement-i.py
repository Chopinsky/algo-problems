'''
3517-smallest-palindromic-rearrangement-i
'''

from collections import Counter


class Solution:
  def smallestPalindrome(self, s: str) -> str:
    n = len(s)
    mid = s[n//2] if n%2 == 1 else ''
    c = Counter(s)
    chars = sorted(c)
    left = ""

    for ch in chars:
      left += ch * (c[ch]//2)

    right = left[::-1]

    return left + mid + right
        