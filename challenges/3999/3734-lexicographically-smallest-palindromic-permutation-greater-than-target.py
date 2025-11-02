'''
3734-lexicographically-smallest-palindromic-permutation-greater-than-target
'''


class Solution:
  def lexPalindromicPermutation(self, s: str, target: str) -> str:
    t = target
    cnt = [0]*26

    for ch in s:
      cnt[ord(ch)-ord('a')] += 1

    odd_cnt = 0
    mid = ''

    for i in range(26):
      if cnt[i] % 2 != 0:
        odd_cnt += 1
        mid = chr(i+ord('a'))

    # can't palindrome
    if odd_cnt > 1:
      return ""
        
    half_c = [c//2 for c in cnt]
    half_s = [''] * n_half
    n_half = len(s)//2

    def find(i: int, is_greater: bool) -> bool:
      if i == n_half:
        rev = half_s[::-1]
        res = ''.join(half_s) + mid + ''.join(rev)
        return res > t

      start = 'a' if is_greater else t[i]
      for cand in range(ord(start), ord('z')+1):
        c = chr(cand)
        pos = cand - ord('a')

        # no more char c left
        if half_c[pos] == 0:
          continue

        # check if using c here is a valid choice
        half_s[i] = c
        half_c[pos] -= 1

        if find(i+1, is_greater or c>t[i]):
          return True

        # backtrack
        half_c[pos] += 1

      return False

    if find(0, False):
      rev = half_s[::-1]
      return ''.join(half_s) + mid + ''.join(rev)

    return ''
