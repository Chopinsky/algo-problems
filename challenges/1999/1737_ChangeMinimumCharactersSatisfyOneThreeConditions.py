'''
You are given two strings a and b that consist of lowercase letters. In one operation, you can change any character in a or b to any lowercase letter.

Your goal is to satisfy one of the following three conditions:

Every letter in a is strictly less than every letter in b in the alphabet.
Every letter in b is strictly less than every letter in a in the alphabet.
Both a and b consist of only one distinct letter.
Return the minimum number of operations needed to achieve your goal.

Example 1:

Input: a = "aba", b = "caa"
Output: 2
Explanation: Consider the best way to make each condition true:
1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b is less than every letter in a.
3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
The best way was done in 2 operations (either condition 1 or condition 3).
Example 2:

Input: a = "dabadd", b = "cda"
Output: 3
Explanation: The best way is to make condition 1 true by changing b to "eee".

Constraints:

1 <= a.length, b.length <= 10^5
a and b consist only of lowercase letters.
'''


class Solution:
  def minCharacters(self, a: str, b: str) -> int:
    m, n = len(a), len(b)
    ca, cb = [0]*26, [0]*26
    
    for i in range(m):
      ia = ord(a[i]) - ord('a')
      ca[ia] += 1
      
    for i in range(n):
      ib = ord(b[i]) - ord('a')
      cb[ib] += 1
      
    # print(ca, cb)
    least_moves = m+n
    
    for i in range(26):
      if i < 25:
        # a is less
        ma = sum(ca[i+1:])
        mb = sum(cb[:i+1])
        # print(i, 'a less', ma, mb)
        least_moves = min(least_moves, ma+mb)
      
      # b is less
      if i > 0:
        ma = sum(ca[:i])
        mb = sum(cb[i:])
        # print(i, 'b less', ma, mb)
        least_moves = min(least_moves, ma+mb)
      
      # same char
      ma = sum(ca[:i]) + sum(ca[i+1:])
      mb = sum(cb[:i]) + sum(cb[i+1:])
      # print(i, 'equal', ma, mb)
      least_moves = min(least_moves, ma+mb)
    
    return least_moves
    