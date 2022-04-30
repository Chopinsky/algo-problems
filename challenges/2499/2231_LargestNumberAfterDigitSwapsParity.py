'''
You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.

Example 1:

Input: num = 1234
Output: 3412
Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.
Example 2:

Input: num = 65875
Output: 87655
Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.

Constraints:

1 <= num <= 10^9
'''


class Solution:
  def largestInteger(self, num: int) -> int:
    odd_idx = []
    odd_vals = []
    even_idx = []
    even_vals = []
    
    for i, ch in enumerate(str(num)):
      if int(ch) % 2 == 0:
        even_idx.append(i)
        even_vals.append(int(ch))
      else:
        odd_idx.append(i)
        odd_vals.append(int(ch))
        
    odd_vals.sort(reverse=True)
    even_vals.sort(reverse=True)
    ans = 0
    i, j = 0, 0
    
    while i < len(odd_idx) or j < len(even_idx):
      if i >= len(odd_idx):
        ans = 10*ans + even_vals[j]
        j += 1
        continue
        
      if j >= len(even_idx):
        ans = 10*ans + odd_vals[i]
        i += 1
        continue
        
      if odd_idx[i] < even_idx[j]:
        val = odd_vals[i]
        i += 1
      else:
        val = even_vals[j]
        j += 1
      
      ans = 10*ans + val
      
    return ans
    
      