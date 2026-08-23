'''
3348-smallest-divisible-digit-product-ii
'''

from math import gcd


class Solution:
  def smallestNumber(self, s: str, t: int) -> str:
    val = t
    for i in range(2, 10):
      while val%i == 0:
        val //= i

    # product can be divisible by t
    if val > 1:
      return "-1"

    n = len(s)
    rem = [0] * (n+1)
    rem[0] = t
    pos = n-1
    digits = list(s)

    for i in range(n):
      if digits[i] == '0':
        pos = i
        break

      rem[i+1] = rem[i] // gcd(rem[i], int(digits[i]))

    # already divisible
    if rem[n] == 1:
      return s

    for i in range(pos, -1, -1):
      while True:
        digits[i] = chr(ord(digits[i]) + 1)
        if digits[i] > "9":
          break

        t_now = rem[i] // gcd(rem[i], int(digits[i]))
        k = 9

        for j in range(n-1, i, -1):
          while t_now % k != 0:
            k -= 1

          t_now //= k
          digits[j] = str(k)

        if t_now == 1:
          return "".join(digits)

    ans = []
    ot = t

    for i in range(9, 1, -1):
      while ot % i == 0:
        ans.append(str(i))
        ot //= i

    ans_str = "".join(ans)
    padding = max(n+1-len(ans_str), 0)
    ans_str += "1" * padding

    return ans_str[::-1]


  def smallestNumber(self, s: str, t: int) -> str:
    def fill(value: int, length: int):
      ans = []

      for d in range(9, 1, -1):
        while value % d == 0:
          ans.append(d)
          value //= d

      ans += [1] * max(0, length-len(ans))

      return "".join(str(val) for val in ans[::-1])
  
    val = t
    for p in [2, 3, 5, 7]:
      while val % p == 0:
        val //= p
    
    if val > 1:
      return "-1"
    
    n = len(s)
    p = [t] * (n + 1)
    
    for i, x in enumerate(map(int, s)):
      if x == 0: 
        break
        
      p[i+1] = p[i] // gcd(p[i], x)
      
    if p[-1] == 1:
      return s

    zero = s.find("0") % n
    
    for i in range(zero, -1, -1):
      req = p[i]
      digits = n - 1 - i
      for d in range(int(s[i]) + 1, 10):
        ending = fill(req // gcd(req, d), digits)
        if len(ending) <= digits:
          return s[:i] + str(d) + ending

    return fill(t, len(s) + 1)
  