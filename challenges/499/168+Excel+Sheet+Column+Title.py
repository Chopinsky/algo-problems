'''
168. Excel Sheet Column Title

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"

Constraints:

1 <= columnNumber <= 2^31 - 1
'''


class Solution:
  def convertToTitle(self, col: int) -> str:
    ans = ""
    
    while col > 0:
      c = (col-1) % 26
      ans = chr(ord('A') + c) + ans
      
      if col % 26 == 0:
        col = (col-1)//26
      else:
        col //= 26
        
      # print(ans, c, col)
    
    return ans
        