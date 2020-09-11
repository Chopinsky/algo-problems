package p1

func minFlips(a int, b int, c int) int {
  // fmt.Println(diff, base)
  var ba, bb, bc, count int

  for a != 0 || b != 0 || c != 0 {
    ba, bb, bc = a & 1, b & 1, c & 1

    if bc == 1 && (bb + ba) < 1 {
      count++
    } else if bc == 0 && (bb + ba) > 0 {
      count += bb + ba
    }

    a >>= 1
    b >>= 1
    c >>= 1
  }

  return count
}