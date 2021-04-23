'''
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
'''

class Solution:
  def countBinarySubstrings(self, s: str) -> int:
    ones, zeros = 0, 0
    count = 0

    for i, ch in enumerate(s):
      if i > 0 and ch != s[i-1]:
        if ch == '0':
          zeros = 1
        else:
          ones = 1
      else:
        if ch == '0':
          zeros += 1
        else:
          ones += 1

      # print(i, ch, zeros, ones)

      if (ch == '0' and zeros <= ones ) or (ch == '1' and zeros >= ones):
        count += 1

    return count