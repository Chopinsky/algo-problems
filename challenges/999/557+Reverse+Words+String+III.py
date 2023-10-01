'''
557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"

Constraints:

1 <= s.length <= 5 * 10^4
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
'''


class Solution:
  def reverseWords(self, s: str) -> str:
    def rev(w: str):
      arr = list(w)
      return ''.join(arr[::-1])
    
    a = s.split(' ')
    for i in range(len(a)):
      a[i] = rev(a[i])
      
    # print(a)
    
    return ' '.join(a)
