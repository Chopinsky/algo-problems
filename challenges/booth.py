def booth_smallest_rotation(s: str) -> str:
  base = s+s
  n = len(s)

  # i - curr rotation start;
  # j - next rotation start; 
  # k - matched prefix;
  i, j, k = 0, 1, 0

  while i < n and j < n and k < n:
    c0 = base[i+k]
    c1 = base[j+k]

    # matching, continue
    if c0 == c1:
      k += 1
      continue

    # j is the better solution, reset i
    if c0 > c1:
      i = i + k + 1
      k = 0
      if i <= j:
        i = j + 1

      continue

    # shift next start to begin new search
    j = j + k + 1
    k = 0
    if j <= i:
      j = i + 1

  start = min(i, j)
  return base[start:start+n]