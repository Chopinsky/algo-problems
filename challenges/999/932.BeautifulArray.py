'''
For some fixed n, an array nums is beautiful if it is a permutation of the integers 1, 2, ..., n, such that:

For every i < j, there is no k with i < k < j such that nums[k] * 2 = nums[i] + nums[j].

Given n, return any beautiful array nums.  (It is guaranteed that one exists.)

Example 1:

Input: n = 4
Output: [2,1,4,3]
Example 2:

Input: n = 5
Output: [3,1,2,5,4]

Note:

1 <= n <= 1000
'''


from typing import List


class Solution:
  '''
  idea is that to an array where the diff between neighboring elements is the same
  (i.e. 等差数列), 2*n[i] = n[i-1] + n[i+1], so we divide them into 2 different arrays:
  odds array where index is odd, and evens array where index is even; we keep doing 
  the split, until we have less than 3 elements in the array, which is beautiful array
  itself, then recombine all these smaller arrays into the final result.
  '''
  def beautifulArray(self, n: int) -> List[int]:
    arr = [i for i in range(1, n+1)]
    
    def split(l: List[int]) -> List[int]:
      if len(l) < 3:
        return l
      
      even = l[::2]
      odd = l[1::2]
      
      return split(even) + split(odd)
    
    return split(arr)
  
    
  def beautifulArray1(self, n: int) -> List[int]:
    d = { 1: [1] }
    
    def partial(num: int) -> List[int]:
      if num not in d:
        odd = partial((num+1)//2)
        even = partial(num//2)
        ans = [2*i-1 for i in odd] + [2*i for i in even]
        d[num] = ans
        
      return d[num]
    
    return partial(n)
  