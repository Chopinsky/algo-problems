'''
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Example 2:

Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

Constraints:

n == dominoes.length
1 <= n <= 10 ** 5
dominoes[i] is either 'L', 'R', or '.'.
'''


class Solution:
  def pushDominoes(self, dominoes: str) -> str:
    stack = [(i, d) for i, d in enumerate(dominoes) if d != '.']
    if not stack:
      return dominoes

    res = ''
    n = len(stack)
    m = len(dominoes)
    # print('init:', stack)

    for i in range(n):
      if i == 0:
        ch = 'L' if stack[i][1] == 'L' else '.'
        res += ch*stack[i][0]

      res += stack[i][1]
      if i < n-1:
        space = stack[i+1][0] - stack[i][0] - 1
        if stack[i][1] == stack[i+1][1]:
          res += stack[i][1]*space 
        elif stack[i][1] == 'L' and stack[i+1][1] == 'R':
          res += '.'*space
        else:
          half = space // 2
          if space%2 == 0:
            res += 'R'*half + 'L'*half
          else:
            res += 'R'*half + '.' + 'L'*half

      if i == n-1:
        ch = 'R' if stack[i][1] == 'R' else '.'
        # print('tail:', ch, stack[i])
        res += ch*(m-1-stack[i][0])

    return res
        
  def pushDominoes(self, dominoes: str) -> str:
    stack = []
    ans = ''
    n = len(dominoes)
    
    for i, ch in enumerate(dominoes):
      if ch == '.':
        continue
        
      stack.append((ch, i))
        
    if not stack:
      return dominoes
    
    idx = 0
    m = len(stack)
    
    while idx < m:
      ch, i = stack[idx]
      if ch == 'L':
        if idx == 0:
          ans += 'L' * (i+1)
        else:
          ans += 'L' * (i-stack[idx-1][1])
          
        idx += 1
        continue

      if idx == 0:
        ans += '.' * i
        
      elif idx > 0 and stack[idx-1][0] == 'L':
        ans += '.' * (i-1-stack[idx-1][1])
        
      if idx == m-1:
        ans += 'R' * (n-i)
        idx += 1
        continue
        
      if stack[idx+1][0] == 'R':
        ans += 'R' * (stack[idx+1][1]-i)
        idx += 1
        continue
        
      # meet in the middle
      cnt = stack[idx+1][1] - i + 1
      # print('r', idx, stack[idx], ans)

      if cnt % 2 == 1:
        ans += 'R'*(cnt//2) + '.' + 'L'*(cnt//2)
      else:
        ans += 'R'*(cnt//2) + 'L'*(cnt//2)
      
      idx += 2
        
    if stack[-1][0] == 'L' and len(ans) < n:
      ans += (n - len(ans)) * '.'
      
    # print(stack)
    return ans
    

  def pushDominoes(self, d: str) -> str:
    stack = []
    
    for i, ch in enumerate(d):
      if ch == 'L' or ch == 'R':
        stack.append((ch, i))

    if len(stack) == 0:
      return d
    
    ans = ''
    # print(stack)
    
    for pos in range(len(d)):
      if len(stack) == 0:
        ans += '.'
        continue
        
      if len(stack) == 1:
        if stack[0][0] == 'L' and pos <= stack[0][1]:
          ans += 'L'
        elif stack[0][0] == 'R' and pos >= stack[0][1]:
          ans += 'R'
        else:
          ans += '.'
          
        continue
        
      if pos <= stack[0][1]:
        if pos == stack[0][1]:
          ans += stack[0][0]
        else:
          ans += '.' if stack[0][0] == 'R' else 'L'
          
        continue
        
      if pos == stack[1][1]:
        ans += stack[1][0]
        stack = stack[1:]
        continue
        
      if stack[0][0] == stack[1][0]:
        ans += stack[0][0]
        continue
        
      if stack[0][0] == 'R' and stack[1][0] == 'L':
        if pos - stack[0][1] > stack[1][1] - pos:
          ans += stack[1][0]
        elif pos - stack[0][1] < stack[1][1] - pos:
          ans += stack[0][0]
        else:
          ans += '.'
        
        continue
        
      ans += '.'
    
    return ans
  