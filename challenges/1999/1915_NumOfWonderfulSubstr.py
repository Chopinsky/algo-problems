'''
A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"
Example 2:

Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"
Example 3:

Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"
 

Constraints:

1 <= word.length <= 10^5
word consists of lowercase English letters from 'a' to 'j'.
'''


from collections import defaultdict


class Solution:
  def wonderfulSubstrings(self, word: str) -> int:
    cnt = [0] * 10
    masks = defaultdict(int)
    masks[0] = 1
    seen = set()
    mask = 0
    total = 0
    
    for j, ch in enumerate(word):
      cnt[ch] = 1 - cnt[ch]
      idx = ord(ch) - ord('a')
      
      if ((1<<idx) & mask > 0) and (cnt[ch] == 0):
        mask ^= (1 << idx)
        
      elif ((1<<idx) & mask == 0) and (cnt[ch] == 1):
        mask |= (1 << idx)
        
      # 0 odd number of letters
      total += masks[mask]
      # one_cnt = 0
      seen.add(idx)
      
      # print(word[:j+1], mask, format(mask, '#12b'))
      # print(1, masks[mask])
      
      # 1 odd number of letters
      for i in range(10):
        # one_cnt += (mask >> i) & 1
        if i not in seen:
          continue
          
        tgt = mask ^ (1<<i)
        total += masks[tgt]
        # print(2, i, tgt, masks[tgt])
        
      masks[mask] += 1
      
    return total
    