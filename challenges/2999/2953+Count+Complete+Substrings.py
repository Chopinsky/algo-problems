'''
2953. Count Complete Substrings

You are given a string word and an integer k.

A substring s of word is complete if:

Each character in s occurs exactly k times.
The difference between two adjacent characters is at most 2. That is, for any two adjacent characters c1 and c2 in s, the absolute difference in their positions in the alphabet is at most 2.
Return the number of complete substrings of word.

A substring is a non-empty contiguous sequence of characters in a string.

Example 1:

Input: word = "igigee", k = 2
Output: 3
Explanation: The complete substrings where each character appears exactly twice and the difference between adjacent characters is at most 2 are: igigee, igigee, igigee.
Example 2:

Input: word = "aaabbbccc", k = 3
Output: 6
Explanation: The complete substrings where each character appears exactly three times and the difference between adjacent characters is at most 2 are: aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc.

Constraints:

1 <= word.length <= 10^5
word consists only of lowercase English letters.
1 <= k <= word.length
'''

from collections import defaultdict


class Solution:
  def countCompleteSubstrings(self, word: str, k: int) -> int:
    i, j = 0, 1
    n = len(word)
    total = 0
    
    def get_count(cc: int) -> int:
      if n == 1:
        return 1 if cc == 1 else 0
      
      i, j = 0, 1
      ln = cc*k
      
      d = defaultdict(int)
      d[word[0]] += 1
      cnt = 0
      
      while j < n:
        while j < n and j-i < ln:
          ch = word[j]
          last = word[j-1]
          
          if abs(ord(ch)-ord(last)) > 2:
            i = j
            d.clear()
            d[ch] = 1
          else:
            d[ch] += 1
            
          j += 1
          
        # if cc == 1:
        #   print('window:', (i, j), d)
          
        if j-i == ln and len(d) == cc and all(v == k for v in d.values()):
          cnt += 1
        
        popped = word[i]
        d[popped] -= 1
        if d[popped] == 0:
          del d[popped]
          
        i += 1
      
      # print('calc:', cc, ln, cnt)
      
      return cnt
      
    for c0 in range(1, 27):
      if c0*k > n:
        break
        
      total += get_count(c0)
    
    return total
    