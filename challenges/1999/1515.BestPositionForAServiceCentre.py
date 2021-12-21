'''
A delivery company wants to build a new service center in a new city. The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new center in a position such that the sum of the euclidean distances to all customers is minimum.

Given an array positions where positions[i] = [xi, yi] is the position of the ith customer on the map, return the minimum sum of the euclidean distances to all customers.

In other words, you need to choose the position of the service center [xcentre, ycentre] such that the following formula is minimized:

Answers within 10-5 of the actual value will be accepted.

Example 1:

Input: positions = [[0,1],[1,0],[1,2],[2,1]]
Output: 4.00000
Explanation: As shown, you can see that choosing [xcentre, ycentre] = [1, 1] will make the distance to each customer = 1, the sum of all distances is 4 which is the minimum possible we can achieve.
Example 2:

Input: positions = [[1,1],[3,3]]
Output: 2.82843
Explanation: The minimum possible sum of distances = sqrt(2) + sqrt(2) = 2.82843
 

Constraints:

1 <= positions.length <= 50
positions[i].length == 2
0 <= xi, yi <= 100
'''


from typing import List, Tuple
from math import sqrt


class Solution:
  def getMinDistSum(self, positions: List[List[int]]) -> float:
    """
    This algorithm approximates a solution using 
    gradient descent with an adaptive learning rate.
    """
    # Get the number of positions
    n = len(positions)

    # Floating point safety padding
    eps = 1e-16

    # Compute the gradient of the distance function
    def grad(x: float, y: float) -> Tuple[float, float]:
      # Compute the Distances
      all_dist = [sqrt((x0 - x)**2 + (y0 - y)**2) for x0, y0 in positions]

      # Compute the gradient: `dx / sqrt(dx*dx+dy*dy)` and `dy / sqrt(dx*dx+dy*dy)`
      dx = sum((x-pt[0]) / (all_dist[i]+eps) for i, pt in enumerate(positions))
      dy = sum((y-pt[1]) / (all_dist[i]+eps) for i, pt in enumerate(positions))

      # Return everything
      return sum(all_dist), dx, dy

    # Compute the center of mass (initial guess)
    x = sum(pt[0] for pt in positions) / n
    y = sum(pt[1] for pt in positions) / n

    # Iterate gradient descent until the required precision is achieved
    dist, dx, dy = grad(x, y)
    alpha = 0.5 / sqrt(dx*dx + dy*dy + eps)
    last_dist = dist + 1
    last_x, last_y = x, y
    
    while abs(last_dist - dist) > 5e-7:
      # Save the current position
      last_dist, last_x, last_y = dist, x, y

      # Apply gradient descent
      x -= alpha * dx
      y -= alpha * dy

      # Compute the new cost / gradient
      dist, dx, dy = grad(x, y)

      # Decrease the learning rate if we over-shoot
      while dist > last_dist:
        # Decrease the learning rate
        alpha *= 0.5

        # update the position and move back a little bit
        x = (x + last_x) / 2
        y = (y + last_y) / 2

        # Compute the new distance/gradient
        dist, dx, dy = grad(x, y)

      #Increase the Learning Rate
      alpha *= 1.2

    #Return the Solution
    return dist
      
  
  def getMinDistSum0(self, positions: List[List[int]]) -> float:
    if len(positions) == 1:
      return 0
    
    def dist_sum(x: int, y: int) -> int:
      total = 0
      for x0, y0 in positions:
        total += sqrt((x-x0)*(x-x0) + (y-y0)*(y-y0))
      
      return total
    
    if len(positions) == 2:
      x = (positions[0][0] + positions[1][0]) / 2.0
      y = (positions[0][1] + positions[1][1]) / 2.0
      return dist_sum(x, y)

    n = len(positions)
    lower_limit = 0.0001
    step = 1000.0
    
    curr_x = sum(pt[0] for pt in positions) / n
    curr_y = sum(pt[1] for pt in positions) / n
    dist = dist_sum(curr_x, curr_y)
    # print('init', curr_x, curr_y, dist)

    for x, y in positions:
      d0 = dist_sum(x, y)
      if d0 < dist:
        dist = d0
        curr_x = x
        curr_y = y

    while step > lower_limit:
      found = False
      
      for dx, dy in [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, 1), (0, -1)]:
        x0 = curr_x + dx * step
        y0 = curr_y + dy * step
        d0 = dist_sum(x0, y0)
        # print('new step', step, x0, y0, d0)
        
        if d0 < dist:
          dist = d0
          curr_x = x0
          curr_y = y0
          found = True
          break
      
      if not found:
        step /= 2.0
        
    # print(curr_x, curr_y, step)
    return dist
  