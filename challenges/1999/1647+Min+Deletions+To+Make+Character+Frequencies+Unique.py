'''
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
 

Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.
'''

from collections import Counter


class Solution:
  def minDeletions(self, s: str) -> int:
    c = Counter(s)
    arr = sorted(c.values())
    deletes = 0
    n = len(c)
    # print(arr)
    
    for i in range(n-2, -1, -1):
      if arr[i] >= arr[i+1]:
        original = arr[i]
        arr[i] = max(0, arr[i+1] - 1)
        # print('d:', original, arr[i])
        deletes += original - arr[i]
    
    return deletes
        
        
  def minDeletions(self, s: str) -> int:
    c = Counter(s)
    arr = sorted(c.values())
    rem = sorted(set([val for val in range(1, arr[-1]+1)]) - set(arr))
    count = 0
    seen = set()
    # print(arr, rem)
    
    while arr:
      val = arr.pop()
      if val not in seen:
        seen.add(val)
        continue
        
      while rem and rem[-1] >= val:
        rem.pop()
        
      if rem:
        nxt = rem.pop()
        count += val - nxt
      else:
        count += val
    
    return count
    