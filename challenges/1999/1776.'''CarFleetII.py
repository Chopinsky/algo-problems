'''
There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:

positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.

Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10-5 of the actual answers are accepted.

Example 1:

Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.

Example 2:

Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]

Constraints:

1 <= cars.length <= 10^5
1 <= positioni, speedi <= 10^6
positioni < positioni+1
'''


class Solution:
  def getCollisionTimes0(self, cars: List[List[int]]) -> List[float]:
    n = len(cars)
    ans = [-1.0] * n
    stack = [(cars[-1][0], cars[-1][1])]
    
    def collision(p0: int, s0: int, p1: int, s1: int) -> float:
      if s0 <= s1:
        return float('inf')
      
      return (p1-p0) / (s0-s1)
    
    for i in range(n-2, -1, -1):
      p0, s0 = cars[i]
      # print(i, s0, p0, stack)
      
      # no collisions
      if not stack:
        stack.clear()
      
      else:
        while len(stack) >= 2 and collision(p0, s0, stack[-1][0], stack[-1][1]) >= collision(p0, s0, stack[-2][0], stack[-2][1]):
          stack.pop()
          
        if s0 > stack[-1][1]:
          ans[i] = collision(p0, s0, stack[-1][0], stack[-1][1])
      
      stack.append((p0, s0))
    
    # print(stack)
    return ans
  
  def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
    if not cars:
      return []
    
    n = len(cars)
    ans = [-1.0] * n
    stack = deque([])
    
    for i in range(n-1, -1, -1):
      p0, s0 = cars[i]
      
      while stack:
        j = stack[-1]
        p1, s1 = cars[j]

        # this one is fast, it must have collided with previous 
        # cars first
        if s1 >= s0:
          stack.pop()
          continue
          
        time = (p1 - p0) / (s0 - s1)
        
        # this one has already collided, skip it since it's merged with
        # the car it runs into already
        if ans[j] >= 0 and ans[j] < time:
          stack.pop()
          continue
          
        ans[i] = time
        break
        
      # done, add the car to the queue
      stack.append(i)
      
    return ans
