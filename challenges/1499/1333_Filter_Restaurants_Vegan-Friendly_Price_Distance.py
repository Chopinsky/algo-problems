'''
1333. Filter Restaurants by Vegan-Friendly, Price and Distance
'''

from typing import List


class Solution:
  def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
    cand = [r for r in restaurants if (veganFriendly == 0 or r[2] == veganFriendly) and r[3] <= maxPrice and r[4] <= maxDistance]
    cand.sort(key=lambda x: (-x[1], -x[0]))
    # print('init:', cand)

    return [r[0] for r in cand]
        