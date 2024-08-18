'''
3260. Find the Largest Palindrome Divisible by K

You are given two positive integers n and k.

An integer x is called k-palindromic if:

x is a palindrome.
x is divisible by k.
Return the largest integer having n digits (as a string) that is k-palindromic.

Note that the integer must not have leading zeros.

Example 1:

Input: n = 3, k = 5

Output: "595"

Explanation:

595 is the largest k-palindromic integer with 3 digits.

Example 2:

Input: n = 1, k = 4

Output: "8"

Explanation:

4 and 8 are the only k-palindromic integers with 1 digit.

Example 3:

Input: n = 5, k = 6

Output: "89898"

Constraints:

1 <= n <= 10^5
1 <= k <= 9
'''

class Solution:
  '''
  most numbers between [1,9] can be solved in O(1) given how division works with them; the tricky part
  is for number 6 and 7, we don't have a good way to guess, so use DP here:

  - for any number "aba", we can calc remainder as (a*100)%k + (b*10)%k + a%k, so we can reduce the
    long number remainder calculation to essentially: sum((a*(exp(10,d)%k)%k);
  - we can pre-compute the exp(10,d)%k part, as it's essentially ((10%k) * exp(10,d-1))%k;
  - for a palindrom position (i, n-i+1), we can calculate the remainder as (a*exp(10,i))%k + (a*exp(10,n-i+1))%k,
    and from above we already know the exp(10,i) and exp(10,n-i+1), so this is O(1) calculation;
  - then we can use DP to store the combinations that won't work: start from number 9, then we go down to a value 
    where the sum(all_remainder_to_pal_pairs) == 0;
  - the technical trick here is that we need to store the invalid position, aka (i,prev_remainder) that can't generate
    the palindrom, otherwise, we will overshoot the memory limits;
  '''
  def largestPalindrome(self, n: int, k: int) -> str:
    if n <= 2:
      for val in range(9, 0, -1):
        pal = val if n == 1 else 10*val + val
        if pal % k == 0:
          return str(pal)
      
      return k
    
    if k == 1 or k == 3 or k == 9:
      return '9'*n
    
    if k == 2:
      return '8' + '9'*(n-2) + '8'
      
    if k == 4:
      if n < 4:
        return '888'
      
      return '88' + '9'*(n-4) + '88'
      
    if k == 8:
      if n < 6:
        return '8'*n
      
      return '888' + '9'*(n-6) + '888'
      
    if k == 5:
      return '5' + '9'*(n-2) + '5'
        
    tens = [1]
    while len(tens) < n:
      rem = ((10%k) * tens[-1]) % k
      tens.append(rem)
    
    # print(tens) 
    seen = set()
    
    def dp(i: int, rem: int):
      j = n-i-1
      if (i, rem) in seen:
        return ''
      
      if i > j:
        return ''
      
      if i == j:
        for val in range(9, 0, -1):
          pal = val * tens[i]
          if (pal+rem) % k == 0:
            return str(val)
          
        seen.add((i, rem))
        return ''
      
      if i+1 == j:
        # print('s1:', rem)
        for val in range(9, 0, -1):
          pal = (val*tens[j]) + (val*tens[i])
          if (pal+rem) % k == 0:
            return str(val) + str(val)
        
        seen.add((i, rem))
        return ''
        
      for val in range(9, 0, -1):
        r0 = val * (tens[i]+tens[j])
        mid = dp(i+1, (r0+rem) % k)
        if mid:
          return str(val) + mid + str(val)
        
      seen.add((i, rem))
      # print('size:', (i, rem), len(seen))
      
      return ''
    
    return dp(0, 0)
      