'''
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
'''


class Solution:
  def maxLength(self, arr: List[str]) -> int:
    n = len(arr)
    data = [[0, 0] for _ in range(n)]
    
    def build(i: int):
      oa = ord('a')
      for ch in arr[i]:
        idx = 1 << (ord(ch) - oa)
        if not idx & data[i][0]:
          data[i][0] |= idx
          data[i][1] += 1
        else:
          data[i][0] = 0
          data[i][1] = 0
          break
    
    for i in range(n):
      build(i)
    
    cache = {}
    # print(data)
    
    def check(base: int, i: int) -> int:
      nonlocal n
      
      if i >= n:
        return 0
      
      if (base, i) in cache:
        return cache[base, i]
      
      best = 0
      if not base & data[i][0]:
        best = data[i][1] + check(base|data[i][0], i+1)
      
      best = max(best, check(base, i+1))
      cache[base, i] = best
      
      return best
    
    return check(0, 0)
    
