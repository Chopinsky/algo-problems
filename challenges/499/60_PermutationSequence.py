'''
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!
'''

from math import factorial


class Solution:
  def getPermutation(self, n: int, k: int) -> str:
    nums = set([i for i in range(1, n+1)])
    val = ""
    
    for i in range(n, 0, -1):
      if i == 1:
        val += str(list(nums)[0])
        break
        
      if k == 1:
        val += ''.join([str(i) for i in sorted(nums)])
        break
        
      if k == factorial(i):
        val += ''.join([str(i) for i in sorted(nums, reverse=True)])
        break
        
      base = factorial(i-1)
      m = ((k-1) // base) + 1
      num_vals = sorted(nums)
      pop_val = num_vals[m-1]
      nums.discard(pop_val)
      
      val += str(pop_val)
      k -= (m-1) * base
    
    return val
  
    '''
    def perm(n: int, k: int) -> str:
      if n == 1:
        return str(list(nums)[0])
      
      if k == 1:
        return ''.join([str(i) for i in sorted(nums)])

      if k == factorial(n):
        return ''.join([str(i) for i in sorted(nums, reverse=True)])
      
      base = factorial(n-1)
      m = ((k-1) // base) + 1
      num_vals = sorted(nums)
      pop_val = num_vals[m-1]
      nums.discard(pop_val)
      # print(n, k, base, m, pop_val, nums)
      
      return str(pop_val) + perm(n-1, k-(m-1)*base)
    
    return perm(n, k)
    '''
  