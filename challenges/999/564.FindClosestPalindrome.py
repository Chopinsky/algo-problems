'''
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

Example 1:

Input: n = "123"
Output: "121"

Example 2:

Input: n = "1"
Output: "0"

Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.

Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 10^18 - 1]

Test cases:

"123"
"1"
"10"
"100"
"99"
"1283"
"1213"
"12389"
"1837722381"
"12"
'''

from functools import cache

class Solution:
  def nearestPalindromic(self, n: str) -> str:
    ln = len(n)
    val = int(n)
    
    if ln == 1:
      return '1' if n == '0' else str(val-1)
    
    @cache
    def get_pal():
      pal = [int(d) for d in n]
      i = (ln-1) // 2
      j = ln // 2
      
      while i >= 0:
        pal[j] = pal[i]
        i -= 1
        j += 1
        
      return ''.join(str(d) for d in pal)
      
    def downgrade():
      return '9' * (ln-1)
    
    def lower_bound():
      pal = get_pal()
      if int(pal) < val:
        return pal
      
      low = [int(d) for d in n]
      i = (ln-1) // 2
      j = ln // 2
      done = False
      over = 0
      
      while i >= 0:
        if done:
          low[i] += over
          if low[i] < 0:
            low[i] += 10
            over = -1
          else:
            over = 0
          
        else:
          if low[j] <= low[i]:
            low[i] -= 1
            
          if low[i] < 0:
            low[i] += 10
            over = -1
          
          done = True
        
        low[j] = low[i]
        i -= 1
        j += 1
        
      # print('low:', low, over)
      i = 0
      while i < len(low) and low[i] == 0:
        i += 1
        
      if i >= len(low) or over != 0:
        return downgrade()
        
      return ''.join(str(d) for d in low[i:])
      
    def upper_bound():
      pal = get_pal()
      if int(pal) > val:
        return pal
      
      high = [int(d) for d in n]
      i = (ln-1) // 2
      j = ln // 2
      done = False
      over = 0
      
      while i >= 0:
        if done:
          high[i] += over
          if high[i] > 9:
            high[i] -= 10
            over = 1
          else:
            over = 0
          
        else:
          if high[j] >= high[i]:
            high[i] += 1
            
          if high[i] > 9:
            high[i] -= 10
            over = 1

          done = True
          
        high[j] = high[i]
        i -= 1
        j += 1
      
      # print('high:', high, over)
      if over != 0:
        return upgrade()
      
      return ''.join(str(d) for d in high)
      
    def upgrade():
      return '1' + '0'*(ln-1) + '1'
    
    res = downgrade()
    diff = abs(val - int(res))
    # print("v0:", res)
    
    v1 = lower_bound()
    d1 = abs(val - int(v1))
    # print("v1:", v1)
    
    if d1 < diff:
      diff = d1
      res = v1
    
    v2 = upper_bound()
    d2 = abs(int(v2) - val)
    # print("v2:", v2)
    
    if d2 < diff:
      diff = d2
      res = v2
    
    v3 = upgrade()
    d3 = abs(int(v3) - val)
    # print("v3:", v3)
    
    if d3 < diff:
      diff = d3
      res = v3
      
    return res
        
  def nearestPalindromic(self, n: str) -> str:
    ln = len(n)
    if ln == 1:
      return str(int(n) - 1)

    if n == '11' or n == ('1' + '0'*(ln-1)):
      return '9' * (ln-1)

    if n == '9'*ln and ln > 1:
      return '1' + '0'*(ln-1) + '1'

    tgt = list(n)
    last = (ln-1)//2
    isPali = True

    for i in range(ln-1, last, -1):
      l, r = n[ln-i-1], n[i]
      if l == r:
        continue

      isPali = False

      # print(i, last, l, r)

      if i == last+1:
        if ln % 2 == 0:
          self.find(list(n), tgt, i-1, i)
        else:
          self.find1(list(n), tgt, i-2, i)

      else:
        tgt[i] = l

    # print(isPali)

    if isPali:
      if ln % 2 == 0:
        r = ln//2
        l = r-1

        if n[l] == '0':
          tgt = self.expand(tgt, l-1, r+1, ln)
        else:
          tgt[l] = str(int(n[l])-1)
          tgt[r] = tgt[l]

      else:
        mid = ln//2
        if n[mid] == '0':
          tgt = self.expand(tgt, mid-1, mid+1, ln)
        else:
          tgt[mid] = str(int(tgt[mid])-1)

    return "".join(tgt)

  def expand(self, tgt, l, r, ln):
    while tgt[l] == '0':
      l -= 1
      r += 1

    if l == 0 and tgt[l] == '1':
      return ['9'] * (ln-1)

    if ln % 2 == 0:
      tgt = ['9' if i != 0 and i != ln-1 else str(int(tgt[0])-1) for i in range(ln)]
    else:
      tgt[ln//2] = '1'

    return tgt

  def find(self, src, tgt, l, r):
    curr = 10 * int(src[l]) + int(src[r])

    if int(src[l]) > int(src[r]):
      upper = 10 * int(tgt[l]) + int(tgt[l])
      lower = upper - 11
    else:
      lower = 10 * int(tgt[l]) + int(tgt[l])
      upper = lower + 11

    uu, ll = upper, lower
    for i in range(r+1, len(tgt)):
      curr = curr*10 + int(src[i])
      uu = uu*10 + int(tgt[i])
      ll = ll*10 + int(tgt[i])

    # print("find:", curr, uu, ll, upper, lower)

    if abs(uu - curr) < abs(curr - ll):
      tgt[l] = str(upper//10)
      tgt[r] = str(upper%10)
    else:
      tgt[l] = str(lower//10)
      tgt[r] = str(lower%10)

  def find1(self, src, tgt, l, r):
    curr = 100 * int(tgt[l]) + 10 * int(tgt[l+1]) + int(tgt[r])

    if int(src[l]) > int(src[r]):
      upper = 100 * int(tgt[l]) + 10 * int(tgt[l+1]) + int(tgt[l])

      if tgt[l+1] == '0':
        lower = upper - 11
      else:
        lower = upper - 10

      uu = upper
      ll = lower

      for i in range(r+1, len(tgt)):
        curr = curr*10 + int(src[i])
        uu = uu*10 + int(tgt[i])
        ll = ll*10 + int(tgt[i])

      # print("find1, upper:", curr, uu, ll, upper, lower)

      if abs(uu - curr) < abs(curr - ll):
        tgt[r] = tgt[l]
      else:
        tgt[l] = str(lower//100)
        tgt[l+1] = str((lower%100) // 10)
        tgt[r] = str(lower % 10)

    else:
      lower = 100 * int(tgt[l]) + 10 * int(tgt[l+1]) + int(tgt[l])

      if tgt[l+1] == '9':
        upper = lower + 11
      else:
        upper = lower + 10

      uu = upper
      ll = lower

      for i in range(r+1, len(tgt)):
        curr = curr*10 + int(src[i])
        uu = uu*10 + int(tgt[i])
        ll = ll*10 + int(tgt[i])

      # print("find1, lower:", curr, uu, ll, upper, lower)

      if abs(uu - curr) < abs(curr - ll):
        tgt[l] = str(upper//100)
        tgt[l+1] = str((upper%100) // 10)
        tgt[r] = str(upper % 10)
      else:
        tgt[r] = tgt[l]
