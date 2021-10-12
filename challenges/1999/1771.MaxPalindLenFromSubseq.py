'''
You are given two strings, word1 and word2. You want to construct a string in the following manner:

Choose some non-empty subsequence subsequence1 from word1.
Choose some non-empty subsequence subsequence2 from word2.
Concatenate the subsequences: subsequence1 + subsequence2, to make the string.
Return the length of the longest palindrome that can be constructed in the described manner. If no palindromes can be constructed, return 0.

A subsequence of a string s is a string that can be made by deleting some (possibly none) characters from s without changing the order of the remaining characters.

A palindrome is a string that reads the same forward as well as backward.

Example 1:

Input: word1 = "cacb", word2 = "cbba"
Output: 5
Explanation: Choose "ab" from word1 and "cba" from word2 to make "abcba", which is a palindrome.

Example 2:

Input: word1 = "ab", word2 = "ab"
Output: 3
Explanation: Choose "ab" from word1 and "a" from word2 to make "aba", which is a palindrome.

Example 3:

Input: word1 = "aa", word2 = "bb"
Output: 0
Explanation: You cannot construct a palindrome from the described method, so return 0.

Constraints:

1 <= word1.length, word2.length <= 1000
word1 and word2 consist of lowercase English letters.
'''


class Solution:
  '''
  idea is to calculate the longest subsequence in word1 + word2, and if the 1st char
  is in word1 and last char in word2, we update the counter.
  '''
  def longestPalindrome(self, word1: str, word2: str) -> int:
    w = word1 + word2
    n, n1 = len(w), len(word1)
    dp = [[1 if j >= i else 0 for j in range(n)] for i in range(n)]
    long = 0
    # print(n, n1, dp)
    
    for i in range(n-2, -1, -1):
      for j in range(i+1, n):
        if w[i] == w[j]:
          dp[i][j] = 2 + dp[i+1][j-1]
          if i < n1 and j >= n1:
            long = max(long, dp[i][j])
            
        else:
          dp[i][j] = max(dp[i+1][j], dp[i][j-1], 1)
    
    return long