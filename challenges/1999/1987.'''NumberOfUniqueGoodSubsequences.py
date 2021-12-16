'''
You are given a binary string binary. A subsequence of binary is considered good if it is not empty and has no leading zeros (with the exception of "0").

Find the number of unique good subsequences of binary.

For example, if binary = "001", then all the good subsequences are ["0", "0", "1"], so the unique good subsequences are "0" and "1". Note that subsequences "00", "01", and "001" are not good because they have leading zeros.
Return the number of unique good subsequences of binary. Since the answer may be very large, return it modulo 109 + 7.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: binary = "001"
Output: 2
Explanation: The good subsequences of binary are ["0", "0", "1"].
The unique good subsequences are "0" and "1".
Example 2:

Input: binary = "11"
Output: 2
Explanation: The good subsequences of binary are ["1", "1", "11"].
The unique good subsequences are "1" and "11".
Example 3:

Input: binary = "101"
Output: 5
Explanation: The good subsequences of binary are ["1", "0", "1", "10", "11", "101"]. 
The unique good subsequences are "0", "1", "10", "11", and "101".

Constraints:

1 <= binary.length <= 105
binary consists of only '0's and '1's.
'''


class Solution:
  def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
    mod = 1_000_000_007
    hasZero = 0
    oneCount = 0
    zeroCount = 0
    
    for char in binary:
      if char == '0':
        hasZero = 1
        zeroCount = (oneCount + zeroCount) % mod
      else:
        oneCount = (1 + oneCount + zeroCount) % mod

    return (hasZero + oneCount + zeroCount) % mod
      
      
  def numberOfUniqueGoodSubsequences0(self, binary: str) -> int:
    mod = 1_000_000_007
    n = len(binary)
    
    if n == 1:
      return 1
    
    if n == 2:
      if binary[0] == '0':
        return 1 if binary[1] == '0' else 2
      
      return 2 if binary[1] == '1' else 3
    
    if all(b == '1' for b in binary):
      return n
    
    if all(b == '0' for b in binary):
      return 1
    
    start = 0
    while start < n and binary[start] == '0':
      start += 1
      
    binary = binary[start:]
    # print('init', binary, n)
    
    total = 1
    acc0 = 0
    acc1 = 1
    zero = False
    
    for val in binary[1:]:
      if val == '1':
        acc0 = (acc0 + (acc1 if zero else 0)) % mod
        addition = acc1
        
      else:
        if not zero:
          acc0 = total
          zero = True
        
        acc1 = (acc1 + acc0) % mod
        addition = acc0
        
      total = (total + addition) % mod
      # print('after', val, (acc0, acc1), total)
      
    return total+1
    