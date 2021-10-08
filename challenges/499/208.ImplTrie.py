'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
'''


class Trie:
  def __init__(self):
    self.is_word = False
    self.children = [None] * 26


  def insert(self, word: str) -> None:
    curr = self
    idx = 0
    
    while idx < len(word):
      c = ord(word[idx]) - ord('a')
      
      if not curr.children[c]:
        curr.children[c] = Trie()

      curr = curr.children[c]
      idx += 1

    curr.is_word = True
    

  def search(self, word: str) -> bool:
    curr = self
    last = None
    idx = 0
    # print(word)
    
    while idx < len(word):
      c = ord(word[idx]) - ord('a')
      
      if not curr.children[c]:
        return False
      
      last = curr
      curr = curr.children[c]
      idx += 1
      
    # print(last.children if last else None)
    return curr.is_word
    

  def startsWith(self, prefix: str) -> bool:
    curr = self
    idx = 0
    
    while idx < len(prefix):
      c = ord(prefix[idx]) - ord('a')
      
      if not curr.children[c]:
        return False
      
      curr = curr.children[c]
      idx += 1
      
    return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)