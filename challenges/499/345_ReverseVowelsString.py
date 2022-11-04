'''
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"

Constraints:

1 <= s.length <= 3 * 10^5
s consist of printable ASCII characters.
'''


class Solution:
  def reverseVowels(self, s: str) -> str:
    cand = []
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    s = list(s)
    
    for i, ch in enumerate(s):
      if ch in vowels:
        cand.append(i)
      
    i, j = 0, len(cand)-1
    # print(cand)
    
    while i < j:
      s[cand[i]], s[cand[j]] = s[cand[j]], s[cand[i]]
      i += 1
      j -= 1
      
    # print(s)
    return ''.join(s)
      