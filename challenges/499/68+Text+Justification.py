'''
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
'''

from typing import List


class Solution:
  def fullJustify(self, words: List[str], max_width: int) -> List[str]:
    def build_string(src: List[str], words_ln: int) -> str:
      if not src:
        return " " * max_width
      
      n = len(src)
      spaces = max_width - words_ln
      
      if n == 1:
        return src[0] + " "*spaces
      
      if n == 2:
        return src[0] + " "*spaces + src[1]
      
      result = src[0]
      between = spaces // (n-1)
      padding_count = spaces % (n-1)
      
      for word in src[1:]:
        spaces = " " * between
        if padding_count > 0:
          spaces += " "
          padding_count -= 1
          
        result += spaces + word
      
      return result
    
    curr = []
    ans = []
    words_ln = 0
    
    for word in words:
      total_len = words_ln + len(word) + len(curr)
      if total_len > max_width:
        s = build_string(curr, words_ln)
        ans.append(s)
        # print(s)
        
        curr.clear()
        words_ln = 0
        
      curr.append(word)
      words_ln += len(word)
      
    if curr:
      s = " ".join(curr)
      paddings = max_width - len(s)
      ans.append(s + " "*paddings)
      
    return ans
        

  def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    ans = []
    line_words = []
    line = 0
    
    def add_row():
      nonlocal line, maxWidth
      
      row = ""
      offset = maxWidth - line
      size = len(line_words)
      
      if size == 1:
        row = line_words[0] + " " * offset
      else:
        space = offset // (size-1)
        extra = offset % (size-1)
        
        # print(line_words, line, offset, space, extra)
        
        for i in range(size):
          if i > 0:
            row += " " if i > extra else "  "
            row += " " * space
            row += line_words[i]
          else:
            row += line_words[0]
        
      ans.append(row)
      return
    
    for w in words:
      ln = len(w)
      
      if not line_words:
        line_words.append(w)
        line += ln
        continue
        
      if line + 1 + ln <= maxWidth:
        line += 1 + ln
        line_words.append(w)
        continue
        
      add_row()
      
      line_words.clear()
      line_words.append(w)
      line = ln
      
    if line_words:
      base = " ".join(line_words)
      if len(base) < maxWidth:
        base += " " * (maxWidth - len(base))
        
      ans.append(base)
  
    return ans
  