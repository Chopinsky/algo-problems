'''
2424. Longest Uploaded Prefix
'''

class LUPrefix:
  def __init__(self, n: int):
    self.videos = [i for i in range(n, 0, -1)]
    self.uploaded = set()


  def upload(self, video: int) -> None:
    self.uploaded.add(video)
    while self.videos and self.videos[-1] in self.uploaded:
      self.videos.pop()


  def longest(self) -> int:
    if not self.videos:
      return len(self.uploaded)
    
    if self.videos[-1] == 1:
      return 0
    
    return self.videos[-1]-1


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
