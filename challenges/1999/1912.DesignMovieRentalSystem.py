'''
You have a movie renting company consisting of n shops. You want to implement a renting system that supports searching for, booking, and returning movies. The system should also support generating a report of the currently rented movies.

Each movie is given as a 2D integer array entries where entries[i] = [shopi, moviei, pricei] indicates that there is a copy of movie moviei at shop shopi with a rental price of pricei. Each shop carries at most one copy of a movie moviei.

The system should support the following functions:

Search: Finds the cheapest 5 shops that have an unrented copy of a given movie. The shops should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopi should appear first. If there are less than 5 matching shops, then all of them should be returned. If no shop has an unrented copy, then an empty list should be returned.
Rent: Rents an unrented copy of a given movie from a given shop.
Drop: Drops off a previously rented copy of a given movie at a given shop.
Report: Returns the cheapest 5 rented movies (possibly of the same movie ID) as a 2D list res where res[j] = [shopj, moviej] describes that the jth cheapest rented movie moviej was rented from the shop shopj. The movies in res should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopj should appear first, and if there is still tie, the one with the smaller moviej should appear first. If there are fewer than 5 rented movies, then all of them should be returned. If no movies are currently being rented, then an empty list should be returned.
Implement the MovieRentingSystem class:

MovieRentingSystem(int n, int[][] entries) Initializes the MovieRentingSystem object with n shops and the movies in entries.
List<Integer> search(int movie) Returns a list of shops that have an unrented copy of the given movie as described above.
void rent(int shop, int movie) Rents the given movie from the given shop.
void drop(int shop, int movie) Drops off a previously rented movie at the given shop.
List<List<Integer>> report() Returns a list of cheapest rented movies as described above.
Note: The test cases will be generated such that rent will only be called if the shop has an unrented copy of the movie, and drop will only be called if the shop had previously rented out the movie.

Example 1:

Input
["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
[[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]
Output
[null, [1, 0, 2], null, null, [[0, 1], [1, 2]], null, [0, 1]]

Explanation
MovieRentingSystem movieRentingSystem = new MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]);
movieRentingSystem.search(1);  // return [1, 0, 2], Movies of ID 1 are unrented at shops 1, 0, and 2. Shop 1 is cheapest; shop 0 and 2 are the same price, so order by shop number.
movieRentingSystem.rent(0, 1); // Rent movie 1 from shop 0. Unrented movies at shop 0 are now [2,3].
movieRentingSystem.rent(1, 2); // Rent movie 2 from shop 1. Unrented movies at shop 1 are now [1].
movieRentingSystem.report();   // return [[0, 1], [1, 2]]. Movie 1 from shop 0 is cheapest, followed by movie 2 from shop 1.
movieRentingSystem.drop(1, 2); // Drop off movie 2 at shop 1. Unrented movies at shop 1 are now [1,2].
movieRentingSystem.search(2);  // return [0, 1]. Movies of ID 2 are unrented at shops 0 and 1. Shop 0 is cheapest, followed by shop 1.
 

Constraints:

1 <= n <= 3 * 105
1 <= entries.length <= 105
0 <= shopi < n
1 <= moviei, pricei <= 104
Each shop carries at most one copy of a movie moviei.
At most 105 calls in total will be made to search, rent, drop and report.

'''


from heapq import *

def is_smaller(a: List[int], b: List[int]) -> bool:
  if a[2] < b[2]:
    return True
  
  if a[2] == b[2] and a[0] < b[0]:
    return True
  
  if a[2] == b[2] and a[0] == b[0]:
    return a[1] < b[1]
  
  return False
  
  
def remove(arr: List[List[int]], dic, idx: int) -> Optional[List[int]]:
  last = len(arr)-1
  if not arr or last < 0:
    return None

  arr[last], arr[idx] = arr[idx], arr[last]
  data = arr.pop()
  dic.pop((data[0], data[1]), None)

  if idx == last:
    return data

  if dic:
    dic[arr[idx][0], arr[idx][1]] = idx

  siftdown(arr, dic, idx)
  siftup(arr, dic, idx)

  return data


def insert(arr: List[List[int]], dic, src: List[int]):
  idx = len(arr)
  arr.append(src)
  dic[arr[idx][0], arr[idx][1]] = idx
  siftup(arr, dic, idx)


