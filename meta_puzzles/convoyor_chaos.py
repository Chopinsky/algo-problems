from collections import defaultdict
from typing import List
from sortedcontainers import SortedSet
from convoyor_chaos_solution import solution


def build_start_end(n: int, h: List[int], a: List[int], b: List[int]):
  start = []
  end = []

  for i in range(n):
    start.append((a[i], h[i], i))
    end.append((b[i], h[i], i))

  start.sort()
  end.sort()

  return start, end


def build_graph(n: int, h: List[int], a: List[int], b: List[int]):
  hmap, hid = SortedSet(), {}
  add, remove = [], []
  start, end = build_start_end(n, h, a, b)
  graph = {}

  s0, e0 = 0, 0

  # print('start:', start, '| end:', end)
  for x in range(1000000+1):
    # add convoyors in range
    for y, i in add:
      hmap.add(y)
      hid[y] = i

    add.clear()

    # remove convoyors out of the range
    while e0 < n and end[e0][0] <= x:
      _, y, i = end[e0]
      hmap.discard(y)
      del hid[y]
      remove.append((y, i))
      e0 += 1

    # push convoyors coming into the range
    while s0 < n and start[s0][0] <= x:
      _, y, i = start[s0]
      add.append((y, i))
      hdx = hmap.bisect_left(y)-1
      if hdx >= 0:
        y0 = hmap[hdx]
        j = (hid[y0], a[i])
      
      else:
        # j: (index, fall position)
        j = (-1, -1)

      # left side of i-th will drop onto j-th convoyor
      s0 += 1
      graph[i] = {
        'idx': i,
        'c': [j],
        'x': [a[i], b[i]],
        'y': h[i],
        'weight': 0,
        'costs': [0, 0],
      }

    # connect right side
    for y, i in remove:
      hdx = hmap.bisect_left(y)-1
      if hdx >= 0:
        y0 = hmap[hdx]
        j = (hid[y0], b[i])
      else:
        j = (-1, -1)

      graph[i]['c'].append(j)

    remove.clear()

  return graph


def getMinExpectedHorizontalTravelDistance(n: int, h: List[int], a: List[int], b: List[int]) -> float:
  # build the graph
  graph = build_graph(n, h, a, b)
  intervals = sorted(list(elem for elem in graph.values()), key=lambda x: x['y'])
  print(graph, intervals)

  def get_width(idx):
    return graph[idx]['x'][1] - graph[idx]['x'][0]

  def get_middle(idx):
    return sum(graph[idx]['x']) / 2.0
  
  #todo

  return 0.0


def get_test_cases():
  return [
    {
      'N': 2,
      'H': [10, 20],
      'A': [100000, 400000],
      'B': [600000, 800000],
      'ans': 155000.00,
    },
    {
      'N': 5,
      'H': [2, 8, 5, 9, 4],
      'A': [5000, 2000, 7000, 9000, 0],
      'B': [7000, 8000, 11000, 11000, 4000],
      'ans': 36.50,
    }
  ]

def main(peek=False):
  testCases = get_test_cases()
  for testCase in testCases:
    print('='*10)
    print(testCase)

    if peek:
      print(solution(
        testCase['N'],
        testCase['H'],
        testCase['A'],
        testCase['B'],
      ))
    else:
      print(getMinExpectedHorizontalTravelDistance(
        testCase['N'],
        testCase['H'],
        testCase['A'],
        testCase['B'],
      ))

  print('='*10)
  print('all done ...')

# peek = True
peek = False
main(peek)
