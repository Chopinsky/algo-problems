class Solution:
  def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    max_time = minutesToTest/minutesToDie + 1
    
    # Initialize the required minimum number of pigs...
    req_pigs = 0
    
    # To find the minimum number of pigs, find the minimum req_pigs such that Math.pow(max_time, req_pigs) >= buckets...
    while (max_time) ** req_pigs < buckets:
      # Increment until it will be greater or equals to bucket...
      req_pigs += 1
      
    # Return the required minimum number of pigs...
    return 
  