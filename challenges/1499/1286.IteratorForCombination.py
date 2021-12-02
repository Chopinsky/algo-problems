'''
Design the CombinationIterator class:

CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
next() Returns the next combination of length combinationLength in lexicographical order.
hasNext() Returns true if and only if there exists a next combination.

Example 1:

Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]

Explanation
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False
 
Constraints:

1 <= combinationLength <= characters.length <= 15
All the characters of characters are unique.
At most 10^4 calls will be made to next and hasNext.
It's guaranteed that all calls of the function next are valid.
'''


class CombinationIterator:
  def __init__(self, characters: str, m: int):
    self.chars = list(characters)
    self.ptrs = [i for i in range(m)]
    # print(self.chars, self.ptrs)

    self.idx = m-1
    self.has_next = (len(self.chars) > m)
    

  def next(self) -> str:
    base = ''.join(self.chars[i] for i in self.ptrs)
    m, n = len(self.ptrs), len(self.chars)
    j = m - 1
    
    while j > 0 and self.ptrs[j] == n-m+j:
      j -= 1
      
    if j == 0 and self.ptrs[j] == n-m:
      self.has_next = False
    else:
      self.ptrs[j] += 1
      for k in range(j+1, m):
        self.ptrs[k] = self.ptrs[k-1] + 1
    
    return base
    

  def hasNext(self) -> bool:
    return self.has_next


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()