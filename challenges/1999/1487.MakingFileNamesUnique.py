class Solution:
  def getFolderNames(self, names: List[str]) -> List[str]:
    last = {}
    
    for name in names:
      curr = name
      
      if name in last:
        version = last[name]
        
        while curr in last:
          version += 1
          curr = f'{name}({version})'
          # print(curr)
          
        last[name] = version
        
      last[curr] = 0
      
    return last.keys()
    
  def getFolderNames0(self, names: List[str]) -> List[str]:
    cache = {}
    added = set()
    ans = []
      
    def suffix(s: str) -> Tuple[str, int]:
      if len(s) < 4 or s[-1] != ')':
        return (s, -1)
      
      idx = len(s) - 2
      base = 0
      
      while idx >= 0 and s[idx] != '(':
        if s[idx] < '0' or s[idx] > '9':
          break
        
        base = base*10 + (ord(s[idx]) - ord('0'))
        idx -= 1
      
      if idx == 0 or idx == len(s)-2 or s[idx] == '0' or not base or s[idx] != '(':
        return (s, -1)
      
      return (s[:idx], base)
    
    def add_name(n: str, has_suffix=False):
      # print('adding new:', n, cache)
      
      if n not in cache:
        if not has_suffix:
          cache[n] = [1, set([0])]
          ans.append(n)
          added.add(n)
          
        else:
          cache[n] = [2, set([1])]
          ans.append(n + '(1)')
          added.add(n + '(1)')
          
        return
      
      # if n == 'r':
      #   print(n, cache[n])

      sfx = cache[n][0]
      src = f'{n}({sfx})' if sfx > 0 else n
      
      while sfx in cache[n][1] or src in added:
        sfx += 1
        src = f'{n}({sfx})' if sfx > 0 else n

      cache[n][0] = sfx + 1
      cache[n][1].add(sfx)
      
      ans.append(src)
      added.add(src)

      return
    
    for name in names:
      n, c = suffix(name)
      # print(n, c)
      
      if c < 0:
        # if name does not have a suffix yet, add it
        add_name(n)
        
      else:
        # if name with the suffix already exists, append new
        if name in added:
          add_name(name, True)
          continue
          
        if n not in cache:
          cache[n] = [0, set([c])]
        else:
          cache[n][1].add(c)
          
        ans.append(name)
        added.add(name)
      
    return ans
  
