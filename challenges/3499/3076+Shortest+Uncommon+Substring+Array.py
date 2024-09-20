'''
3076. Shortest Uncommon Substring in an Array

You are given an array arr of size n consisting of non-empty strings.

Find a string array answer of size n such that:

answer[i] is the shortest substring of arr[i] that does not occur as a substring in any other string in arr. If multiple such substrings exist, answer[i] should be the lexicographically smallest. And if no such substring exists, answer[i] should be an empty string.
Return the array answer.

Example 1:

Input: arr = ["cab","ad","bad","c"]
Output: ["ab","","ba",""]
Explanation: We have the following:
- For the string "cab", the shortest substring that does not occur in any other string is either "ca" or "ab", we choose the lexicographically smaller substring, which is "ab".
- For the string "ad", there is no substring that does not occur in any other string.
- For the string "bad", the shortest substring that does not occur in any other string is "ba".
- For the string "c", there is no substring that does not occur in any other string.
Example 2:

Input: arr = ["abc","bcd","abcd"]
Output: ["","","abcd"]
Explanation: We have the following:
- For the string "abc", there is no substring that does not occur in any other string.
- For the string "bcd", there is no substring that does not occur in any other string.
- For the string "abcd", the shortest substring that does not occur in any other string is "abcd".

Constraints:

n == arr.length
2 <= n <= 100
1 <= arr[i].length <= 20
arr[i] consists only of lowercase English letters.
'''

from functools import lru_cache
from typing import List

class Solution:
  def shortestSubstrings(self, arr: List[str]) -> List[str]:
    n = len(arr)
    ans = []
    cnt = {}
    
    @lru_cache(None)
    def substr(s: str) -> tuple:
      res = set()
      ln = len(s)
      
      for i in range(ln):
        for j in range(i, ln):
          res.add(s[i:j+1])
      
      return tuple(sorted(res, key=lambda x: (len(x), x)))
    
    for s in arr:
      for subs in substr(s):
        cnt[subs] = cnt.get(subs, 0) + 1
        
    # print(cnt)
    for s in arr:
      done = False
      # print('iter:', s, substr(s))
      
      for subs in substr(s):
        if cnt[subs] > 1:
          continue
          
        ans.append(subs)
        done = True
        break  
        
      if not done:
        ans.append("")
    
    return ans
        