'''
3504-longest-palindrome-after-substring-concatenation-ii
'''


class Solution:
  def longestPalindrome(self, s: str, t: str) -> int:
    s_set = set(s)
    t_set = set(t)

    if len(s_set) == 1 and len(t_set) == 1:
      if list(s_set)[0] == list(t_set)[0]:
        return len(s) + len(t)

    def max_palindrome(arr: str, pos: int, even_odd: int):
      if even_odd == 0: # Even case
        l, r = pos, pos+1

      else:
        l, r = pos, pos

      min_l = pos
      max_r = pos

      while l >= 0 and r < len(arr):
        if arr[l] != arr[r]:
          break

        min_l = l
        max_r = r
        l -= 1
        r += 1
        
      return min_l, max_r

    n, m = len(s), len(t)
    s_pal = [1] * n

    for i in range(n):
      even_l, even_r = max_palindrome(s, i, 0)
      even_len = even_r - even_l + 1
      s_pal[even_l] = max(s_pal[even_l], even_len)
      
      odd_l, odd_r = max_palindrome(s, i, 1)
      odd_len = odd_r - odd_l + 1
      s_pal[odd_l] = max(s_pal[odd_l], odd_len)

    t_pal = [1] * m
    for j in range(m):
      even_l, even_r = max_palindrome(t, j, 0)
      even_len = even_r - even_l + 1
      t_pal[even_r] = max(t_pal[even_r], even_len)

      odd_l, odd_r = max_palindrome(t, j, 1)
      odd_len = odd_r - odd_l + 1
      t_pal[odd_r] = max(t_pal[odd_r], odd_len)

    ans = 1
    for s_pos in range(n):
      for t_pos in range(m-1, -1, -1):
        ans = max(ans, s_pal[s_pos], t_pal[t_pos])
        s_l, t_r = s_pos, t_pos

        while s_l < n and t_r >= 0:
          if s[s_l] != t[t_r]:
            break

          s_l += 1
          t_r -= 1
          common_len = s_l - s_pos
          ans = max(ans, 2*common_len)
          
          if s_l < n:
            ans = max(ans, 2*common_len + s_pal[s_l])

          if t_r >= 0:
            ans = max(ans, 2*common_len + t_pal[t_r])

    return ans
    