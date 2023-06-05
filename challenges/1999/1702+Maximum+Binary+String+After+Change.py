'''
1702. Maximum Binary String After Change

You are given a binary string binary consisting of only 0's or 1's. You can apply each of the following operations any number of times:

Operation 1: If the number contains the substring "00", you can replace it with "10".
For example, "00010" -> "10010"
Operation 2: If the number contains the substring "10", you can replace it with "01".
For example, "00010" -> "00001"
Return the maximum binary string you can obtain after any number of operations. Binary string x is greater than binary string y if x's decimal representation is greater than y's decimal representation.

Example 1:

Input: binary = "000110"
Output: "111011"
Explanation: A valid transformation sequence can be:
"000110" -> "000101" 
"000101" -> "100101" 
"100101" -> "110101" 
"110101" -> "110011" 
"110011" -> "111011"
Example 2:

Input: binary = "01"
Output: "01"
Explanation: "01" cannot be transformed any further.

Constraints:

1 <= binary.length <= 10^5
binary consist of '0' and '1'.
'''


class Solution:
  """
  the trick is we have at most one '0' in the final answer: we
  shift a '0' forward to the frontmost '0' to form a '00' -> '10',
  then we find the next '0' and shift it forward to the tail '0' of
  the '10' substring we generated in the last step, and keep repeating
  the process; this is equivalent to shift the left-most '0' by 1 position 
  to the right for each '0' to the right of it.
  """
  def maximumBinaryString(self, binary: str) -> str:
    n = len(binary)
    left = -1
    cnt = 0
    
    for i, b in enumerate(binary):
      if b == '0':
        cnt += 1
        if left < 0:
          left = i
    
    if cnt <= 1 or n == 1:
      return binary
    
    b_arr = list(binary)
    zero_pos = left + (cnt-1)
    
    for i in range(n):
      b_arr[i] = '0' if i == zero_pos else '1'
    
    return ''.join(b_arr)
  