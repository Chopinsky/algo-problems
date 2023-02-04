'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''


class Solution:
  def convert(self, s: str, num_rows: int) -> str:
    if num_rows == 1:
      return s
    
    stack = [[] for _ in range(num_rows)]
    idx = 0
    delta = 1
    
    for ch in s:
      stack[idx].append(ch)
      idx += delta
      
      if idx >= num_rows:
        idx = num_rows - 2
        delta = -1
        
      elif idx < 0:
        idx = 1
        delta = 1
    
    res = ''
    for arr in stack:
      res += ''.join(arr)
      
    return res
    

  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
      return s
    
    rows = [[] for _ in range(numRows)]
    dirs = 1
    rdx = 0
    
    for ch in s:
      rows[rdx].append(ch)
      rdx += dirs
      
      if rdx >= numRows:
        rdx -= 2
        dirs = -1
        
      elif rdx < 0:
        rdx += 2
        dirs = 1
    
    # print(rows)
    
    ans = ""
    for r in rows:
      ans += "".join(r)
    
    return ans