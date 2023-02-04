'''
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''


class Solution:
  def isAlienSorted(self, words: List[str], order: str) -> bool:
    dic = {ch: idx for idx, ch in enumerate(order)}
    # print(dic)
    
    def is_correct_order(s1: str, s2: str) -> bool:
      idx = 0
      n1, n2 = len(s1), len(s2)
      
      while idx < n1 and idx < n2:
        rank1, rank2 = dic[s1[idx]], dic[s2[idx]]
        if rank1 > rank2:
          # print((s1[idx], rank1), (s2[idx], rank2))
          return False
        
        if rank1 < rank2:
          return True
        
        idx += 1
        
      return idx == n1
    
    for i in range(1, len(words)):
      if not is_correct_order(words[i-1], words[i]):
        # print(words[i-1], words[i])
        return False
      
    return True
    
    
  def isAlienSorted(self, words: List[str], order: str) -> bool:
    dict = {l: idx for idx, l in enumerate(order)}

    # print(dict)

    for i in range(1, len(words)):
      if not self.compare(words[i-1], words[i], dict):
        return False

      # print(words[i-1], words[i])

    return True

  def compare(self, a: str, b: str, dict) -> bool:
    lb = len(b)

    for i in range(0, len(a)):
      if i >= lb:
        return False

      ca = a[i]
      cb = b[i]

      if dict[ca] < dict[cb]:
        return True

      if dict[ca] > dict[cb]:
        # print("False:", ca, dict[ca], cb, dict[cb], i)
        return False

    return True
