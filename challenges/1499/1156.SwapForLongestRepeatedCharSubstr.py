'''
You are given a string text. You can swap two of the characters in the text.

Return the length of the longest substring with repeated characters.

Example 1:

Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa" with length 3.
Example 2:

Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa" with length 6.
Example 3:

Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa" with length is 5.

Constraints:

1 <= text.length <= 2 * 10^4
text consist of lowercase English characters only.
'''


from collections import defaultdict


class Solution:
  def maxRepOpt1(self, text: str) -> int:
    pos = defaultdict(list)
    for i, ch in enumerate(text):
      if (ch not in pos) or (i != pos[ch][-1][1]+1):
        pos[ch].append([i, i])
      else:
        pos[ch][-1][1] = i
        
    # print(pos)
    if len(pos) == 1:
      return len(text)
    
    max_len = 1
    for p in pos.values():
      if len(p) == 1:
        max_len = max(max_len, p[0][1]-p[0][0]+1)
        continue
        
      last_dist = 0
      for i in range(len(p)):
        # we can always borrow a char from another range
        dist = p[i][1]-p[i][0]+1
        max_len = max(max_len, dist+1)
        
        # if we can connect with the next range
        if i > 0 and p[i][0] == p[i-1][1]+2:
          # print(p, p[i])
          max_len = max(max_len, dist+last_dist+(1 if len(p) > 2 else 0))
        
        last_dist = dist
        
    return max_len
      