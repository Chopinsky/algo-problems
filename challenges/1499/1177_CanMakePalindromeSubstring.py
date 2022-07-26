'''
You are given a string s and array queries where queries[i] = [lefti, righti, ki]. We may rearrange the substring s[lefti...righti] for each query and then choose up to ki of them to replace with any lowercase English letter.

If the substring is possible to be a palindrome string after the operations above, the result of the query is true. Otherwise, the result is false.

Return a boolean array answer where answer[i] is the result of the ith query queries[i].

Note that each letter is counted individually for replacement, so if, for example s[lefti...righti] = "aaa", and ki = 2, we can only replace two of the letters. Also, note that no query modifies the initial string s.

Example :

Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
Output: [true,false,false,true,true]
Explanation:
queries[0]: substring = "d", is palidrome.
queries[1]: substring = "bc", is not palidrome.
queries[2]: substring = "abcd", is not palidrome after replacing only 1 character.
queries[3]: substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
queries[4]: substring = "abcda", could be changed to "abcba" which is palidrome.
Example 2:

Input: s = "lyb", queries = [[0,1,0],[2,2,1]]
Output: [false,true]

Constraints:

1 <= s.length, queries.length <= 10^5
0 <= lefti <= righti < s.length
0 <= ki <= s.length
s consists of lowercase English letters.
'''

from typing import List
from functools import lru_cache
from collections import defaultdict
from bisect import bisect_left, bisect_right


class Solution:
  def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
    mask = 0
    masks = [0]*len(s)
    
    @lru_cache(None)
    def count(val: int) -> int:
      c = 0
      while val > 0:
        if val & 1:
          c += 1
          
        val >>= 1
      
      return c
    
    for i, ch in enumerate(s):
      idx = ord(ch) - ord('a')
      mask ^= (1 << idx)
      masks[i] = mask
    
    ans = [False] * len(queries)
    for m, [l, r, k] in enumerate(queries):
      lc = 0 if l == 0 else masks[l-1]
      rc = masks[r]
      ans[m] = count(lc^rc)//2 <= k
    
    return ans
    
    
  def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
    pos = defaultdict(list)
    for i, ch in enumerate(s):
      pos[ch].append(i)
      
    # print(pos)
    ans = [False] * len(queries)
    
    for m, [l, r, k] in enumerate(queries):
      odd_cnt = 0
      for ch in pos:
        i = bisect_left(pos[ch], l)
        j = bisect_right(pos[ch], r) - 1
        
        if j >= i:
          odd_cnt += (j-i+1) % 2
          
      # print(l, r, k, odd_cnt)
      ans[m] = odd_cnt//2 <= k
      
    return ans
    
    