def siftdown(arr: List[List[int]], dic, idx: int):
  while idx < len(arr):
    curr = idx
    l, r = 2*idx+1, 2*idx+2

    if l < len(arr) and is_smaller(arr[l], arr[idx]):
      idx = l

    if r < len(arr) and is_smaller(arr[r], arr[idx]):
      idx = r

    if curr == idx:
      break

    arr[curr], arr[idx] = arr[idx], arr[curr]
    dic[arr[idx][0], arr[idx][1]] = idx
    dic[arr[curr][0], arr[curr][1]] = curr

  return


def siftup(arr: List[List[int]], dic, idx: int):
  while idx > 0:
    p = (idx-1) >> 1
    if is_smaller(arr[p], arr[idx]):
      break

    arr[p], arr[idx] = arr[idx], arr[p]
    dic[arr[idx][0], arr[idx][1]] = idx
    dic[arr[p][0], arr[p][1]] = p
    idx = p

  return
  

class MovieRentingSystem0:
  def __init__(self, n: int, entries: List[List[int]]):
    self.rented = defaultdict(int)
    self.r_shelf = []
    self.stock = defaultdict(int)
    self.s_shelf = defaultdict(list)
    
    for e in entries:
      # print(s, m, p)
      insert(self.s_shelf[e[1]], self.stock, e)


  def search(self, movie: int) -> List[int]:
    backup = []
    rpt = []
    
    # rpt_full = sorted(self.s_shelf[movie][:8].copy(), key=lambda x: x[2])
    # for s, _, _ in rpt_full[:5]:
    #   rpt.append(s)
    
    while self.s_shelf and len(rpt) < 5:
      data = remove(self.s_shelf[movie], self.stock, 0)
      if not data:
        break
        
      backup.append(data)
      rpt.append(data[0])
      
    for e in backup:
      insert(self.s_shelf[movie], self.stock, e)
      
    # print("search", rpt)
      
    return rpt


  def rent(self, shop: int, movie: int) -> None:
    if (shop, movie) not in self.stock:
      return
    
    idx = self.stock[shop, movie]
    data = remove(self.s_shelf[movie], self.stock, idx)
    
    if not data:
      return
    
    # print("renting:", data)
    insert(self.r_shelf, self.rented, data)
    

  def drop(self, shop: int, movie: int) -> None:
    if (shop, movie) not in self.rented:
      return
    
    idx = self.rented[shop, movie]
    data = remove(self.r_shelf, self.rented, idx)
    
    if not data:
      return
    
    # print("dropping:", data)
    insert(self.s_shelf[movie], self.stock, data)


  def report(self) -> List[List[int]]:
    backup = []
    rpt = []
    p = False
    
    # rpt_full = sorted(self.r_shelf[:8].copy(), key=lambda x: x[2])
    # for s, m, _ in rpt_full[:5]:
    #   rpt.append([s, m])
    
    while self.r_shelf and len(rpt) < 5:
      data = remove(self.r_shelf, self.rented, 0)
      
      if p:
        print(data, self.r_shelf)
        
      backup.append(data)
      rpt.append([data[0], data[1]])
      
    for e in backup:
      insert(self.r_shelf, self.rented, e)
    
    if p:
      print("report", rpt)
      
    return rpt


class MovieRentingSystem:
  def __init__(self, n: int, entries: List[List[int]]):
    self.movies = defaultdict(list)
    self.out = []
    self.rented = set()
    self.p = {}
    
    for s, m, p in entries:
      self.p[s, m] = p
      self.movies[m].append((p, s, m))
      
    for m in self.movies.keys():
      heapify(self.movies[m])


  def search(self, movie: int) -> List[int]:
    rpt = []
    store = []
    
    while len(rpt) < 5 and self.movies[movie]:
      e = heappop(self.movies[movie])
      store.append(e)
      
      if (e[1], e[2]) not in self.rented:
        rpt.append(e[1])
    
    for e in store:
      heappush(self.movies[movie], e)
    
    return rpt


  def rent(self, shop: int, movie: int) -> None:
    # movie is already rented
    if (shop, movie) in self.rented:
      return
    
    self.rented.add((shop, movie))
    heappush(self.out, (self.p[shop, movie], shop, movie))
    

  def drop(self, shop: int, movie: int) -> None:
    self.rented.discard((shop, movie))


  def report(self) -> List[List[int]]:
    rpt = []
    store = []
    seen = set()
    
    while len(rpt) < 5 and self.out:
      e = heappop(self.out)
      if (e[1], e[2]) in self.rented and (e[1], e[2]) not in seen:
        rpt.append([e[1], e[2]])
        seen.add((e[1], e[2]))
        store.append(e)
    
    for e in store:
      heappush(self.out, e)
    
    # print(rpt)
    return rpt

  
# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
