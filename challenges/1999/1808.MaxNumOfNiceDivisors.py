'''
You are given a positive integer primeFactors. You are asked to construct a positive integer n that satisfies the following conditions:

The number of prime factors of n (not necessarily distinct) is at most primeFactors.
The number of nice divisors of n is maximized. Note that a divisor of n is nice if it is divisible by every prime factor of n. For example, if n = 12, then its prime factors are [2,2,3], then 6 and 12 are nice divisors, while 3 and 4 are not.
Return the number of nice divisors of n. Since that number can be too large, return it modulo 109 + 7.

Note that a prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. The prime factors of a number n is a list of prime numbers such that their product equals n.

Example 1:

Input: primeFactors = 5
Output: 6
Explanation: 200 is a valid value of n.
It has 5 prime factors: [2,2,2,5,5], and it has 6 nice divisors: [10,20,40,50,100,200].
There is not other value of n that has at most 5 prime factors and more nice divisors.

Example 2:

Input: primeFactors = 8
Output: 18

Constraints:

1 <= primeFactors <= 10^9
'''


from bisect import bisect_right


class Solution:
  '''
  the idea is that the optimal solution is actually [a,a,b,b,b,c,c,c, ... ,d,d,d], where a, b, c,
  and d are prime numbers; we just need the length of the sequence to be n, and product of the number
  of each prime number (i.e. a, b, c, d, etc.) to be maximum.

  the trick is that 
  '''
  def maxNiceDivisors(self, n: int) -> int:
    mod = 1_000_000_007
    base = 1
    prod = 3
    x = 3
    trace = [(3, 3)]
    
    while x+x+1 < n:
      prod = (prod * prod) % mod
      x += x
      trace.append((x, prod))
      
      n -= x
      base *= prod
    
    # print(n, base, trace)
    
    while n > 4:
      idx = bisect_right(trace, (n, )) - 1
      if idx >= 0 and n-trace[idx][0] == 1:
        idx -= 1
        
      if idx < 0:
        break
        
      # print('reduce:', n, idx, trace[idx])
      base = (base * trace[idx][1]) % mod
      n -= trace[idx][0]
    
    # print('post', n, base)
    while n > 4:
      base = (3 * base) % mod
      n -= 3
      
    return (base * (n if n > 1 else 1)) % mod
  