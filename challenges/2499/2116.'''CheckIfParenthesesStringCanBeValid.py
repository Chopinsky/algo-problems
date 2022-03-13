'''
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.

Example 1:


Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
Example 2:

Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.
Example 3:

Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.
 

Constraints:

n == s.length == locked.length
1 <= n <= 10^5
s[i] is either '(' or ')'.
locked[i] is either '0' or '1'.
'''


class Solution:
  def canBeValid(self, s: str, locked: str) -> bool:
    opened = []
    free = []

    for i in range(len(s)):
      # a free char, open for flips
      if locked[i] == '0':
        free.append(i)
        continue

      # a locked char
      if locked[i] == '1':
        # an open, push to the stack
        if s[i] == '(':
          opened.append(i)
          continue

        # a close, take the right-most open
        # one first if possible
        if opened:
          opened.pop()
          continue

        # a close, take the right-most free
        # one if possible
        if free:
          free.pop()
          continue

        # not gonna make it
        return False

    # match with free ones from the right side
    for pos in reversed(opened):
      if free and free[-1] > pos:
        free.pop()
        continue

      return False

    return len(free) % 2 == 0


  def canBeValid0(self, s: str, locked: str) -> bool:
    n = len(s)
    if n % 2 == 1:
      return False
    
    # forward checking: if too many fixed open in
    # s[i:]
    free, opened, closed = 0, 0, 0
    for i in range(n-1, -1, -1):
      if locked[i] == '0':
        free += 1
      elif s[i] == '(':
        opened += 1
      else:
        closed += 1
        
      if free + (closed - opened) < 0:
        return False
      
    # backward checking: if too many fixed close in
    # s[:i+1]
    free, opened, closed = 0, 0, 0
    for i in range(n):
      if locked[i] == '0':
        free += 1
      elif s[i] == '(':
        opened += 1
      else:
        closed += 1
        
      if free + (opened - closed) < 0:
        return False
      
    return True
    