class Solution:
  '''
  The idea is to build up a palindrome dictionary for if s[i:j] is palindrome,
  and check if we can find i, j such that s[0:i], s[i:j], s[j:n] are all palindrome
  strings
  '''
  def checkPartitioning(self, s: str):
    n = len(s)

    def is_pal(src: str):
      if len(src) <= 1:
        return True

      n0 = len(src)
      for i in range(n0//2):
        if src[i] != src[n0-1-i]:
          return False

      return True

    dp = [[True if i >= j else False for j in range(n)] for i in range(n)]

    # build up the dp[i][j] for if s[i:j] if a palindorme
    for l in range(2, n+1):
      i = 0
      j = i+l-1

      while j < n:
        dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        i += 1
        j += 1

    for i in range(1, n):
      for j in range(i, n-1):
        if dp[0][i-1] and dp[i][j] and dp[j+1][n-1]:
          return True

    return False
