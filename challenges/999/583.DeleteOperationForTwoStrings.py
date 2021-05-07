'''
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:

1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
'''

class Solution:
  def minDistance1(self, word1: str, word2: str) -> int:
    n1, n2 = len(word1), len(word2)
    dp = [[0 for _ in range(n1)] for _ in range(n2)]

    for i in range(n2):
      for j in range(n1):
        match = 1 if (word1[j] == word2[i]) else 0
        up = match if i == 0 else dp[i-1][j]
        left = match if j == 0 else dp[i][j-1]
        diag = 0 if (i == 0 or j == 0) else (dp[i-1][j-1] + match)

        dp[i][j] = max(up, left, diag)
        # print(i, j, up, left, diag, match, dp[i][j])

    # print(dp)

    return n1 + n2 - 2*dp[n2-1][n1-1]


  def minDistance(self, word1: str, word2: str) -> int:
    def lcs() -> int:
      pos2 = defaultdict(list)
      char1_set = set(word1)
      dp = [] # longest common sequence

      # add all the potential char matches between word2 and word1
      for index in range(len(word2)-1, -1, -1):
        char = word2[index]
        if char in char1_set:
          pos2[char].append(index)

      # add chars if they can be a match char from each char's
      # matching positions in word2, and then moves forward.
      for char in word1:
        pos = pos2[char]

        # not a match found in word2, skip
        if len(pos) == 0:
          continue

        if len(dp) == 0:
          # matching sequence is empty, add and done
          dp.append(pos[-1])

        else:
          # find the proper location to insert the matching char
          for index in pos:
            if index > dp[-1]:
              # if the char can be added to the back of the current seq, done
              dp.append(index)

            else:
              # replace the later matching pos with an earlier position
              frontIdx = bisect_left(dp, index)
              if frontIdx < len(dp):
                dp[frontIdx] = index

      return len(dp)

    return len(word1) + len(word2) - 2*lcs()
