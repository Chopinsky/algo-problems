'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:

Input: s = "Hello"
Output: "hello"

Example 2:

Input: s = "here"
Output: "here"

Example 3:

Input: s = "LOVELY"
Output: "lovely"

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
'''

class Solution:
  def toLowerCase(self, s: str) -> str:
    arr = list(s)
    diff = ord('A') - ord('a')

    for i, ch in enumerate(arr):
      if ch >= 'A' and ch <= 'Z':
        arr[i] = chr(ord(ch) - diff)

    return ''.join(arr)
