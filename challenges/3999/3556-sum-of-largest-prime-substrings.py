'''
3556-sum-of-largest-prime-substrings
'''


top = 10**5+1
val = list(range(top))
p = list()

for v0 in range(2, top):
  if val[v0] < v0:
    continue

  p.append(v0)
  for v1 in range(v0*v0, top, v0):
    val[v1] = v0


class Solution:
  def sumOfLargestPrimes(self, s: str) -> int:
    cand = set()

    def is_prime_mr(num: int) -> bool:
      basePrimes = [2, 3, 5, 7, 11, 13, 17, 19]
      if num <= basePrimes[-1]: 
        return num in basePrimes

      for prime in basePrimes:
        if num %prime == 0: 
          return False
      
      #  Miller-Rabin primality test,
      #  based of Fermat's Little Thm
      oddPart,twoFactors = num-1, 0    
      while oddPart%2 == 0:
        oddPart //= 2
        twoFactors+= 1

      for prime in basePrimes:
        if prime >= num: 
          break
        
        modExp = pow(prime, oddPart, num)

        if 1 < modExp < num - 1:
          for _ in range(twoFactors-1):
            modExp = pow(modExp, 2, num)
            if modExp == num-1: 
              break

        else: 
          return False
          
      return True

    def is_prime(val: int) -> bool:
      if val < 2:
        return False

      for p0 in p:
        if p0 > val:
          break

        if val%p0 == 0:
          # print('check:', val, p0)
          return val == p0

      return True

    n = len(s)
    for i in range(n):
      if s[i] == '0':
        continue

      for j in range(i, n):
        val = int(s[i:j+1])
        if is_prime(val):
          cand.add(val)

    if not cand:
      return 0

    cand = sorted(cand)
    # print('done:', cand)

    return sum(cand[-3:])
