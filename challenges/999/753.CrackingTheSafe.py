'''
There is a safe protected by a password. The password is a sequence of n digits where each digit can be in the range [0, k - 1].

The safe has a peculiar way of checking the password. When you enter in a sequence, it checks the most recent n digits that were entered each time you type a digit.

For example, the correct password is "345" and you enter in "012345":
After typing 0, the most recent 3 digits is "0", which is incorrect.
After typing 1, the most recent 3 digits is "01", which is incorrect.
After typing 2, the most recent 3 digits is "012", which is incorrect.
After typing 3, the most recent 3 digits is "123", which is incorrect.
After typing 4, the most recent 3 digits is "234", which is incorrect.
After typing 5, the most recent 3 digits is "345", which is correct and the safe unlocks.
Return any string of minimum length that will unlock the safe at some point of entering it.

Example 1:

Input: n = 1, k = 2
Output: "10"
Explanation: The password is a single digit, so enter each digit. "01" would also unlock the safe.

Example 2:

Input: n = 2, k = 2
Output: "01100"
Explanation: For each possible password:
- "00" is typed in starting from the 4th digit.
- "01" is typed in starting from the 1st digit.
- "10" is typed in starting from the 3rd digit.
- "11" is typed in starting from the 2nd digit.
Thus "01100" will unlock the safe. "01100", "10011", and "11001" would also unlock the safe.
 

Constraints:

1 <= n <= 4
1 <= k <= 10
1 <= kn <= 4096
'''


class Solution:
  def crackSafe(self, n: int, k: int) -> str:
    def de_bruijn(k: int, n: int) -> str:
      """
      de Bruijn sequence for alphabet k
      and subsequences of length n.
      """

      alphabet = list(map(str, range(k)))
      arr = [0] * (k*n)
      seq = []

      '''
      build the de Bruijin sequence
      '''
      def db_seq(t, p):
        if t <= n:
          arr[t] = arr[t-p]
          db_seq(t+1, p)

          for j in range(arr[t-p]+1, k):
            arr[t] = j
            db_seq(t + 1, t)

        elif n % p == 0:
          seq.extend(arr[1:p+1])

      db_seq(1, 1)
      return "".join(alphabet[i] for i in seq)
    
    if n==1:
      return "".join(str(j) for j in range(0,k))
    
    if k == 1:
      return "".join(str(0) for j in range(0,n))
    
    z= de_bruijn(k, n)
    
    return z + z[:n-1]
    
  def crackSafe00(self, n: int, k: int) -> str:
    m = k ** (n-1)
    ans = ''
    out = [0 for _ in range(k * m)]
    
    # build the graph
    for i in range(k):
      for j in range(m):
        out[i*m+j] = j*k + i
        
    for i in range(len(out)):
      curr = i
      while out[curr] >= 0:
        ans += str(curr // m)
        nxt = out[curr]
        out[curr] = -1
        curr = nxt
    
    for i in range(n-1):
      ans += '0'
    
    return ans
    
    
  def crackSafe01(self, n: int, k: int) -> str:
    # use Eulerian path to format the string
    seen = set(['0'*n])
    stack = [['0'*n, 0]]
    # print('target', k ** n)
    
    while len(stack) < k ** n:
      # print(stack, len(stack))
      src, last = stack[-1]
      nxt, idx = src, -1
      found = False
      
      for i in range(last+1, k):
        nxt = src[1:] + str(i)
        if nxt not in seen:
          found = True
          idx = i
          break
      
      if found:
        seen.add(nxt)
        stack[-1][1] = idx
        stack.append([nxt, -1])
      else:
        stack.pop()
        seen.discard(src)
        
    # print(stack)
    base = stack[0][0]
    for s, _ in stack[1:]:
      base += s[-1]
    
    return base
