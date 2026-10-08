'''
1021-remove-outermost-parentheses
'''


class Solution:
  def removeOuterParentheses(self, s: str) -> str:
    cand = []
    start = 0
    bal = 0

    for i, ch in enumerate(s):
      bal += 1 if ch == '(' else -1
      if bal == 0:
        cand.append(s[start:i+1])
        start = i+1

    # print('init:', cand)
    return "".join(w[1:-1] if w[0] == '(' and w[-1] == ')' else w for w in cand)
