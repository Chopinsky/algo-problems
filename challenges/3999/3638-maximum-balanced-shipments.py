'''
3638-maximum-balanced-shipments
'''


class Solution:
  '''
  want the smallest shipment segments, which is the shortest descending subarray,
  and just count how many of this exists
  '''
  def maxBalancedShipments(self, weight: list[int]) -> int:
    count = 0
    max_val = 0

    for w in weight:
      max_val = max(max_val, w)

      # completing a shipment
      if w < max_val:
        count += 1
        max_val = 0

    return count
        