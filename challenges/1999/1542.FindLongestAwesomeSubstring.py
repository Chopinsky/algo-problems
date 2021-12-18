'''
Given a string s. An awesome substring is a non-empty substring of s such that we can make any number of swaps in order to make it palindrome.

Return the length of the maximum length awesome substring of s.

Example 1:

Input: s = "3242415"
Output: 5
Explanation: "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.

Example 2:

Input: s = "12345678"
Output: 1

Example 3:

Input: s = "213123"
Output: 6
Explanation: "213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.
Example 4:

Input: s = "00"
Output: 2
 

Constraints:

1 <= s.length <= 10^5
s consists only of digits.
'''


from collections import Counter


class Solution:
  def longestAwesome(self, s: str) -> int:
    c = Counter(s)
    if len(c) == 1:
      return len(s)
    
    first_seen = {}
    mask, long = 0, 1
    zero = ord('0')
    
    singles = set()
    for i in range(10):
      singles.add(1 << i)
    
    for i, ch in enumerate(s):
      mask ^= 1 << (ord(ch) - zero)
      # print('iter:', i, ch, format(mask, '#010b'))
      
      if mask not in first_seen:
        first_seen[mask] = i
        
      if (not mask) or (mask in singles):
        long = i+1
        # print('full or single', format(mask, '#010b'), long)
        continue
        
      for j in range(10):
        # flip off 1 bit, e.g.: 1011001 -> 1010001
        prev0 = mask ^ (1<<j)
        if prev0 < mask and prev0 in first_seen:
          long = max(long, i - first_seen[prev0])
          
        # flip on 1 bit, e.g.: 1011001 -> 1011011 
        prev1 = mask | (1<<j)
        if prev1 > mask and prev1 in first_seen:
          long = max(long, i - first_seen[prev1])
      
    return long
  