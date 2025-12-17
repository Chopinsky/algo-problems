'''
3562-maximum-profit-from-trading-stocks-with-discounts
'''

from typing import List


class Solution:
  def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
    # 建图：构建邻接表
    adj = [[] for _ in range(n + 1)]
    for u, v in hierarchy:
      adj[u].append(v)
    
    # 调整数组索引，使员工 ID 直接对应索引（题目ID从1开始）
    # present 和 future 是从索引 0 开始的，对应 ID 1
    # 所以 ID i 对应 present[i-1]
    
    # 树形 DP 函数
    # 返回值: (dp_no_discount, dp_with_discount)
    # dp_no_discount: 假设当前节点 u 的父节点没买（u 需要原价），u 子树在不同 budget 下的最大利润
    # dp_with_discount: 假设当前节点 u 的父节点买了（u 可以半价），u 子树在不同 budget 下的最大利润
    # 每个 dp 是一个列表，索引是 cost，值是 profit。初始化为 -1 表示不可达，0处为0。
    def dfs(u: int) -> tuple[list[int], list[int]]:
      # 1. 首先合并所有子节点的结果
      #我们需要两个背包状态：
      # `child_sum_if_u_bought`: u 买了，子节点都能享受折扣 (即取子节点的 dp_with_discount 进行合并)
      # `child_sum_if_u_skip`: u 没买，子节点都不能享受折扣 (即取子节点的 dp_no_discount 进行合并)
      
      # 初始化背包：花费0，利润0
      # 使用 list 也就是数组来模拟 map，因为 budget 很小
      # 索引为 cost, 值为 profit
      
      child_sum_if_u_bought = [-1] * (budget + 1)
      child_sum_if_u_bought[0] = 0
      
      child_sum_if_u_skip = [-1] * (budget + 1)
      child_sum_if_u_skip[0] = 0
      
      for v in adj[u]:
        v_no_disc, v_with_disc = dfs(v)
        
        # 分组背包合并 - 情况1: u 买了，v 享受折扣 (v_with_disc)
        next_bought = [-1] * (budget + 1)
        for c1 in range(budget + 1):
          if child_sum_if_u_bought[c1] == -1: 
            continue

          for c2 in range(budget + 1 - c1):
            if v_with_disc[c2] == -1: 
              continue
            
            next_bought[c1 + c2] = max(
              next_bought[c1 + c2], 
              child_sum_if_u_bought[c1] + v_with_disc[c2],
            )

        child_sum_if_u_bought = next_bought
        
        # 分组背包合并 - 情况2: u 没买，v 无折扣 (v_no_disc)
        next_skip = [-1] * (budget + 1)
        for c1 in range(budget + 1):
          if child_sum_if_u_skip[c1] == -1: 
            continue
          
          for c2 in range(budget + 1 - c1):
            if v_no_disc[c2] == -1: 
              continue
            
            next_skip[c1 + c2] = max(
              next_skip[c1 + c2], 
              child_sum_if_u_skip[c1] + v_no_disc[c2],
            )

        child_sum_if_u_skip = next_skip

      # 2. 计算当前节点 u 的返回结果
      # u 的基本数据
      idx = u - 1
      price_full = present[idx]
      price_half = math.floor(price_full / 2)
      # 如果利润是负的，还是有可能买（虽然本题 future > present 通常，但如果 future < present 就不应该买）
      # 题目只需 max profit，如果不买利润是0。如果买了亏本，不如不买。
      # 题目逻辑：profit = future - cost。
      
      prof_full = future[idx] - price_full
      prof_half = future[idx] - price_half
      
      # 结果数组
      res_no_discount = [-1] * (budget + 1)
      res_with_discount = [-1] * (budget + 1)
      
      # --- 填充 res_no_discount (u 的父节点没买) ---
      # 选项 A: u 也不买 -> 利润来源于 child_sum_if_u_skip
      for c in range(budget + 1):
        if child_sum_if_u_skip[c] != -1:
          res_no_discount[c] = max(res_no_discount[c], child_sum_if_u_skip[c])
      
      # 选项 B: u 原价买 -> 利润来源于 prof_full + child_sum_if_u_bought
      if prof_full > 0: 
        # 只有利润 > 0 才考虑买 (或者根据题目逻辑，只要合法就买？通常最大利润不买亏本货)
        # 修正：即使当前单个股票亏本，但为了给子节点打折获得更大总收益，也可能买。
        # 但是这里的 profit 定义已经是净利润了。
        for c in range(budget + 1 - price_full):
          if child_sum_if_u_bought[c] != -1:
            res_no_discount[c + price_full] = max(
              res_no_discount[c + price_full], 
              child_sum_if_u_bought[c] + prof_full,
            )

      else:
        # 即使当前亏本，也可能为了子节点买。需遍历。
        # 实际上只要 budget 够就可以买
        if price_full <= budget:
          for c in range(budget + 1 - price_full):
            if child_sum_if_u_bought[c] != -1:
              res_no_discount[c + price_full] = max(
                res_no_discount[c + price_full], 
                child_sum_if_u_bought[c] + prof_full,
              )

      # --- 填充 res_with_discount (u 的父节点买了) ---
      # 选项 A: u 不买 -> 利润来源于 child_sum_if_u_skip (注意：u不买，u的子节点就没折扣，这和u父节点是否买无关)
      for c in range(budget + 1):
        if child_sum_if_u_skip[c] != -1:
          res_with_discount[c] = max(
            res_with_discount[c], 
            child_sum_if_u_skip[c],
          )
      
      # 选项 B: u 半价买 -> 利润来源于 prof_half + child_sum_if_u_bought
      # 只要 budget 够就可以买
      if price_half <= budget:
        for c in range(budget + 1 - price_half):
          if child_sum_if_u_bought[c] != -1:
            res_with_discount[c + price_half] = max(
              res_with_discount[c + price_half], 
              child_sum_if_u_bought[c] + prof_half,
            )
      
      return res_no_discount, res_with_discount

    # CEO 是 1 号员工，作为根节点
    # 对于根节点，它没有父节点，所以只能取 dp_no_discount 的结果
    final_dp, _ = dfs(1)
    
    return max(final_dp)

  def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
    tree = [[] for _ in range(n)]
    dp = [[[0]*(budget+1) for _ in range(2)] for _ in range(n)]

    for u, v in hierarchy:
      tree[u-1].append(v-1)

    def dfs(u: int):
      children = tree[u]
      dps = []

      for v in children:
        dfs(v)
        dps.append((dp[v][0], dp[v][1]))

      for bot in range(2):
        price = present[u]//2 if bot else present[u]
        profit = future[u] - price
        
        # Option 1: not buying u
        base = [0]*(budget+1)
        for c0, _ in dps:
          nxt = [0]*(budget+1)
          for b in range(budget+1):
            if base[b] == 0 and b != 0:
              continue

            for k in range(budget-b+1):
              nxt[b+k] = max(nxt[b+k], base[b] + c0[k])

          base = nxt

        curr = base[:]

        # Option 2: buying u
        if price <= budget:
          base = [0]*(budget+1)
          for _, c1 in dps:
            nxt = [0]*(budget+1)
            for b in range(budget+1):
              if base[b] == 0 and b != 0:
                continue

              for k in range(budget-b+1):
                nxt[b+k] = max(nxt[b+k], base[b] + c1[k])

            base = nxt

          for b in range(price, budget+1):
            curr[b] = max(curr[b], base[b-price]+profit)

        dp[u][bot] = curr

    dfs(0)
    
    return max(dp[0][0])
