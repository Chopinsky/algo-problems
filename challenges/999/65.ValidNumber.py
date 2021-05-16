'''
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
At least one digit, followed by a dot '.'.
At least one digit, followed by a dot '.', followed by at least one digit.
A dot '.', followed by at least one digit.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
At least one digit.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:

Input: s = "0"
Output: true

Example 2:

Input: s = "e"
Output: false

Example 3:

Input: s = "."
Output: false

Example 4:

Input: s = ".1"
Output: true

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
'''

class Solution:
  def isNumber(self, s: str) -> bool:
    def parseNumber(src: str, top_level: bool) -> bool:
      if not src:
        return False

      if src[0] == '+' or src[0] == '-':
        if len(src) == 1:
          return False

        src = src[1:]

      dot = False
      for i, char in enumerate(src):
        if char == 'e' or char == 'E':
          if not top_level or i == 0 or (dot and i == 1):
            return False

          return parseNumber(src[i+1:], False)

        if char >= '0' and char <= '9':
          continue

        if char == '.':
          if len(src) == 1 or not top_level or dot:
            return False

          dot = True
          continue

        return False

      return True

    return parseNumber(s, True)
