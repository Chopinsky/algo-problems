from p1.FrequencyOfTheMostFrequentElement1838 import Solution1838

def execute(problem: int) -> None:
  solution = None

  if problem == -1:
    print("p1 done", problem)

  if problem == 1838:
    solution = Solution1838()

  if solution is not None:
    solution.test()
    return

  print("Unknown problem number: ", problem)
