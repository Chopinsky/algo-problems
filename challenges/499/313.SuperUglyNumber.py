'''
A super ugly number is a positive integer whose prime factors are in the array primes.

Given an integer n and an array of integers primes, return the nth super ugly number.

The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

Example 1:

Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].

Example 2:

Input: n = 1, primes = [2,3,5]
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].

Constraints:

1 <= n <= 106
1 <= primes.length <= 100
2 <= primes[i] <= 1000
primes[i] is guaranteed to be a prime number.
All the values of primes are unique and sorted in ascending order.
'''


from typing import List
from heapq import heapify, heappop, heappush


class Solution:
  def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
    if n <= 1:
      return 1
    
    ln = len(primes)
    ugly = 1
    dp = [1]
    vals = [1] * ln
    idx = [0] * ln
    
    for _ in range(1, n):
      for i in range(ln):
        if ugly == vals[i]:
          vals[i] = primes[i] * dp[idx[i]]
          idx[i] += 1
          
      ugly = min(vals)
      dp.append(ugly)
          
    return ugly
    
    
  def nthSuperUglyNumber1(self, n: int, primes: List[int]) -> int:
    if n <= 1:
      return 1

    num = 1
    count = 1
    ln = len(primes)
    top_val = primes[-1]
    
    stack = [(p, p, 0) for p in primes]
    heapify(stack)
    
    while count < n:
      val, base, i = heappop(stack)
      if val != num:
        count += 1
        
      num = val
      # print(num, count)
      
      if i < ln:
        nxt_val = base * primes[i]
        # if count + len(stack) > n and nxt_val > top_val:
        #   continue
        # top_val = max(top_val, nxt_val)
        
        heappush(stack, (nxt_val, base, i+1))
        heappush(stack, (nxt_val, nxt_val, 0))
      
    # print(num, len(stack))
    return num
    