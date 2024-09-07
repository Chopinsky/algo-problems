from scipy.stats import beta

class ThompsonSampling():
  def __init__(self, counts, values, a, b):
    self.counts = counts
    self.values = values
    
    # Beta parameters
    self.a = a
    self.b = b
    return

  def initialize(self, n_arms: int):
    self.counts = [0 for _ in range(n_arms)]
    self.values = [0.0 for _ in range(n_arms)]

    # Uniform distribution of prior beta (A,B)
    self.a = [1 for _ in range(n_arms)]
    self.b = [1 for _ in range(n_arms)]
    return
  
  def select_arm(self):
    # Pair up all beta params of a and b for each arm
    beta_params = zip(self.a, self.b)
    
    # Perform random draw for all arms based on their params (a,b)
    all_draws = [beta.rvs(i[0], i[1], size = 1) for i in beta_params]
      
    # return index of arm with the highest draw
    return all_draws.index(max(all_draws))
  
  def update(self, chosen_arm, reward):
    self.counts[chosen_arm] = self.counts[chosen_arm] + 1
    n = self.counts[chosen_arm]
    
    value = self.values[chosen_arm]
    new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
    self.values[chosen_arm] = new_value
    
    # Update a and b
    
    # a is based on total counts of rewards of arm
    self.a[chosen_arm] = self.a[chosen_arm] + reward
    
    # b is based on total counts of failed rewards on arm
    self.b[chosen_arm] = self.b[chosen_arm] + (1-reward)
    
    return
    