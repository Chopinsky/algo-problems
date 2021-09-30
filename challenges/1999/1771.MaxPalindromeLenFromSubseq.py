class Solution:
  '''
  Convert the problem of the longest panlindrome subsequence: concatnat the 
  2 strings and find the longest panlindrome subsequence that span between 
  the left and right half of the 2 strings.

  Longest panlindrome subsequence: use dp to find the solution --> if s[i] == s[j],
  then longest palindrome equals (2 + LPS[i+1:j-1]), otherwise, it equals
  max(LPS[i+1:j], LPS[i:j-1]), that is the best solution with 1 less character
  in this subarray for consideration.
  '''
  def longestPalindrome(self, word1: str, word2: str) -> int:
    l1, l2 = len(word1), len(word2)
    l0 = l1 + l2
    dp = [[0 if i != j else 1 for j in range(l0)] for i in range(l0)]
    
    longest = 0
    s = word1 + word2

    for diag in range(1, l0):
      for i in range(l0-diag):
        j = i+diag
        dp[i][j] = dp[i+1][j-1] + 2 if s[i] == s[j] else max(dp[i+1][j], dp[i][j-1])

        if s[i] == s[j] and dp[i][j] > longest and i < l1 and j >= l1:
          longest = dp[i][j]

    # for r in dp:
    #   print(r)

    return longest

s = Solution()
a1 = s.longestPalindrome("cacb", "cbba")
print("Answer:", a1, "\nExpected:", 5)
