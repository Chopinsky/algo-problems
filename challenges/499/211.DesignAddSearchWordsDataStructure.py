'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
'''


class WordDictionary:
  def __init__(self):
    self.root = {}


  def addWord(self, word: str) -> None:
    curr = self.root
    for ch in word:
      if ch not in curr:
        curr[ch] = {}
        
      curr = curr[ch]
      
    curr['$'] = None


  def search(self, word: str) -> bool:
    curr = self.root
    
    def find(word: str) -> bool:
      nonlocal curr 
      
      for i, ch in enumerate(word):
        if not curr:
          return False
        
        if ch == '.':
          src_curr = curr
          for nxt in curr.keys():
            curr = curr[nxt]
            if find(word[i+1:]):
              return True
            
            # reset
            curr = src_curr
            
          return False
        
        if ch not in curr:
          return False
        
        curr = curr[ch]
        
      # make sure we're at the end word
      return ('$' in curr) if curr else False
    
    return find(word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)