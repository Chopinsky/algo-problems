'''
3224. Minimum Array Changes to Make Differences Equal
'''

class Solution:
  def minChanges(self, nums, k):
    n = len(nums)             
    change_count = [0] * (k + 2)  
    change_count[0] = n // 2

    for i in range(n // 2):
      left = nums[i]
      right = nums[n - i - 1]
      cur_diff = abs(left - right)
      
      # left->0; left->k; right->0; right->k;
      max_diff = max(left, right, k - left, k - right)

      # [curr_diff, curr_diff+1) requires no change
      change_count[cur_diff] -= 1
      change_count[cur_diff + 1] += 1
      
      # [curr_diff+1, max_diff] requires 1 change, [max_diff+1, k+1]
      # requires 2 changes
      change_count[max_diff + 1] += 1

    cur_changes = 0
    min_changes = n // 2
    for i in range(k + 1):
      cur_changes += change_count[i]
      min_changes = min(min_changes, cur_changes)

    return min_changes
  