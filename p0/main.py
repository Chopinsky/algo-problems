from p0.StringToInteger_8 import Solution8
from p0.WildcardMatching_44 import Solution44

def execute(problem: int) -> None:
  solution = None

  if problem == -1:
    print("p1 done", problem)

  if problem == 8:
    solution = Solution8()

  if problem == 44:
    solution = Solution44()

  if solution is not None:
    solution.test()
    return

  print("Unknown problem number: ", problem)
