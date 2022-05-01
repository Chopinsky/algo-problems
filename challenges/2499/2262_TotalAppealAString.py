'''
The appeal of a string is the number of distinct characters found in the string.

For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.
Given a string s, return the total appeal of all of its substrings.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "abbca"
Output: 28
Explanation: The following are the substrings of "abbca":
- Substrings of length 1: "a", "b", "b", "c", "a" have an appeal of 1, 1, 1, 1, and 1 respectively. The sum is 5.
- Substrings of length 2: "ab", "bb", "bc", "ca" have an appeal of 2, 1, 2, and 2 respectively. The sum is 7.
- Substrings of length 3: "abb", "bbc", "bca" have an appeal of 2, 2, and 3 respectively. The sum is 7.
- Substrings of length 4: "abbc", "bbca" have an appeal of 3 and 3 respectively. The sum is 6.
- Substrings of length 5: "abbca" has an appeal of 3. The sum is 3.
The total sum is 5 + 7 + 7 + 6 + 3 = 28.
Example 2:

Input: s = "code"
Output: 20
Explanation: The following are the substrings of "code":
- Substrings of length 1: "c", "o", "d", "e" have an appeal of 1, 1, 1, and 1 respectively. The sum is 4.
- Substrings of length 2: "co", "od", "de" have an appeal of 2, 2, and 2 respectively. The sum is 6.
- Substrings of length 3: "cod", "ode" have an appeal of 3 and 3 respectively. The sum is 6.
- Substrings of length 4: "code" has an appeal of 4. The sum is 4.
The total sum is 4 + 6 + 6 + 4 = 20.

Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
'''

from collections import defaultdict
from functools import lru_cache


class Solution:
  '''
  the problem is asking for all characters that appears in the string, count the
  number of substrings each character has appeared in. e.g., for `abbca`, `a` appears
  in 9 substrings, `b` appears in 11 substrings, and `c` appears in 8, so the total score
  is 9 + 11 + 8 = 28
  '''
  def appealSum(self, s: str) -> int:
    pos = defaultdict(list)
    for i, ch in enumerate(s):
      pos[ch].append(i)
      
    # count number of substrings that have a total
    # length of `ln`
    @lru_cache(None)
    def count(ln: int) -> int:
      if ln <= 0:
        return 0
      
      return ln + ln*(ln-1)//2
    
    n = len(s)
    total = count(n)
    scores = 0
    # print(pos, total)
    
    # iterate over all characters, find out number of substrings
    # that have this character in -- by removing substrings that
    # don't have this character in from all possible substrings
    for p in pos.values():
      # count of all possible substrings
      s0 = total
      
      # iterate over all positions of the char, and add number of
      # substrings between 2 neighboring chars
      for i in range(len(p)):
        pc = p[i] - (p[i-1] if i > 0 else -1) - 1
        s0 -= count(pc)
        
      # also count the substrings in the tail portion
      pc = n - p[-1] - 1
      s0 -= count(pc)
      
      # add the count of the substrings that contains this char to
      # the final score
      scores += s0

    return scores
    