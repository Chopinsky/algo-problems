class Solution:
  step = 1

  def output(self, disk: int, source: str, dest: str):
    print('step', self.step, '-> move', disk, 'from', source, 'to', dest)
    self.step += 1

  def solve(self, disk: int):
    self.move(disk, 'A', 'C', 'B')

  def move(self, disk: int, source: str, dest: str, middle: str):
    if disk == 1:
      self.output(disk, source, dest)
      return
    
    self.move(disk-1, source, middle, dest)
    self.output(disk, source, dest)
    self.move(disk-1, middle, dest, source)

s = Solution()
s.solve(8)
  

