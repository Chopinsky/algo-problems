'''
You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.

Return the rearranged number with minimal value.

Note that the sign of the number does not change after rearranging the digits.

Example 1:

Input: num = 310
Output: 103
Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 
The arrangement with the smallest value that does not contain any leading zeros is 103.
Example 2:

Input: num = -7605
Output: -7650
Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
The arrangement with the smallest value that does not contain any leading zeros is -7650.

Constraints:

-10^15 <= num <= 10^15
'''

class Solution:
  def smallestNumber(self, num: int) -> int:
    if num == 0:
      return num
    
    arr = list(str(num))
    if num < 0:
      arr = arr[1:]
      return -1 * int(''.join(sorted(arr, reverse=True)))
      
    arr.sort()
    idx = 0
    
    while idx < len(arr) and arr[idx] == '0':
      idx += 1
      
    if idx > 0:
      arr[0], arr[idx] = arr[idx], arr[0]
    
    return int(''.join(arr))
  