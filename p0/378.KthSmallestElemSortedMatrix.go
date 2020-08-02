package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// KSESMProblems ...
type KSESMProblems struct {
	set []*KSESM
}

// Solve ...
func (p *KSESMProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= 0; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == 0 {
				s.Print(i, p.output, result)
			}
		}
	}

	fmt.Println("Algorithm finished in:", time.Since(start))
}

// KSESM ...
type KSESM struct {
	data   [][]int
	k      int
	output int
}

// CreateKSESM ...
func CreateKSESM() s.Problem {
	set := make([]*KSESM, 0, 4)

	set = append(set, &KSESM{
		data:   [][]int{
			{1,  5,  9},
			{10, 11, 13},
			{12, 13, 15},
		},
		k:      8,
		output: 13,
	})

	return &KSESMProblems{set}
}

func (p *KSESM) solve() int {
	return kthSmallest(p.data, p.k)
}

func kthSmallest(matrix [][]int, k int) int {
  if matrix == nil || len(matrix) == 0 || len(matrix[0]) == 0 {
    return -1
  }

  var tv, bv, bc, cv, cc int
  tv, bv = -1, -1

  h, w := len(matrix), len(matrix[0])
  l, r := matrix[0][0], matrix[h-1][w-1] + 1

  for l <= r {
    cv = (l+r)/2
    cc = count(matrix, cv, h, w)

    // fmt.Println("it:", cv, cc, l, r)

    if cc < k {
      l = cv + 1

      if bv == -1 || cv > bv {
        bv = cv
        bc = cc
      }
    } else {
      r = cv - 1

      if tv == -1 || cv < tv {
        tv = cv
        // tc = cc
      }
    }
  }

  // fmt.Println(tv, tc, bv, bc, cv, cc)

  if bc == k {
    return bv
  }

  return tv
}

func count(mtr [][]int, k, h, w int) int {
  var l, r, m, c int

  for i := 0; i < h; i++ {
    if mtr[i][0] > k {
      break
    }

    if mtr[i][w-1] <= k {
      c += w
      continue
    }

    l, r = 0, w

    for l < r {
      m = (l + r) / 2

      if mtr[i][m] <= k {
        l = m + 1
      } else {
        r = m - 1
      }
    }

    if mtr[i][l] > k {
      c += l
    } else {
      c += l+1
    }
  }

  return c
}