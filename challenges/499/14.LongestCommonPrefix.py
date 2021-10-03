'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

'''


class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    bound = 0
    prefix = ""
    
    for i in range(200):
      curr = None
      done = False
      
      for s in strs:
        if i >= len(s):
          done = True
          break
          
        if not curr:
          curr = s[i]
        elif s[i] != curr:
          done = True
          break
          
      if done:
        break
        
      prefix += curr
    
    return prefix
  
