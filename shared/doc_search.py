from bisect import bisect_left, bisect_right
from typing import List


class Search:
  def __init__(self, doc: str = ''):
    self.backbone = ''
    self.dict = None

    if doc:
      self.set_doc(doc)


  def parse(self, w: str) -> str:
    # to lower case
    w = w.lower()
    # remove non-alphabetic-or-numeric chars
    w = ''.join(filter(str.isalnum, w))

    return w


  def set_doc(self, doc: str):
    self.backbone = doc.split()
    self.dict = {}

    for i, w in enumerate(self.backbone):
      w = self.parse(w)
      if not w:
        continue

      if w not in self.dict:
        self.dict[w] = []

      self.dict[w].append(i)


  def append_doc(self, extra: str):
    last = len(self.backbone)
    self.backbone += extra.split()

    for i, w in enumerate(self.backbone[last:]):
      j = i + last
      w = self.parse(w)
      if not w:
        continue

      if w not in self.dict:
        self.dict[w] = []

      self.dict[w].append(j)


  def search(self, keywords: List[str]) -> str:
    words = set(map(str.lower, keywords))
    i, j = len(self.backbone), 0

    # get the starting boundaries
    for k in words:
      if k in self.dict:
        i = min(i, self.dict[k][0])
        j = max(j, self.dict[k][-1])

    # print(i, j)
    # print(self.backbone)

    # prepare for the internal counters
    counter = {}
    for k in words:
      if k in self.dict:
        l = bisect_left(self.dict[k], i)
        r = bisect_right(self.dict[k], j)
        counter[k] = r-l

    s, e = i, j+1
    while s < e:
      w = self.parse(self.backbone[s])

      if w not in words:
        s += 1
        continue

      if counter[w] == 1:
        break

      counter[w] -= 1
      s += 1

    while s < e:
      w = self.parse(self.backbone[e-1])

      if w not in words:
        e -= 1
        continue

      if counter[w] == 1:
        break

      counter[w] -= 1
      e -= 1

    # print(counter)
    # print('after start:', s)
    # print('after end:', e)

    return ' '.join(self.backbone[s:e])


test = Search('''
The format of the output is as follows:
For each term of free variables with a non-zero coefficient, we write the free variables within a term in sorted order lexicographically.
For example, we would never write a term like "b*a*c", only "a*b*c".
Terms have degrees equal to the number of free variables being multiplied, counting multiplicity. We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.
For example, "a*a*b*c" has degree 4.
The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.) A leading coefficient of 1 is still printed.
An example of a well-formatted answer is ["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"].
Terms (including constant terms) with coefficient 0 are not included.
For example, an expression of "0" has an output of [].
''')

words = ['for', 'we', 'equal', 'of']

print(test.search(words))
