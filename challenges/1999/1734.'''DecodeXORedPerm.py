'''
There is an integer array perm that is a permutation of the first n positive integers, where n is always odd.

It was encoded into another integer array encoded of length n - 1, such that encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then encoded = [2,1].

Given the encoded array, return the original array perm. It is guaranteed that the answer exists and is unique.

Example 1:

Input: encoded = [3,1]
Output: [1,2,3]
Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
Example 2:

Input: encoded = [6,5,4,6]
Output: [2,4,1,5,3]
 

Constraints:

3 <= n < 10^5
n is odd.
encoded.length == n - 1
'''


from typing import List


class Solution:
  def decode(self, encoded: List[int]) -> List[int]:
    perm = []
    n = len(encoded)+1
    
    xor_sum = 1
    for i in range(2, n+1):
      xor_sum ^= i
      
    # print('before', xor_sum, n)
      
    for i in range(1, n, 2):
      xor_sum ^= encoded[i]
      
    # print(xor_sum)
    perm.append(xor_sum)
    for i in range(1, n):
      perm.append(perm[-1] ^ encoded[i-1])
      
    return perm
  