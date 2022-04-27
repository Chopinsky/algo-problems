'''
You are given two strings s and t. In one step, you can append any character to either s or t.

Return the minimum number of steps to make s and t anagrams of each other.

An anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "leetcode", t = "coats"
Output: 7
Explanation: 
- In 2 steps, we can append the letters in "as" onto s = "leetcode", forming s = "leetcodeas".
- In 5 steps, we can append the letters in "leede" onto t = "coats", forming t = "coatsleede".
"leetcodeas" and "coatsleede" are now anagrams of each other.
We used a total of 2 + 5 = 7 steps.
It can be shown that there is no way to make them anagrams of each other with less than 7 steps.
Example 2:

Input: s = "night", t = "thing"
Output: 0
Explanation: The given strings are already anagrams of each other. Thus, we do not need any further steps.
 

Constraints:

1 <= s.length, t.length <= 2 * 10^5
s and t consist of lowercase English letters.
'''

from typing import List


class Solution:
  def minSteps(self, s: str, t: str) -> int:
    c1, c2 = Counter(s), Counter(t)
    cnt = 0
    
    for ch in set(c1)|set(c2):
      cnt1, cnt2 = c1.get(ch, 0), c2.get(ch, 0)
      c = max(cnt1, cnt2)
      cnt += (c-cnt1) + (c-cnt2)
      
    return cnt
    