'''
3518-smallest-palindromic-rearrangement-ii
'''

from typing import List


class Solution:
  def smallestPalindrome(self, s: str, k: int) -> str:
    def capped_comb(n: int, r: int, mval: int) -> int:
      if r > n:
        return 0

      r = min(r, n-r)
      result = 1

      for d in range(1, r+1):
        result = result * (n-r+d) // d
        if result >= mval:
          return mval

      return result
        
    def count(freq: List, slots: int, mval: int) -> int:
      cnt = 1

      for f in freq:
        c0 = capped_comb(slots, f, mval)
        cnt *= c0
        if cnt >= mval:
          return mval

        slots -= f

      return cnt
    
    needed = k+1
    freq = [0]*26
    for ch in s:
      freq[ord(ch) - ord('a')] += 1

    middle = ""
    half_counts = []
    for i in range(26):
      if freq[i] % 2 == 1:
        middle = chr(ord('a') + i)

      half_counts.append(freq[i] // 2)

    ln = sum(half_counts)
    total = count(half_counts, ln, needed)

    if k > total:
      return ""

    stack = []
    for pos in range(ln):
      for c in range(26):
        if half_counts[c] == 0:
          continue

        # get the perm counts if using this char
        half_counts[c] -= 1
        c0 = count(half_counts, ln-pos-1, needed)

        if k <= c0:
          # more than enough, append the char and continue search
          # at the next position
          stack.append(chr(ord('a')+c))
          break

        # not enough counts, continue search
        k -= c0
        half_counts[c] += 1

    left = ''.join(stack)

    return left + middle + left[::-1]
