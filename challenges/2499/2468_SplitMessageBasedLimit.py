'''
2468. Split Message Based on Limit

You are given a string, message, and a positive integer, limit.

You must split message into one or more parts based on limit. Each resulting part should have the suffix "<a/b>", where "b" is to be replaced with the total number of parts and "a" is to be replaced with the index of the part, starting from 1 and going up to b. Additionally, the length of each resulting part (including its suffix) should be equal to limit, except for the last part whose length can be at most limit.

The resulting parts should be formed such that when their suffixes are removed and they are all concatenated in order, they should be equal to message. Also, the result should contain as few parts as possible.

Return the parts message would be split into as an array of strings. If it is impossible to split message as required, return an empty array.

Example 1:

Input: message = "this is really a very awesome message", limit = 9
Output: ["thi<1/14>","s i<2/14>","s r<3/14>","eal<4/14>","ly <5/14>","a v<6/14>","ery<7/14>"," aw<8/14>","eso<9/14>","me<10/14>"," m<11/14>","es<12/14>","sa<13/14>","ge<14/14>"]
Explanation:
The first 9 parts take 3 characters each from the beginning of message.
The next 5 parts take 2 characters each to finish splitting message. 
In this example, each part, including the last, has length 9. 
It can be shown it is not possible to split message into less than 14 parts.
Example 2:

Input: message = "short message", limit = 15
Output: ["short mess<1/2>","age<2/2>"]
Explanation:
Under the given constraints, the string can be split into two parts: 
- The first part comprises of the first 10 characters, and has a length 15.
- The next part comprises of the last 3 characters, and has a length 8.

Constraints:

1 <= message.length <= 10^4
message consists only of lowercase English letters and ' '.
1 <= limit <= 10^4
'''

from typing import List


class Solution:
  def splitMessage(self, message: str, limit: int) -> List[str]:
    n = len(message)
    
    def check_parts(k: int) -> bool:
      low, up, d = 1, 9, 1
      total = 0
      base = 3 + len(str(k))
      # print('check:', k, base)
      
      while low <= k:
        # this is the number of buckets allowed in this [low, up] range
        cnt = (k if up >= k else up) - low + 1
        suffix_size = base + d
        body_size = limit - suffix_size
        # print(low, up, body_size, cnt, suffix_size)
        
        if body_size <= 0:
          return False
        
        # this is the top bucket
        if up >= k:
          total += body_size * (cnt - 1)
          rem = n - total
          # print('final:', total, rem)
          
          if rem <= 0 or rem+suffix_size > limit:
            return False
          
        # this is the middle bucket
        else:
          total += body_size * cnt
          
          # already used all 
          if total >= n:
            return False
          
        low *= 10
        up = 10*up + 9
        d += 1
      
      return True
      
    def build_parts(k: int) -> List[str]:
      stack = []
      base = 3 + len(str(k))
      d, idx = 1, 0
      low = 10
      ln = limit - (base + d)
      
      for i in range(1, k+1):
        if i == low:
          d += 1
          ln = limit - (base + d)
          low *= 10
          
        # print('build:', i, ln, limit, base, d)  
        stack.append(f'{message[idx:idx+ln]}<{i}/{k}>')
        idx += ln
      
      return stack
      
    # print('total:', n)
    for i in range(1, len(message)+1):
      if check_parts(i):
        # print('found:', i)
        return build_parts(i)
      
    return []
  