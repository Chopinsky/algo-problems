'''
Special binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.
You are given a special binary string s.

A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.

Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.

Example 1:

Input: s = "11011000"
Output: "11100100"
Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.
Example 2:

Input: s = "10"
Output: "10"

Constraints:

1 <= s.length <= 50
s[i] is either '0' or '1'.
s is a special binary string.
'''


from functools import lru_cache


class Solution:
  def makeLargestSpecial(self, s: str) -> str:
    @lru_cache(None)
    def update(s: str) -> str:
      n = len(s)
      
      # no swap is possible
      if n <= 2:
        return s
      
      # already the lexicographically largest
      if (s[:n//2] == '1' * (n//2)) or (s[0] == '0'):
        return s
      
      best = s
      found = False
      
      # the start of the first half of the sbs
      for i in range(n-3):
        if s[i] != '1':
          continue
          
        cnt1, cnt0 = 1, 0
        
        # the end of the first half of the sbs
        for j in range(i+1, n-2):
          if s[j] == '0':
            cnt0 += 1
          else:
            cnt1 += 1

          # print('first', cnt0, cnt1, s[i:j+1])
          
          # prefix fail: not going to make a special bin 
          # str anymore
          if cnt0 > cnt1:
            break

          # not yet a spcial bin str, or the tail part is
          # not going to be a special bin str
          if (cnt1 > cnt0) or (s[j+1] == '0'):
            continue
          
          # the prefix is a special bin str, check the tail
          # part
          rest = update(s[j+1:])
          rcnt1, rcnt0 = 1, 0

          # the tail part starts from [0, len(rest)-1] for rest
          for k in range(1, len(rest)):
            # further swaps won't imporve
            end = min(k+1, j+1-i)
            if rest[:end] < s[i:i+end]:
              break
              
            if rest[k] == '0':
              rcnt0 += 1
            else:
              rcnt1 += 1
              
            # not going to make a special bin str anymore
            if rcnt0 > rcnt1:
              break
      
            # not yet a special bin str
            if rcnt1 > rcnt0:
              continue
              
            target = s[:i] + rest[:k+1] + update(s[i:j+1] + rest[k+1:])
            if target > best:
              best = target
        
        if found:
          break
        
      return best
    
    return update(s)
  