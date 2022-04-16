'''
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

Example 1:

Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
Example 2:

Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
Example 3:

Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".

Constraints:

n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
All the values of recipes and supplies combined are unique.
Each ingredients[i] does not contain any duplicate values.
'''

from typing import List
from collections import defaultdict


class Solution:
  def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    n = len(recipes)
    s = set(supplies)
    
    dep = defaultdict(list)
    g = defaultdict(list)
    c = defaultdict(int)
    r = set(recipes)
    res = set()
    
    for f, ing in zip(recipes, ingredients):
      dep[f] = ing
      
      for i in ing:
        if i not in r:
          continue
          
        g[i].append(f)
        c[f] += 1
        
    stack = [f for f in r if c[f] == 0]
    idx = 0
    # print(stack, c)
    
    while idx < len(stack):
      f = stack[idx]
      # print(f, dep[f])
      
      if (f not in dep) or (f in res):
        idx += 1
        continue
      
      done = True
      for d in dep[f]:
        if d not in s:
          done = False
          break
        
      dep.pop(f, None)
      if not done:
        idx += 1
        continue
        
      res.add(f)
      s.add(f)
      
      for i in g[f]:
        c[i] -= 1
        if c[i] == 0:
          stack.append(i)
      
      idx += 1
      
    return list(res)
    