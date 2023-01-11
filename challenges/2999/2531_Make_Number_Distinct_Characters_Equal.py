'''
2531. Make Number of Distinct Characters Equal

You are given two 0-indexed strings word1 and word2.

A move consists of choosing two indices i and j such that 0 <= i < word1.length and 0 <= j < word2.length and swapping word1[i] with word2[j].

Return true if it is possible to get the number of distinct characters in word1 and word2 to be equal with exactly one move. Return false otherwise.

Example 1:

Input: word1 = "ac", word2 = "b"
Output: false
Explanation: Any pair of swaps would yield two distinct characters in the first string, and one in the second string.
Example 2:

Input: word1 = "abcc", word2 = "aab"
Output: true
Explanation: We swap index 2 of the first string with index 0 of the second string. The resulting strings are word1 = "abac" and word2 = "cab", which both have 3 distinct characters.
Example 3:

Input: word1 = "abcde", word2 = "fghij"
Output: true
Explanation: Both resulting strings will have 5 distinct characters, regardless of which indices we swap.

Constraints:

1 <= word1.length, word2.length <= 10^5
word1 and word2 consist of only lowercase English letters.
'''

from collections import Counter


class Solution:
  def isItPossible(self, word1: str, word2: str) -> bool:
    c1, c2 = Counter(word1), Counter(word2)
    # print(c1, c2)
    
    for ch1 in c1:
      for ch2 in c2:
        n1, n2 = c1.copy(), c2.copy()
        
        n1[ch1] -= 1
        n1[ch2] = n1.get(ch2, 0) + 1

        n2[ch2] -= 1
        n2[ch1] = n2.get(ch1, 0) + 1
        
        if n1[ch1] == 0:
          del n1[ch1]
          
        if n2[ch2] == 0:
          del n2[ch2]
          
        if len(n1) == len(n2):
          return True
        
    return False
    