'''
390. Elimination Game

You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:

Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
Given the integer n, return the last number that remains in arr.

Example 1:

Input: n = 9
Output: 6
Explanation:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]
Example 2:

Input: n = 1
Output: 1

Constraints:

1 <= n <= 10^9
'''

class Solution:
  '''
  this is a math problem: we only care about what's the first number of the 
  filtered array; if we're at even steps (i.e. 0, 2, 4, 6 ...) or if the
  length of the array is odd, then the first number in the source array will
  be filtered out, so we move the head number with the diff to the new value;
  then rinse and repeat. 
  '''
  def lastRemaining(self, n: int) -> int:
    head = 1
    diff = 1
    ln = n
    odd_step = False
    
    while ln > 1:
      if not odd_step or ln%2 == 1:
        head += diff
        
      odd_step = not odd_step
      ln //= 2
      diff <<= 1
      
    return head
  