'''
1946. Largest Number After Mutating Substring

You are given a string num, which represents a large integer. You are also given a 0-indexed integer array change of length 10 that maps each digit 0-9 to another digit. More formally, digit d maps to digit change[d].

You may choose to mutate a single substring of num. To mutate a substring, replace each digit num[i] with the digit it maps to in change (i.e. replace num[i] with change[num[i]]).

Return a string representing the largest possible integer after mutating (or choosing not to) a single substring of num.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: num = "132", change = [9,8,5,0,3,6,4,2,6,8]
Output: "832"
Explanation: Replace the substring "1":
- 1 maps to change[1] = 8.
Thus, "132" becomes "832".
"832" is the largest number that can be created, so return it.
Example 2:

Input: num = "021", change = [9,4,3,5,7,2,1,9,0,6]
Output: "934"
Explanation: Replace the substring "021":
- 0 maps to change[0] = 9.
- 2 maps to change[2] = 3.
- 1 maps to change[1] = 4.
Thus, "021" becomes "934".
"934" is the largest number that can be created, so return it.
Example 3:

Input: num = "5", change = [1,4,7,5,3,2,5,6,9,4]
Output: "5"
Explanation: "5" is already the largest number that can be created, so return it.

Constraints:

1 <= num.length <= 10^5
num consists of only digits 0-9.
change.length == 10
0 <= change[d] <= 9
'''

from typing import List

testCases = [
  ["132", [9,8,5,0,3,6,4,2,6,8]],
  ["021", [9,4,3,5,7,2,1,9,0,6]],
  ["5", [1,4,7,5,3,2,5,6,9,4]],
  ["334111", [0,9,2,3,3,2,5,5,5,5]],
  ["7218518888806706540", [5,1,5,3,1,9,5,2,0,5]],
]

class Solution:
  def maximumNumber(self, num: str, change: List[int]) -> str:
    c = {str(i):str(change[i]) for i in range(len(change)) if change[i] >= i}
    d = list(num)
    state = 0
    updated = False
    # print('init:', c)
    
    for i in range(len(num)):
      d0 = str(d[i])
      # print('iter:', d0, state)
      
      if state == 2:
        break
        
      if state == 0 and d0 in c:
        state = 1
          
      if state == 1:
        if d0 in c:
          d[i] = c[d0]
          updated = updated or c[d0] != d0
        else:
          state = 2 if updated else 0
    
    return ''.join(d)
    