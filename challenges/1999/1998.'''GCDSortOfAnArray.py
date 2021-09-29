'''
You are given an integer array nums, and you can perform the following 
operation any number of times on nums:

Swap the positions of two elements nums[i] and nums[j] if gcd(nums[i], nums[j]) > 1 where gcd(nums[i], nums[j]) is the greatest common divisor of nums[i] and nums[j].
Return true if it is possible to sort nums in non-decreasing order using the above swap method, or false otherwise.

Example 1:

Input: nums = [7,21,3]
Output: true
Explanation: We can sort [7,21,3] by performing the following operations:
- Swap 7 and 21 because gcd(7,21) = 7. nums = [21,7,3]
- Swap 21 and 3 because gcd(21,3) = 3. nums = [3,7,21]

Example 2:

Input: nums = [5,2,6,2]
Output: false
Explanation: It is impossible to sort the array because 5 cannot be swapped with any other element.

Example 3:

Input: nums = [10,5,9,3,15]
Output: true
We can sort [10,5,9,3,15] by performing the following operations:
- Swap 10 and 15 because gcd(10,15) = 5. nums = [15,5,9,3,10]
- Swap 15 and 3 because gcd(15,3) = 3. nums = [3,5,9,15,10]
- Swap 10 and 15 because gcd(10,15) = 5. nums = [3,5,9,10,15]

Constraints:

1 <= nums.length <= 3 * 10 ** 4
2 <= nums[i] <= 10 ** 5
'''


from typing import List


class Solution:
  def gcdSort(self, nums: List[int]) -> bool:
    top = max(nums)
    roots = [i for i in range(top+1)]
    
    # find the root num
    def find(i: int) -> int:
      while roots[i] != i:
        i = roots[i]
        
      return i
    
    # union nums
    def union(i: int, j: int):
      ii, jj = find(i), find(j)
      if ii == jj:
        return
      
      if ii < jj:
        roots[jj] = ii
        return
      
      roots[ii] = jj
      return
    
    # create a sieve
    def get_sieve(n: int) -> List[int]:
      s = [i for i in range(n)]
      for i in range(2, n):
        # not a prime factor
        if s[i] != i:
          continue
          
        for j in range(i*i, n, i):
          if s[j] > i:
            s[j] = i
          
      return s
    
    # get prime factors of number `n`
    def prime_factors(n: int, s: List[int]):
      while n > 1:
        yield s[n]
        n //= s[n]
    
    sieves = get_sieve(top+1)
    
    # connect all prime factor numbers into the same
    # group, this will effectively connecting all numbers
    # from the `nums` array that belong to the same group
    for n in set(nums):
      for f in prime_factors(n, sieves):
        union(f, n)
        
    # check if the number in the desired position can be
    # swapped with the number from the original array,
    # and only 2 numbers in the same group can be swapped.
    base = sorted(nums)
    for i in range(len(nums)):
      if find(nums[i]) != find(base[i]):
        return False
    
    return True
  