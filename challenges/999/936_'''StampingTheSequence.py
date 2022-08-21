'''
936. Stamping The Sequence

You are given two strings stamp and target. Initially, there is a string s of length target.length with all s[i] == '?'.

In one turn, you can place stamp over s and replace every letter in the s with the corresponding letter from stamp.

For example, if stamp = "abc" and target = "abcba", then s is "?????" initially. In one turn you can:
place stamp at index 0 of s to obtain "abc??",
place stamp at index 1 of s to obtain "?abc?", or
place stamp at index 2 of s to obtain "??abc".
Note that stamp must be fully contained in the boundaries of s in order to stamp (i.e., you cannot place stamp at index 3 of s).
We want to convert s to target using at most 10 * target.length turns.

Return an array of the index of the left-most letter being stamped at each turn. If we cannot obtain target from s within 10 * target.length turns, return an empty array.

Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
Explanation: Initially s = "?????".
- Place stamp at index 0 to get "abc??".
- Place stamp at index 2 to get "ababc".
[1,0,2] would also be accepted as an answer, as well as some other answers.
Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]
Explanation: Initially s = "???????".
- Place stamp at index 3 to get "???abca".
- Place stamp at index 0 to get "abcabca".
- Place stamp at index 1 to get "aabcaca".

Constraints:

1 <= stamp.length <= target.length <= 1000
stamp and target consist of lowercase English letters.
'''

from typing import List
from collections import deque


class Solution:
  '''
  reverse the process -- check all the positions that we can stamp last, then 
  remove them from the target string, and check all the positions that become
  available after removing the top stamps; then just reverse the stamp order
  and we're done
  '''
  def movesToStamp(self, stamp: str, target: str) -> List[int]:
    m, n = len(stamp), len(target)
    seen = set()
    target = list(target)
    count = 0
    ans = []
      
    def can_replace(idx):
      for d in range(m):
        if target[idx+d] != '*' and target[idx+d] != stamp[d]:
          return False

      return True

    def replace(idx):
      count = 0
      for i in range(idx, idx+m):
        if target[i] != '*':
          count += 1
          target[i] = '*'

      return count
    
    while count < n:
      replaced = False
      
      # check every index that hasn't bee stamped as the starting
      # position and can now be stamped
      for i in range(n-m+1):
        # can't do anything at index-i
        if i in seen or not can_replace(i):
          continue
          
        # we can stamp at index-i, update how many
        # characters will be replaced
        ans.append(i)
        seen.add(i)
        replaced = True

        # add count of replaced chars to keep track
        # of the progress
        count += replace(i)
        if count == n:
          break

      # if none of the positions can be stamped, we're stuck, failed 
      # and done
      if not replaced:
        return []

    return ans[::-1]

  
  def movesToStamp(self, stamp: str, target: str) -> List[int]:
    m, n = len(stamp), len(target)
    ans = []
    
    if stamp[0] != target[0] or stamp[-1] != target[-1]:
      return ans
    
    q = deque([])
    done = [False] * n
    arr = []
    
    for i in range(n-m+1):
      seen, todo = set(), set()
      for j, ch in enumerate(stamp):
        if target[i+j] == ch:
          seen.add(i+j)
        else:
          todo.add(i+j)
        
      arr.append((seen, todo))
      if not todo:
        ans.append(i)
        for j in range(i, i+m):
          if not done[j]:
            q.append(j)
            done[j] = True
        
    # print(arr)
    while q:
      i = q.popleft()
      for j in range(max(0, i-m+1), min(n-m, i)+1):
        if i in arr[j][1]:
          arr[j][1].discard(i)
          if not arr[j][1]:
            ans.append(j)
            for k in arr[j][0]:
              if not done[k]:
                q.append(k)
                done[k] = True
      
    if all(done):
      return ans[::-1]
    
    return []
    