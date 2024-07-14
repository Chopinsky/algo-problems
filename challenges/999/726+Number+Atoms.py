'''
726. Number of Atoms
'''

class Solution:
  def countOfAtoms(self, formula: str) -> str:
    n = len(formula)
    
    def merge(c0, c1, factor):
      for e, c in c1.items():
        c0[e] += c*factor
    
    def update(cnt, elem, num):
      cnt[elem] += num if num > 0 else 1
    
    def parse_num(i: int):
      if i >= n:
        return i, 1
      
      num = 0
      while i < n and '0' <= formula[i] <= '9':
        num = 10*num + (ord(formula[i])-ord('0'))
        i += 1
      
      return i, num if num > 0 else 1
      
    def parse(i: int):
      total = defaultdict(int)
      if i >= n:
        return i, total
      
      num = 0
      elem = ""
      j = i
      
      while j < n:
        ch = formula[j]
        if ch == ')':
          j += 1
          break
        
        if ch == '(':
          j, nested = parse(j+1)
          j, num = parse_num(j)
          merge(total, nested, num)
          num = 0
          continue
        
        if 'a' <= ch <= 'z':
          elem += ch
          j += 1
          continue
          
        if '0' <= ch <= '9':
          j, num = parse_num(j)
          update(total, elem, num)
          elem = ""
          num = 0
          continue
          
        # now it's a capital letter
        if elem:
          update(total, elem, num)
          elem = ""
          num = 0
          
        elem += ch
        j += 1
          
      if elem:
        update(total, elem, num)
        
      return j, total
        
    _, counter = parse(0)
    result = ""
    # print(counter, elements)
    
    for elem in sorted(counter.keys()):
      cnt = counter[elem]
      result += elem + ("" if cnt == 1 else str(cnt))
    
    return result
        