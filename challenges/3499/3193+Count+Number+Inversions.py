'''
3193. Count the Number of Inversions

You are given an integer n and a 2D array requirements, where requirements[i] = [endi, cnti] represents the end index and the inversion count of each requirement.

A pair of indices (i, j) from an integer array nums is called an inversion if:

i < j and nums[i] > nums[j]
Return the number of permutations perm of [0, 1, 2, ..., n - 1] such that for all requirements[i], perm[0..endi] has exactly cnti inversions.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, requirements = [[2,2],[0,0]]

Output: 2

Explanation:

The two permutations are:

[2, 0, 1]
Prefix [2, 0, 1] has inversions (0, 1) and (0, 2).
Prefix [2] has 0 inversions.
[1, 2, 0]
Prefix [1, 2, 0] has inversions (0, 2) and (1, 2).
Prefix [1] has 0 inversions.
Example 2:

Input: n = 3, requirements = [[2,2],[1,1],[0,0]]

Output: 1

Explanation:

The only satisfying permutation is [2, 0, 1]:

Prefix [2, 0, 1] has inversions (0, 1) and (0, 2).
Prefix [2, 0] has an inversion (0, 1).
Prefix [2] has 0 inversions.
Example 3:

Input: n = 2, requirements = [[0,0],[1,0]]

Output: 1

Explanation:

The only satisfying permutation is [0, 1]:

Prefix [0] has 0 inversions.
Prefix [0, 1] has an inversion (0, 1).
 
 

Constraints:

2 <= n <= 300
1 <= requirements.length <= n
requirements[i] = [endi, cnti]
0 <= endi <= n - 1
0 <= cnti <= 400
The input is generated such that there is at least one i such that endi == n - 1.
The input is generated such that all endi are unique.

Test cases:

3
[[2,2],[0,0]]
3
[[2,2],[1,1],[0,0]]
2
[[0,0],[1,0]]
5
[[0,0],[1,0],[4,6],[3,4]]
'''

from functools import lru_cache
from typing import List

class Solution:
  '''
  the idea is that we use dp(ln, pairs) to count all arrays that has a lenght of `ln` and `pairs` 
  of inversion number pairs; then the restraint is that if [requirements] also defines `ln`, then
  any dp(ln, pairs) are 0 except the `pairs == requirements[x]`; 

  the state transition is defined as:
    dp(ln, pairs) = sum(dp(ln-1, p0) for p0 in range(1+pairs))
  
  because for any valid array that has lenght of `ln-1` and `p0` pairs, we can append the new number
  `ln` to each of them, then shift it `pairs-p0` times to get the additional pairs, such that the total
  count of inversion pairs is `pairs`;

  the trick to avoid TLE is that we break the summation if `pairs-p0` is smaller than 0, meaning we
  can shift valid number `ln` a valid number of times to get the (ln, pairs) state;
  '''
  def numberOfPermutations(self, n: int, req: List[List[int]]) -> int:
    mod = 10**9+7
    r = {i+1:c for i, c in req}
    # print('init:', r)
    # dv = -1
    
    @lru_cache(None)
    def dp(l: int, inv: int):
      if l <= 0:
        # if l == dv:
        #   print('exit 1')
          
        return 0
      
      if l in r and r[l] != inv:
        # if l == dv:
        #   print('exit 2:', (l, inv))
          
        return 0
      
      max_inv = l*(l-1)//2
      if inv > max_inv:
        # if l == dv:
        #   print('exit 3:', (max_inv, inv))
          
        return 0
      
      if l == 1:
        # if l == dv:
        #   print('exit 4')
          
        return 1 if inv == 0 else 0
      
      total = 0
      for nxt_inv in range(inv, -1, -1):
        if nxt_inv+l-1 < inv:
          break
        
        cnt = dp(l-1, nxt_inv)
        total = (total + cnt) % mod
        # if l == dv:
        #   print("iter:", (inv, nxt_inv), cnt)
        
      return total
    
    return dp(n, r[n])
        