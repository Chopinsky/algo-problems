'''
1781. Sum of Beauty of All Substrings

The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:

Input: s = "aabcbaa"
Output: 17

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters.
'''

from collections import defaultdict


class Solution:
  def beautySum(self, s: str) -> int:
    cnt = defaultdict(int)
    n = len(s)
    
    def get_sum(i: int) -> int:
      cnt.clear()
      cnt[s[i]] += 1
      score = 0
      
      for j in range(i+1, n):
        cnt[s[j]] += 1
        score += max(cnt.values()) - min(cnt.values())
        
      return score
    
    score = 0
    for i in range(n-1):
      score += get_sum(i)
      
    return score
  