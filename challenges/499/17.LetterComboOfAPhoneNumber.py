'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

from typing import List


class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    if len(digits) == 0:
      return []
    
    stack, nxt = [""], []
    chars = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]    
    
    for d in digits:
      nxt.clear()
      for ch in chars[int(d)]:
        for s in stack:
          nxt.append(s + ch)
          
      stack, nxt = nxt, stack
    
    return stack
        

  def letterCombinations(self, digits: str) -> List[str]:
    ans = []
    keys = {
      '2': ['a', 'b', 'c'],
      '3': ['d', 'e', 'f'],
      '4': ['g', 'h', 'i'],
      '5': ['j', 'k', 'l'],
      '6': ['m', 'n', 'o'],
      '7': ['p', 'q', 'r', 's'],
      '8': ['t', 'u', 'v'],
      '9': ['w', 'x', 'y', 'z'],
    }

    for i in range(len(digits)):
      key = keys[digits[i]]

      if i == 0:
        ans = key
        continue

      tmp = []
      for j in range(len(ans)):
        for k in range(len(key)):
          tmp.append(ans[j] + key[k])

      # print(digits[i])

      ans = tmp

    return ans
