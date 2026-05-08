'''
3790-smallest-all-ones-multiple
'''


class Solution:
  def minAllOneMultiple(self, k: int) -> int:
    if k%2 == 0:
      return -1

    base = 1
    count = 1

    while base < k:
      base = 10*base + 1
      count += 1

    base %= k
    if base == 0:
      return count
    
    mods = set()
    while base > 0 and base not in mods:
      mods.add(base)
      base = 10*base + 1
      base %= k
      count += 1

    return count if base == 0 else -1
