'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0

Constraints:

1 <= text.length <= 10 ** 4
text consists of lower case English letters only.
'''


from collections import Counter


class Solution:
  def maxNumberOfBalloons(self, text: str) -> int:
    count = Counter(text)
    ans = len(text)
    # print(count)  
    
    for ch in 'balon':
      if ch == 'l' or ch == 'o':
        ans = min(ans, count[ch]//2)
      else:
        ans = min(ans, count[ch])
    
    return ans
  