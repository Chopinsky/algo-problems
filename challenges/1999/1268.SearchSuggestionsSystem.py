'''
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.



Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]

Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
'''

from bisect import bisect_left, bisect_right
from typing import List

class Trie:
  def __init__(self, w: str, idx: int):
    self.children = [None] * 26

    if idx == len(w):
      self.word = w
    else:
      self.word = None
      ch = ord(w[idx]) - ord('a')
      self.children[ch] = Trie(w, idx+1)


  def insert(self, w: str, idx: int):
    if idx == len(w):
      self.word = w
      return

    ch = ord(w[idx]) - ord('a')
    if self.children[ch]:
      self.children[ch].insert(w, idx+1)
    else:
      self.children[ch] = Trie(w, idx+1)


  def get_next(self, w: str, idx: int):
    return self.children[ord(w[idx]) - ord('a')]


  def collect(self, arr: list) -> list:
    if self.word:
      arr.append(self.word)

    if len(arr) >= 3:
      return arr

    for child in self.children:
      if not child:
        continue

      arr = child.collect(arr)
      if len(arr) >= 3:
        break

    return arr


class Solution:
  def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    ans = []
    products.sort()
    prefix = ''

    for ch in searchWord:
      prefix += ch
      l = bisect_left(products, prefix)
      r = bisect_right(products, prefix+'~')

      # no matching
      if l == r:
        break

      ans.append(products[l:min(l+3, r)])

    while len(ans) < len(searchWord):
      ans.append([])

    return ans


  def suggestedProducts1(self, products: List[str], searchWord: str) -> List[List[str]]:
    root = Trie("", 0)
    ans = []

    for w in products:
      root.insert(w, 0)

    # print(root.children)
    curr = root

    for i in range(len(searchWord)):
      if curr:
        curr = curr.get_next(searchWord, i)

      # print(curr.__dict__ if curr else None)
      ans.append([] if not curr else curr.collect([]))

    return ans
