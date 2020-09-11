package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// SNProblems ...
type SNProblems struct {
	set []*SN
}

// Solve ...
func (p *SNProblems) Solve() {
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

// SN ...
type SN struct {
	data   [][]int
	output int
}

// CreateSN ...
func CreateSN() s.Problem {
	set := make([]*SN, 0, 4)

	set = append(set, &SN{
		data:   [][]int{},
		output: 0,
	})

	return &SNProblems{set}
}

func (p *SN) solve() int {
	return countServers(p.data)
}

func countServers(grid [][]int) int {
  if grid == nil || len(grid) == 0 || len(grid[0]) == 0 {
    return 0
  }

  h, w := len(grid), len(grid[0])
  sh, sw := make([]int, h), make([]int, w)

  var total int

  for i := 0; i < h; i++ {
    for j := i; j < w; j++ {
      if grid[i][j] == 1 {
        total++
        sh[i]++
        sw[j]++
      }
    }

    if i < w {
      for j := i; j < h; j++ {
        if grid[j][i] == 1 {
          total++
          sh[j]++
          sw[i]++
        }
      }

      if grid[i][i] == 1 {
        total--
        sh[i]--
        sw[i]--
      }
    }

    // fmt.Println(i, total)
  }

  for i := 0; i < h; i++ {
    for j := 0; j < w; j++ {
      if grid[i][j] == 0 {
        continue
      }

      if sh[i] == 1 && sw[j] == 1 {
        total--
      }
    }
  }

  // fmt.Println(sh, sw)

  return total
}