'''
3484-design-spreadsheet
'''

from collections import defaultdict


class Spreadsheet:
  def __init__(self, rows: int):
    self.rows = rows
    self.vals = defaultdict(int)

  def toRC(self, cell: str):
    col = ord(cell[0]) - ord('A')
    row = int(cell[1:]) - 1
    return (row, col)

  def setCell(self, cell: str, value: int) -> None:
    r, c = self.toRC(cell)
    self.vals[r, c] = value
      

  def resetCell(self, cell: str) -> None:
    r, c = self.toRC(cell)
    self.vals[r, c] = 0
      

  def getValue(self, formula: str) -> int:
    if not formula or formula[0] != '=':
      return 0

    stack = formula[1:].split('+')
    curr = 0
    if len(stack) < 2:
      return 0

    # print('sheet:', self.vals, stack)
    for symb in stack:
      if not symb:
        continue

      if 'A' <= symb[0] <= 'Z':
        r, c = self.toRC(symb)
        curr += self.vals[r, c]
      else:
        curr += int(symb)

    return curr
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)