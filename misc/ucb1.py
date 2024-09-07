import math

class UCB1():
    def __init__(self, counts, values):
      self.counts = counts # Count represent counts of pulls for each arm. For multiple arms, this will be a list of counts.
      self.values = values # Value represent average reward for specific arm. For multiple arms, this will be a list of values.
      return

    # Initialise k number of arms
    def initialize(self, n_arms):
      self.counts = [0 for _ in range(n_arms)]
      self.values = [0.0 for _ in range(n_arms)]
      return
    
    # UCB arm selection based on max of UCB reward of each arm
    def select_arm(self):
      n_arms = len(self.counts)
      for arm in range(n_arms):
        if self.counts[arm] == 0:
          return arm
  
      ucb_values = [0.0 for _ in range(n_arms)]
      total_counts = sum(self.counts)
      
      for arm in range(n_arms):
        bonus = math.sqrt((2 * math.log(total_counts)) / float(self.counts[arm]))
        ucb_values[arm] = self.values[arm] + bonus

      return ucb_values.index(max(ucb_values))
    
    # Choose to update chosen arm and reward
    def update(self, chosen_arm, reward):
      self.counts[chosen_arm] += 1
      n = self.counts[chosen_arm]
      
      # Update average/mean value/reward for chosen arm
      value = self.values[chosen_arm]
      new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
      self.values[chosen_arm] = new_value
      return