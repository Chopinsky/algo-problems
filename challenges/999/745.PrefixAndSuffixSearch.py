'''
Design a special dictionary which has some words and allows you to search the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".

Constraints:

1 <= words.length <= 15000
1 <= words[i].length <= 10
1 <= prefix.length, suffix.length <= 10
words[i], prefix and suffix consist of lower-case English letters only.
At most 15000 calls will be made to the function f.
'''

from typing import List, Set


class WordFilter:
  def __init__(self, words: List[str]):
    self.dict = {}
    
    for i, w in enumerate(words):
      n = len(w)
      
      #prefix
      for j in range(1, n+1):
        #suffix
        for k in range(1, n+1):
          s = f'{w[-k:]}#{w[:j]}'
          self.dict[s] = i
          

  def f(self, prefix: str, suffix: str) -> int:
    w = f'{suffix}#{prefix}'
    if w not in self.dict:
      return -1
    
    return self.dict[w]


class WordFilter0:
  def __init__(self, words: List[str]):
    self.pre = Trie()
    self.suf = Trie()

    for i, w in enumerate(words):
      self.pre.insert(w, i)
      self.suf.insert(w[::-1], i)


  def f(self, prefix: str, suffix: str) -> int:
    a = self.pre.find(prefix)
    b = self.suf.find(suffix[::-1])

    if not a or not b:
      return -1

    c = a & b
    # print(a, b, c, max(c))

    return max(c)


class Trie:
  def __init__(self):
    self.i = -1
    self.c = {}


  def insert(self, w: str, i: int):
    if not w:
      self.i = i
      return

    if w[0] not in self.c:
      self.c[w[0]] = Trie()

    self.c[w[0]].insert(w[1:], i)


  def find(self, w: str) -> Set[int]:
    # print("found", self.i, w)

    if not w:
      ans = set()
      self.collect(ans)

      return ans if len(ans) > 0 else None

    return self.c[w[0]].find(w[1:]) if w[0] in self.c else None


  def collect(self, s: Set[int]):
    if self.i >= 0:
      s.add(self.i)

    for _, node in self.c.items():
      node.collect(s)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
