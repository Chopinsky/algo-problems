'''
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

 

Example 1:


Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Example 2:


Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Example 3:


Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Example 4:


Input: board = [[3,2,4],[1,5,0]]
Output: 14

Constraints:

board.length == 2
board[i].length == 3
0 <= board[i][j] <= 5
Each value board[i][j] is unique.
'''


from typing import List


class Solution:
  def slidingPuzzle(self, board: List[List[int]]) -> int:
    curr, nxt = [tuple(board[0]+board[1])], []
    seen = set(curr)
    steps = 0
    target = (1, 2, 3, 4, 5, 0)
    # print('init:', seen)
        
    def find_nxt(s, nxt):
      idx = s.index(0)
      arr = list(s)
      
      # swap to right
      if idx != 2 and idx != 5:
        arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
        s0 = tuple(arr)
        if s0 not in seen:
          seen.add(s0)
          nxt.append(s0)
          
        arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
        
      # swap to left
      if idx != 0 and idx != 3:
        arr[idx], arr[idx-1] = arr[idx-1], arr[idx]
        s1 = tuple(arr)
        if s1 not in seen:
          seen.add(s1)
          nxt.append(s1)
        
        arr[idx], arr[idx-1] = arr[idx-1], arr[idx]
        
      # swap to below
      if idx < 3:
        arr[idx], arr[idx+3] = arr[idx+3], arr[idx]
        s2 = tuple(arr)
        if s2 not in seen:
          seen.add(s2)
          nxt.append(s2)
        
        arr[idx], arr[idx+3] = arr[idx+3], arr[idx]
      
      # swap to above
      if idx >= 3:
        arr[idx], arr[idx-3] = arr[idx-3], arr[idx]
        s3 = tuple(arr)
        if s3 not in seen:
          seen.add(s3)
          nxt.append(s3)
        
        arr[idx], arr[idx-3] = arr[idx-3], arr[idx]
        
    while curr:
      # print('iter:', steps, curr)
      for s in curr:
        if s == target:
          return steps
        
        find_nxt(s, nxt)
      
      curr, nxt = nxt, curr
      nxt.clear()
      steps += 1
    
    # all states iterated, not solved
    return -1
      
  def slidingPuzzle(self, board: List[List[int]]) -> int:
    b = board[0] + board[1]
    target = (1, 2, 3, 4, 5, 0)
    if tuple(b) == target:
      return 0
    
    idx = 0
    while b[idx]:
      idx += 1
      
    q, nxt = [(idx, b)], []
    seen = set([tuple(b)])
    step = 1
    # print(q, seen)
    
    def update(idx: int, moved: List[int], shift: int) -> bool:
      if tuple(moved) == (4,1,2,0,5,3):
        print('at', moved, shift)
        
      moved[idx], moved[idx+shift] = moved[idx+shift], moved[idx]
      moved_hash = tuple(moved)

      if moved_hash == target:
        return True

      if moved_hash not in seen:
        seen.add(moved_hash)
        nxt.append((idx+shift, moved))
        
      return False
    
    while q:
      for idx, src in q:
        # moving to the right
        if idx != 2 and idx != 5:
          if update(idx, src.copy(), 1):
            return step

        # moving to the left
        if idx != 0 and idx != 3:
          if update(idx, src.copy(), -1):
            return step

        # moving down or up
        if update(idx, src.copy(), 3 if idx < 3 else -3):
          return step
          
      q, nxt = nxt, q
      nxt.clear()
      step += 1
      # print(step, q)
    
    return -1
