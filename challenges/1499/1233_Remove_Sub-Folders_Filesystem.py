'''
1233. Remove Sub-Folders from the Filesystem

Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it.

The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.

Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".
Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]

Constraints:

1 <= folder.length <= 4 * 10^4
2 <= folder[i].length <= 100
folder[i] contains only lowercase letters and '/'.
folder[i] always starts with the character '/'.
Each folder name is unique.
'''

from typing import List


class Solution:
  def removeSubfolders(self, folder: List[str]) -> List[str]:
    root = {}
    cand = sorted([f.split('/') for f in folder], key=lambda x: (len(x), x))
    # print('init:', cand)

    def check(c: List) -> bool:
      curr = root
      level = 0
      # print('check:', c)

      for f in c:
        if f not in curr:
          if level == 0:
            # print('out-1')
            return True

          if len(curr) > 0:
            # print('out-2')
            return True

          return False

        curr = curr[f]
        level += 1

      return True

    def insert(c: List):
      curr = root

      for f in c:
        if f not in curr:
          curr[f] = {}

        curr = curr[f]

    ans = []
    for c in cand:
      # print(root)
      if check(c[1:]):
        insert(c[1:])
        ans.append('/'.join(c))

    return ans
        
  def removeSubfolders(self, folder: List[str]) -> List[str]:
    folder.sort()
    root = {}
    ans = []
    # print('init:', folder)
    
    def add(f: str) -> bool:
      node = root
      subs = f[1:].split('/')
      n = len(subs)
      
      if n == 1:
        root[subs[0]] = {'$': 1}
        return True
      
      for sf in subs:
        if sf not in node:
          node[sf] = {}
          
        node = node[sf]
        if '$' in node:
          return False
        
      node['$'] = 1
      return True
    
    for f in folder:
      if not add(f):
        continue
        
      ans.append(f)
      
    return ans
        
  def removeSubfolders(self, folder: List[str]) -> List[str]:
    folder.sort(key=lambda x: x.count('/'))
    seen = set()
    ans = []
    # print(folder)
    
    for f in folder:
      if not f:
        continue
        
      src = f.split('/')[1:]
      parent = ''
      found = False
      
      for sf in src:
        parent += f'/{sf}'
        # print('build:', f, parent)
        
        if parent in seen:
          found = True
          break
      
      seen.add(f)
      if not found:
        ans.append(f)
        
      # print(f, parent, found)
    
    return ans
  
  