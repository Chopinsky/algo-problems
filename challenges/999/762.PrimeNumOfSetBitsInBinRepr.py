'''
Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

Recall that the number of set bits an integer has is the number of 1's present when written in binary.

For example, 21 written in binary is 10101, which has 3 set bits.

Example 1:

Input: left = 6, right = 10
Output: 4
Explanation:
6  -> 110 (2 set bits, 2 is prime)
7  -> 111 (3 set bits, 3 is prime)
8  -> 1000 (1 set bit, 1 is not prime)
9  -> 1001 (2 set bits, 2 is prime)
10 -> 1010 (2 set bits, 2 is prime)
4 numbers have a prime number of set bits.
Example 2:

Input: left = 10, right = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
5 numbers have a prime number of set bits.
 

Constraints:

1 <= left <= right <= 10^6
0 <= right - left <= 10^4
'''

from math import comb


primes = set([2, 3, 5, 7, 11, 13, 17, 19])

class Solution:
  # this solution can handle 1 <= left <= right <= 2^31-1
  def countPrimeSetBits(self, left: int, right: int) -> int:
    def calc(slot: int, pre: int) -> int:
      cnt = 0
      if slot == 0:
        return 1 if pre in primes else 0

      for i in range(slot+1):
        if i+pre in primes:
          cnt += comb(slot, i)

      return cnt

    def count(val: int) -> int:
      if val <= 2:
        return 0

      bval = bin(val)[2:]
      slot = len(bval)-1
      cnt = 0 # count of 1s set in the previous spots (except the current spot)
      res = 1 if bval.count('1') in primes else 0

      while slot >= 0:
        mask = 1 << slot

        # can set 1s in the lower slots with current spot to be 0
        if mask&val > 0:
          res += calc(slot, cnt)
          cnt += 1 # update prev 1s count

        slot -= 1

      # print('count:', val, res)
      return res

    return count(right) - count(left-1)
        
  def countPrimeSetBits(self, left: int, right: int) -> int:
    count = 0
    
    for val in range(left, right+1):
      cnt = 0
      while val > 0:
        if val&1 > 0:
          cnt += 1
          
        val >>= 1
        
      if cnt in primes:
        count += 1
        
    return count
  