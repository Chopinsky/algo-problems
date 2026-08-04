'''
3514-number-of-unique-xor-triplets-ii
'''

from typing import List


class Solution:
  def uniqueXorTriplets(self, nums: List[int]) -> int:
    pairs = set()
    trip = set()
    n = len(nums)
    digits = 2 ** max(nums).bit_length()

    for i in range(n):
      for j in range(i+1):
        pairs.add(nums[i]^nums[j])

      for val in pairs:
        trip.add(nums[i]^val)

      # print('iter:', i, nums[i], pairs, trip)
      if len(trip) == digits: 
        break

    return len(trip)

        