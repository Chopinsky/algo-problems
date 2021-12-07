'''
here is a donuts shop that bakes donuts in batches of batchSize. They have a rule where they must serve all of the donuts of a batch before serving any donuts of the next batch. You are given an integer batchSize and an integer array groups, where groups[i] denotes that there is a group of groups[i] customers that will visit the shop. Each customer will get exactly one donut.

When a group visits the shop, all customers of the group must be served before serving any of the following groups. A group will be happy if they all get fresh donuts. That is, the first customer of the group does not receive a donut that was left over from the previous group.

You can freely rearrange the ordering of the groups. Return the maximum possible number of happy groups after rearranging the groups.

Example 1:

Input: batchSize = 3, groups = [1,2,3,4,5,6]
Output: 4
Explanation: You can arrange the groups as [6,2,4,5,1,3]. Then the 1st, 2nd, 4th, and 6th groups will be happy.
Example 2:

Input: batchSize = 4, groups = [1,3,2,5,2,2,1,6]
Output: 4
 

Constraints:

1 <= batchSize <= 9
1 <= groups.length <= 30
1 <= groups[i] <= 109
'''


class Solution:
  def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
    # get the remainder counters
    freq = Counter(g % batchSize for g in groups)
    # print('before', freq, n)
    
    # remove the groups that are happy by themselves from the equation
    ans = freq[0]
    freq[0] = 0
    
    # matching rem-i with rem-(batchSize-i), where the pair will
    # yield at least 1 happy group, and still let the next group
    # yield 1 happy group as well
    for i in range(1, batchSize):
      if i + i == batchSize:
        cnt = freq[i] // 2
      else:
        cnt = min(freq[i], freq[batchSize-i])

      freq[i] -= cnt
      freq[batchSize-i] -= cnt
      ans += cnt
    
    # print('after', freq, n, ans)
    cache = {}
    base = sorted(freq)
    n = sum(freq.values())
    
    def dp(cnt: int, leftover: int) -> int:
      if cnt >= n:
        return 0
      
      key = ','.join(str(freq[val]) for val in base)
      if (leftover, key) in cache:
        return cache[leftover, key]
      
      best_count = 0
      
      for i in base:
        if not freq[i]:
          continue
          
        freq[i] -= 1
        cnt = dp(cnt+1, (leftover+i) % batchSize) + (1 if not leftover else 0)
        best_count = max(best_count, cnt)
        freq[i] += 1
        
      cache[leftover, key] = best_count
      return best_count
    
    return ans + dp(0, 0)
    
    
  def maxHappyGroups0(self, batchSize: int, groups: List[int]) -> int:
    n = len(groups)
    freq = [0] * batchSize
    fp = [0] * batchSize
    
    for g in groups:
      mod = g % batchSize
      freq[mod] += 1
    
    for i in range(1, batchSize):
      fp[i] += fp[i-1] + freq[i-1]
    
    cache = {}
    
    # @lru_cache(None)
    def dp(cnt: int, leftover: int, mask: int) -> int:
      if cnt >= n:
        return 0
      
      # key = ','.join(str(f) for f in freq)
      if (leftover, mask) in cache:
        return cache[leftover, mask]
      
      best_count = 0
      
      for i in range(1, batchSize):
        if not freq[i]:
          continue
          
        freq[i] -= 1
        fp[i] += 1
        
        cnt = dp(cnt+1, (leftover+i) % batchSize, mask | (1<<fp[i])) + (1 if not leftover else 0)
        best_count = max(best_count, cnt)
        
        freq[i] += 1
        fp[i] -= 1
        
      cache[leftover, mask] = best_count
      return best_count
    
    return freq[0] + dp(0, 0, 0)
  
