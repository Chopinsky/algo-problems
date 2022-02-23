'''
You are given two positive integers left and right with left <= right. Calculate the product of all integers in the inclusive range [left, right].

Since the product may be very large, you will abbreviate it following these steps:

Count all trailing zeros in the product and remove them. Let us denote this count as C.
For example, there are 3 trailing zeros in 1000, and there are 0 trailing zeros in 546.
Denote the remaining number of digits in the product as d. If d > 10, then express the product as <pre>...<suf> where <pre> denotes the first 5 digits of the product, and <suf> denotes the last 5 digits of the product after removing all trailing zeros. If d <= 10, we keep it unchanged.
For example, we express 1234567654321 as 12345...54321, but 1234567 is represented as 1234567.
Finally, represent the product as a string "<pre>...<suf>eC".
For example, 12345678987600000 will be represented as "12345...89876e5".
Return a string denoting the abbreviated product of all integers in the inclusive range [left, right].

Example 1:

Input: left = 1, right = 4
Output: "24e0"
Explanation: The product is 1 × 2 × 3 × 4 = 24.
There are no trailing zeros, so 24 remains the same. The abbreviation will end with "e0".
Since the number of digits is 2, which is less than 10, we do not have to abbreviate it further.
Thus, the final representation is "24e0".
Example 2:

Input: left = 2, right = 11
Output: "399168e2"
Explanation: The product is 39916800.
There are 2 trailing zeros, which we remove to get 399168. The abbreviation will end with "e2".
The number of digits after removing the trailing zeros is 6, so we do not abbreviate it further.
Hence, the abbreviated product is "399168e2".
Example 3:

Input: left = 371, right = 375
Output: "7219856259e3"
Explanation: The product is 7219856259000.

Constraints:

1 <= left <= right <= 10^4
'''


from math import log10


class Solution:
  '''
  this is a math problem .... prod % 10000 will get us the last 5 digits,
  min(fact_2_cnt, fact_5_cnt) will get us number of trailing 0s, and use
  10^(integer + fraction) = P => integer+fraction = log(P) = sum(log(val for val in [l, r+1]))
  then take 10^(4+fraction) will give us the top 5 digits
  '''
  def abbreviateProduct(self, left: int, right: int) -> str:
    
    c2, c5 = 0, 0
    prod = 1
    log_sum = 0
    mod = 100000
    big = False
    
    for num in range(max(2, left), right+1):
      log_sum = (log_sum + log10(num)) % 1
      
      curr = num
      while curr >= 2 and curr % 2 == 0:
        curr //= 2
        c2 += 1
        
      while curr >= 5 and curr % 5 == 0:
        curr //= 5
        c5 += 1
        
      prod = (prod * curr)
      while prod >= 10 and prod % 10 == 0:
        prod //= 10
        
      if not big and len(str(prod)) > 10:
        big = True
        
      if big:
        prod %= mod
      
    # number of 0s
    c = min(c2, c5)
    c2 -= c
    c5 -= c
    
    prod = (prod * pow(2, c2, mod) * pow(5, c5, mod))
    if big or len(str(prod)) > 10:
      big = True
      prod %= mod
      
    # print(prod, c, int(10 ** (4 + log_sum)))
    
    if not big:
      return str(prod) + 'e' + str(c)
    
    a = str(int(10 ** (4 + log_sum)))
    b = str(prod)
    c = str(c)
    
    if len(b) < 5:
      b = '0' * (5 - len(b)) + b
    
    return f'{a}...{b}e{c}' 
  