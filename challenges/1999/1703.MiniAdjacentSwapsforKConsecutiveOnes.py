'''
You are given an integer array, nums, and an integer k. nums comprises of only 0's and 1's. In one move, you can choose two adjacent indices and swap their values.

Return the minimum number of moves required so that nums has k consecutive 1's.

Example 1:

Input: nums = [1,0,0,1,0,1], k = 2
Output: 1
Explanation: In 1 move, nums could be [1,0,0,0,1,1] and have 2 consecutive 1's.

Example 2:

Input: nums = [1,0,0,0,0,0,1,1], k = 3
Output: 5
Explanation: In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0,1,1,1].

Example 3:

Input: nums = [1,1,0,1], k = 2
Output: 0
Explanation: nums already has 2 consecutive 1's.
 

Constraints:

1 <= nums.length <= 105
nums[i] is 0 or 1.
1 <= k <= sum(nums)
'''


class Solution:
  '''
  the trick for both solutions rely on the fact that the min-move for 
  an array of 1s at index arr=[i0, i1, ..., iN] happens at moving index
  to the left and right of arr[N//2] towards this index.
  '''
  
  def minMoves(self, nums: List[int], k: int) -> int:
    idx = [i for i, num in enumerate(nums) if num]
    prefix = list(accumulate([0] + idx))
    ans = float('inf')
    
    # print(idx)
    # print(prefix)

    for i in range(len(idx)-k+1):
        ans = min(
          ans, 
          prefix[i+k] - prefix[i+k//2] - prefix[i+(k+1)//2] + prefix[i]
        )
        
    return ans - (k//2) * ((k+1)//2)
      
    
  def minMoves0(self, nums: List[int], k: int) -> int:
    if k == 1:
      return 0
    
    ones = []
    base = 0
    
    for i, n in enumerate(nums):
      if n == 1:
        if 1 <= len(ones) < k:
          base += i - ones[0] - len(ones)     
          
        ones.append(i)
        if len(ones) >= k and ones[-1] - ones[-k] == k-1:
          return 0
    
    ln = len(ones)
    if k == 2:
      return min([ones[i]-ones[i-1]-1 for i in range(1, ln)])
    
    lst = deque(ones[:k])
    n = 0
    m = k-n

    while n < m-2:
      n += 1
      m -= 1
      base += (lst[n]-lst[n-1]-1) * (n-m)
    
    if base == 0:
      return 0
    
    # print('init:', lst, n, base)
    
    ans = base
    n += 1
    
    for i in range(k, ln):
      num = ones[i]
      
      '''
      if n == 1:
        # shift right, reduce numbers of moves to the left most 1
        base -= (k-1) * (lst[1]-lst[0]-1)
        lst.popleft()
        
        # adding the new 1 to the list
        base += (num-lst[1]) - (k-1)
        lst.append(num)
        
      else:
      '''
      
      # remove the leftmost 1, reduce it from the total steps
      base -= (lst[n-1]-lst[0]) - (n-1)
      lst.popleft()
      n -= 1

      # adding the new 1 to the list
      base += (num-lst[n-1]) - (k-n)
      lst.append(num)
        
      # optimizing the moves the 1s in the list shall make to be 
      # consecutive
      m = k-n
      base += (lst[n]-lst[n-1]-1) * (n-m)
      n += 1
      
      # print(i, '--', lst, n, base)
      
      ans = min(ans, base)
      if ans == 0:
        return 0
    
    return ans
  
