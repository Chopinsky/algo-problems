'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
'''


from collections import defaultdict


class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    count = defaultdict(int)
    l, r = 0, 0
    long = 1
    
    while r < len(s):
      count[s[r]] += 1
      size = r-l+1
      
      while size - max(count.values()) > k and l < r:
        count[s[l]] -= 1
        l += 1
        size = r-l+1
      
      long = max(long, r-l+1)
      r += 1
    
    return long
  