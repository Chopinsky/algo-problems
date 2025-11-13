'''
2125-number-of-laser-beams-in-a-bank
'''

from typing import List


class Solution:
  def numberOfBeams(self, bank: List[str]) -> int:
    c = 0
    if not bank:
      return c

    n = len(bank[0])
    prev = 0

    for row in bank:
      sensor_count = row.count('1')
      if not sensor_count:
        continue

      c += prev * sensor_count
      prev = sensor_count

    return c

        