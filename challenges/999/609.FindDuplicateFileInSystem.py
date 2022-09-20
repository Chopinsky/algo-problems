'''
Given a list paths of directory info, including the directory path, and all the files with contents in this directory, return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"

Example 1:

Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Example 2:

Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Constraints:

1 <= paths.length <= 2 * 104
1 <= paths[i].length <= 3000
1 <= sum(paths[i].length) <= 5 * 105
paths[i] consist of English letters, digits, '/', '.', '(', ')', and ' '.
You may assume no files or directories share the same name in the same directory.
You may assume each given directory info represents a unique directory. A single blank space separates the directory path and file info.
'''

from collections import defaultdict
from typing import List
from functools import lru_cache


class Solution:
  def findDuplicate(self, paths: List[str]) -> List[List[str]]:
    store = defaultdict(list)
    
    @lru_cache(None)
    def parse_file(src):
      content = src.split('.txt(')
      return content[0]+'.txt', content[1][:-1]
    
    @lru_cache(None)
    def parse(src):
      arr = src.split(' ')
      dir_name = arr[0]
      
      for file in arr[1:]:
        file_name, content = parse_file(file)
        store[content].append(f"{dir_name}/{file_name}")
        
    for path in paths:
      parse(path)
    
    ans = []
    for files in store.values():
      if len(files) > 1:
        ans.append(files)
      
    return ans
      

  def findDuplicate(self, paths: List[str]) -> List[List[str]]:
    ans = []
    contents = defaultdict(list)

    for f in paths:
      f = f.strip().split()
      if len(f) <= 1:
        continue

      d = f[0]
      if d[-1] != '/':
        d += '/'

      for w in f[1:]:
        idx = w.find('(')
        if idx < 0 or idx >= len(w)-1:
          continue

        c = w[idx:-1]
        if len(c) == 0:
          continue

        fname = w[:idx]
        while len(fname) > 0:
          if fname[0] != '/':
            break

          fname = fname[1:]

        contents[c].append(d + fname)

    # print(contents)
    for v in contents.values():
      if len(v) > 1:
        ans.append(v)

    return ans
