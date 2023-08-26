'''
1053. Previous Permutation With One Swap

Given an array of positive integers arr (not necessarily distinct), return the lexicographically largest permutation that is smaller than arr, that can be made with exactly one swap. If it cannot be done, then return the same array.

Note that a swap exchanges the positions of two numbers arr[i] and arr[j]

Example 1:

Input: arr = [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.
Example 2:

Input: arr = [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.
Example 3:

Input: arr = [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^4
'''

from typing import List


class Solution:
  '''
  find the first number that's larger than its right number, and the second number should
  be the largest number that's smaller than the first number but the largest among the smallest
  numbers to the right of the first number
  '''
  def prevPermOpt1(self, arr: List[int]) -> List[int]:
    i = len(arr)-2
    
    while i >= 0 and arr[i] <= arr[i+1]:
      i -= 1
        
    if i >= 0:
      max_idx = i + 1
      
			# max number greater on right that less than arr[i]
      for j in range(max_idx+1, len(arr)):
        if arr[max_idx] < arr[j] < arr[i]:
          max_idx = j
          
      arr[max_idx], arr[i] = arr[i], arr[max_idx]
      
    return arr