'''
1888. Minimum Number of Flips to Make the Binary String Alternating

You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.
Example 3:

Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".

Constraints:

1 <= s.length <= 10^5
s[i] is either '0' or '1'.
'''

class Solution:
  '''
  the problem is tricky: 
  1)  the end state will be one of the 2 cases: '0' in even slots and '1' in 
      odd slots, or vice versa; so the type-2 operation is to either flip all even 
      slots to '0' and all odd slots to '1', or vice versa; 
  
  2)  then type-1 operation will change the odd/even counters if n % 2 == 1, because
      in that case, character @ index-0 will be moved to index-(n-1), which is still an
      even number, hence the counters could change: we have to loop through the string
      again, and update the odd/even counters accordingly.
  '''
  def minFlips(self, s: str) -> int:
    n = len(s)
    if n <= 1:
      return 0
    
    if n == 2:
      return 1 if s[0] == s[1] else 0
    
    odd_count = 0
    odd_zeros, even_ones = 0, 0
    
    for i in range(n):
      odd_count += (i % 2)
      if i % 2 == 1 and s[i] == '0':
        odd_zeros += 1
        
      if i % 2 == 0 and s[i] == '1':
        even_ones += 1
      
    even_count = n - odd_count
    even_zeros = even_count - even_ones
    odd_ones = odd_count - odd_zeros
    min_ops = min((n-odd_zeros-even_ones), (n-odd_ones-even_zeros))
    
    if n % 2 == 0:
      return min_ops
    
    # keep rotating
    for i in range(n):
      # swapping counters as we apply type-1 operation, which will alter the even/odd 
      # counters
      even_zeros, odd_ones, odd_zeros, even_ones = odd_zeros, even_ones, even_zeros, odd_ones
      
      # this char will remain at an even position, update counters
      if s[i] == '0':
        odd_zeros -= 1
        even_zeros += 1
        
      else:
        odd_ones -= 1
        even_ones += 1
        
      min_ops = min(min_ops, (n-odd_zeros-even_ones), (n-odd_ones-even_zeros))
    
    return min_ops
  