'''
Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.

Example 1:

Input: s = "aaabcccd", k = 2
Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
Example 2:

Input: s = "aabbaa", k = 2
Output: 2
Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
Example 3:

Input: s = "aaaaaaaaaaa", k = 0
Output: 3
Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.

Constraints:

1 <= s.length <= 100
0 <= k <= s.length
s contains only lowercase English letters.
'''


from typing import Tuple
from functools import lru_cache


class Solution:
  def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
    if not s:
      return 0
      
    stack = []
    last, cnt = '', 0
    total = 0
    
    for ch in s:
      if ch == last:
        cnt += 1
      else:
        if cnt > 0:
          stack.append((last, cnt, total))
          
        last = ch
        cnt = 1
          
      total += 1
      
    if cnt > 0:
      stack.append((last, cnt, total))
      
    # print(stack)
    
    @lru_cache(None)
    def get_cnt_len(cnt: int) -> int:
      if cnt <= 0:
        return 0

      if cnt <= 1:
        return 1

      if cnt <= 9:
        return 2

      if cnt <= 99:
        return 3

      return 1 + len(str(cnt))

    @lru_cache(None)
    def dp(i: int, rem: int) -> int:
      # edge case -- everything has been deleted
      if i < 0:
        return 0
      
      # no more deletions
      if rem <= 0:
        return sum(get_cnt_len(state[1]) for state in stack[:i+1])
      
      # decompose state
      ch, cnt, total = stack[i]

      # if we can delete the rest of the string
      if rem >= total:
        return 0

      # no deletions
      base = get_cnt_len(cnt) + dp(i-1, rem)

      # delete the whole segment, this could cause a sub-optimal
      # solution, if the segment before and after this one are of
      # the same character; however, this solution should have been 
      # optimized away from the for-loop in the parent's dp calcuations
      if rem >= cnt:
        base = min(base, dp(i-1, rem-cnt))
        
      # delete to 'a99'
      if rem >= cnt-99 > 0:
        base = min(base, 3+dp(i-1, rem-cnt+99))

      # delete to 'a9'
      if rem >= cnt-9 > 0:
        base = min(base, 2+dp(i-1, rem-cnt+9))
        
      # delete to 'a'
      if rem >= cnt-1 > 0:
        base = min(base, 1+dp(i-1, rem-cnt+1))

      # delete intermediate segements to collapse the `a` segments
      # in between
      to_del = 0
      seg_cnt = cnt
      
      # loop over the rest of the string, find other character's segments
      # to delete, and collapse segments with the same character with `ch`
      for j in range(i-1, -1, -1):
        if stack[j][0] != ch:
          to_del += stack[j][1]
          if to_del > rem:
            break
            
        else:
          seg_cnt += stack[j][1]
          nxt_cnt = get_cnt_len(seg_cnt) + dp(j-1, rem-to_del)
          base = min(base, nxt_cnt)
      
      return base
    
    return dp(len(stack)-1, k)
      

  def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
    d = [0, 1, 9, 99]
    stack = []
    last, cnt = s[0], 1
    
    for ch in s[1:]:
      if ch != last:
        stack.append((cnt, len(str(cnt)), last))
        last = ch
        cnt = 1
      else:
        cnt += 1
        
    stack.append((cnt, len(str(cnt)), last))
    # print(stack)
    
    @lru_cache(None)
    def dp(s: Tuple, rem: int) -> int:
      if not s:
        return 0
      
      if rem == 0:
        return sum(1+(val[1] if val[0] > 1 else 0) for val in s)
        
      # if don't delete any char from this chain
      cnt, l0, last = s[0]
      size = 1 + (l0 if cnt > 1 else 0) + dp(s[1:], rem)
      
      # if we can merge this chain with the chain after which
      # has the same char, try it
      idx = 1
      del_cnt = 0
      
      while idx < len(s) and del_cnt <= rem:
        if last == s[idx][2]:
          nxt_cnt = cnt + s[idx][0]
          nxt_s = ((nxt_cnt, len(str(nxt_cnt)), last),) + s[idx+1:]
          size = min(size, dp(nxt_s, rem-del_cnt))
          break
          
        del_cnt += s[idx][0]
        idx += 1
      
      # if we delete some chars from this chain
      for l1, target in enumerate(d):
        if target > cnt:
          break
          
        if cnt-target > rem:
          continue
          
        size = min(size, l1 + dp(s[1:], rem-(cnt-target)))
        
      return size
    
    return dp(tuple(stack), k)
    