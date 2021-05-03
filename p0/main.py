from p0.StringToInteger_8 import Solution8

def execute(problem: int) -> None:
  solution = None

  if problem == -1:
    print("p1 done", problem)

  if problem == 8:
    solution = Solution8()

  if solution is not None:
    solution.test()
    return

  print("Unknown problem number: ", problem)
