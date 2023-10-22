'''
1371. Find the Longest Substring Containing Vowels in Even Counts

Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
'''


class Solution:
  def findTheLongestSubstring(self, s: str) -> int:
    vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
    masks = {}
    curr_mask = 0
    long = 0
    
    for i in range(len(s)):
      ch = s[i]
      mask = 0
      
      if ch in vowels:
        mask = 1 << (vowels[ch])
        
      if curr_mask & mask > 0:
        curr_mask ^= mask
      else:
        curr_mask |= mask
        
      if curr_mask == 0:
        long = i+1
        
      elif curr_mask in masks:
        long = max(long, i-masks[curr_mask])
        
      else:
        masks[curr_mask] = i
      
    return long
  