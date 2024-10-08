'''
1813. Sentence Similarity III

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. For example, "Hello World", "HELLO", "hello world hello world" are all sentences. Words consist of only uppercase and lowercase English letters.

Two sentences sentence1 and sentence2 are similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. For example, sentence1 = "Hello my name is Jane" and sentence2 = "Hello Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in sentence2.

Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

Example 1:

Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".
Example 2:

Input: sentence1 = "of", sentence2 = "A lot of words"
Output: false
Explanation: No single sentence can be inserted inside one of the sentences to make it equal to the other.
Example 3:

Input: sentence1 = "Eating right now", sentence2 = "Eating"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.

Constraints:

1 <= sentence1.length, sentence2.length <= 100
sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
The words in sentence1 and sentence2 are separated by a single space.
'''

from typing import List


class Solution:
  def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
    def is_similar(a1: List, a2: List) -> bool:
      n1 = len(a1)
      n2 = len(a2)
      
      if n1 < n2:
        return False
      
      i1, j1 = 0, n1-1
      i2, j2 = 0, n2-1
      front = 0
      back = 0
      
      while i1 < n1 and i2 < n2 and a1[i1] == a2[i2]:
        i1 += 1
        i2 += 1
        front += 1
        
      while j1 >= 0 and j2 >= 0 and a1[j1] == a2[j2]:
        j1 -= 1
        j2 -= 1
        back += 1
        
      # print('check:', a1, a2)
      # print('idx:', (front, back))
      
      return front+back >= n2
      
    a1 = sentence1.split(' ')
    a2 = sentence2.split(' ')
    
    return is_similar(a1, a2) or is_similar(a2, a1)
    
  def areSentencesSimilar(self, s1: str, s2: str) -> bool:
    w1, w2 = s1.split(' '), s2.split(' ')
    n1, n2 = len(w1), len(w2)
    # print(w1, w2)
    
    if n1 == n2:
      return s1 == s2
    
    if n1 > n2:
      w1, w2 = w2, w1
      n1, n2 = n2, n1
      s1, s2 = s2, s1
      
    if s1.startswith(s2) or s1.endswith(s2):
      return True
    
    l1, r1 = 0, n1-1
    l2, r2 = 0, n2-1
    
    while l1 < n1 and l2 < n2:
      if w1[l1] != w2[l2]:
        break
      
      l1 += 1
      l2 += 1
      
    while r1 >= 0 and r2 >= 0:
      if w1[r1] != w2[r2]:
        break
        
      r1 -= 1
      r2 -= 1
      
    # print(l1, r1)
    return l1 > r1
        