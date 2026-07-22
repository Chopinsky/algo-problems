def manacher_pali_len(s: str) -> str:
  """Return the longest palindromic substring in s."""
  # Phase 1: insert separators
  t = "#" + "#".join(s) + "#"
  n = len(t)
  p = [0] * n
  center = 0
  right = 0

  for i in range(n):
    # ----- L1: mirror initialization -----
    if i < right:
      mirror = 2*center - i            # L2, center - (i-center)
      p[i] = min(right-i, p[mirror])   # L3

    # ----- L4: expand outward -----
    while i-p[i]-1 >= 0 and i+p[i]+1 < n and t[i-p[i]-1] == t[i+p[i]+1]:
      p[i] += 1                        # L5

    # ----- L6: update rightmost palindrome -----
    if i+p[i] > right:
      center = i                       # L7
      right = i + p[i]                 # L8

  # ----- L9: extract result -----
  max_radius = max(p)                      # L10
  center_idx = p.index(max_radius)         # L11
  start = (center_idx-max_radius) // 2     # L12

  # longest palindrome in the string
  return s[start:start+max_radius]         # L13
