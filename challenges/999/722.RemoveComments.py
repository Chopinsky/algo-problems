'''
Given a C++ program, remove comments from it. The program source is an array of strings source where source[i] is the ith line of the source code. This represents the result of splitting the original source code string by the newline character '\n'.

In C++, there are two types of comments, line comments, and block comments.

The string "//" denotes a line comment, which represents that it and the rest of the characters to the right of it in the same line should be ignored.
The string "/*" denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of "*/" should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string "/*/" does not yet end the block comment, as the ending would be overlapping the beginning.
The first effective comment takes precedence over others.

For example, if the string "//" occurs in a block comment, it is ignored.
Similarly, if the string "/*" occurs in a line or block comment, it is also ignored.
If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.

There will be no control characters, single quote, or double quote characters.

For example, source = "string s = "/* Not a comment. */";" will not be a test case.
Also, nothing else such as defines or macros will interfere with the comments.

It is guaranteed that every open block comment will eventually be closed, so "/*" outside of a line or block comment always starts a new comment.

Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.

After removing the comments from the source code, return the source code in the same format.

Example 1:

Input: source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
Explanation: The line by line code is visualized as below:
/*Test program */
int main()
{ 
  // variable declaration 
int a, b, c;
/* This is a test
   multiline  
   comment for 
   testing */
a = b + c;
}
The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4 as comments.
The line by line output code is visualized as below:
int main()
{ 
  
int a, b, c;
a = b + c;
}

Example 2:

Input: source = ["a/*comment", "line", "more_comment*/b"]
Output: ["ab"]
Explanation: The original source string is "a/*comment\nline\nmore_comment*/b", where we have bolded the newline characters.  After deletion, the implicit newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].

Constraints:

1 <= source.length <= 100
0 <= source[i].length <= 80
source[i] consists of printable ASCII characters.
Every open block comment is eventually closed.
There are no single-quote or double-quote in the input.
'''


from typing import List, Tuple


class Solution:
  def removeComments(self, source: List[str]) -> List[str]:
    block_open = False
    ans = []
    
    def parse_row(row: str) -> Tuple[str, bool]:
      if not row:
        return (row, False)
      
      i0, i1 = row.find('/*'), row.find('//')
      idx = -1
      
      if i0 < 0 and i1 < 0:
        return (row, False)
      
      if (0 <= i1 < i0) or (i0 < 0 and i1 >= 0):
        return (row[:i1], False)
      
      is_open = True
      head = row[:i0]
      row = row[i0+2:]
      
      # print('open row:', i0, head, row)
      i2 = row.find('*/')
      
      if i2 >= 0:
        row, is_open = parse_row(row[i2+2:])
      else:
        row = ''
        
      return (head + row, is_open)
        
    for row in source:
      if block_open:
        idx = row.find('*/')
        if 0 <= idx < len(row):
          # print('to parse:', row[idx+2:])
          rem, block_open = parse_row(row[idx+2:])
          if rem:
            ans[-1] += rem
                        
      else:
        row, block_open = parse_row(row)
        if row:
          ans.append(row)
        
    return ans