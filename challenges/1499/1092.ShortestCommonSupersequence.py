'''
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation:
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
'''

class Solution:
  def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
    l1, l2 = len(str1), len(str2)
    if l1 == 0 or l2 == 0:
      return str2 if l1 == 0 else str1

    dp = []
    temp = []
    col_added = False

    for i, c2 in enumerate(str2):
      row_added = False

      for j, c1 in enumerate(str1):
        if j > 0:
          if i > 0:
            cc = dp[j-1] + str(c1) + str(c2) if c1 != c2 else dp[j-1] + str(c1)

            if len(temp[j-1]) + 1 < len(cc):
              cc = temp[j-1] + str(c1)

            if len(dp[j]) + 1 < len(cc):
              cc = dp[j] + str(c2)

            temp.append(cc)

          else:
            if row_added:
              cc = str1[:j+1]
            else:
              cc = temp[j-1] + str(c1) if c1 != c2 else str1[:j+1]
              row_added |= (c1 == c2)

            temp.append(cc)

        else:
          if col_added:
            cc = str2[:i+1]
          else:
            if i > 0:
              cc = dp[0] + str(c2) if c1 != c2 else str2[:i+1]
            else:
              cc = str(c1) + str(c2) if c1 != c2 else str(c1)

            col_added |= (c1 == c2)

          temp.append(cc)

      dp, temp = temp, dp
      temp.clear()
      # print(dp)

    return dp[l1-1]
