'''
Given an array of strings names of size n. You will create n folders in your file system such that, at the ith minute, you will create a folder with the name names[i].

Since two files cannot have the same name, if you enter a folder name which is previously used, the system will have a suffix addition to its name in the form of (k), where, k is the smallest positive integer such that the obtained name remains unique.

Return an array of strings of length n where ans[i] is the actual name the system will assign to the ith folder when you create it.

Example 1:

Input: names = ["pes","fifa","gta","pes(2019)"]
Output: ["pes","fifa","gta","pes(2019)"]
Explanation: Let's see how the file system creates folder names:
"pes" --> not assigned before, remains "pes"
"fifa" --> not assigned before, remains "fifa"
"gta" --> not assigned before, remains "gta"
"pes(2019)" --> not assigned before, remains "pes(2019)"

Example 2:

Input: names = ["gta","gta(1)","gta","avalon"]
Output: ["gta","gta(1)","gta(2)","avalon"]
Explanation: Let's see how the file system creates folder names:
"gta" --> not assigned before, remains "gta"
"gta(1)" --> not assigned before, remains "gta(1)"
"gta" --> the name is reserved, system adds (k), since "gta(1)" is also reserved, systems put k = 2. it becomes "gta(2)"
"avalon" --> not assigned before, remains "avalon"

Example 3:

Input: names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
Output: ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
Explanation: When the last folder is created, the smallest positive valid k is 4, and it becomes "onepiece(4)".

Example 4:

Input: names = ["wano","wano","wano","wano"]
Output: ["wano","wano(1)","wano(2)","wano(3)"]
Explanation: Just increase the value of k each time you create folder "wano".

Example 5:

Input: names = ["kaido","kaido(1)","kaido","kaido(1)"]
Output: ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
Explanation: Please note that system adds the suffix (k) to current name even it contained the same suffix before.

Constraints:

1 <= names.length <= 5 * 10^4
1 <= names[i].length <= 20
names[i] consists of lower case English letters, digits and/or round brackets.
'''

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
