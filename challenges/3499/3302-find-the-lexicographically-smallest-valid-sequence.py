'''
3302-find-the-lexicographically-smallest-valid-sequence
'''


class Solution:
  def validSequence(self, word1: str, word2: str) -> List[int]:
    n1 = len(word1)
    n2 = len(word2)
    if n2 <= 1:
      return [0]

    dp = [0]*n1
    for i in range(n1-1, -1, -1):
      if i == n1-1:
        dp[i] = 1 if word1[i] == word2[-1] else 0
      else:
        ln = dp[i+1]
        j = n2-ln-1
        dp[i] = ln + (1 if j >= 0 and word1[i] == word2[j] else 0)
        
    # print('init:', dp)
    ans = []
    used = False

    for i in range(n1):
      j = len(ans)

      # done
      if j >= n2:
        break

      # a match
      if word1[i] == word2[j]:
        ans.append(i)
        continue

      # not a match
      if not used:
        if i == n1-1 or 1+len(ans)+dp[i+1] >= n2:
          # can use the wild card here
          ans.append(i)
          used = True
          continue

    return ans if len(ans) == n2 else []

        