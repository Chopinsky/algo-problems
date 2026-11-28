def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
  dp = [0] * (capacity + 1)
  for i, weight in enumerate(weights):
    value = values[i]
    for c in range(capacity, weight-1, -1):
      dp[c] = max(dp[c], dp[c-weight] + value)

  return dp[capacity]

print(knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5))
