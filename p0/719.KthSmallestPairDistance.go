package p0

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// KSPDProblems ...
type KSPDProblems struct {
	set []*KSPD
}

// Solve ...
func (p *KSPDProblems) Solve() {
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

// KSPD ...
type KSPD struct {
	data   []int
	kth    int
	output int
}

// CreateKSPD ...
func CreateKSPD() s.Problem {
	set := make([]*KSPD, 0, 4)

	set = append(set, &KSPD{
		data:   []int{1,3,1},
		kth:      1,
		output: 0,
	})

	return &KSPDProblems{set}
}

func (p *KSPD) solve() int {
	return smallestDistancePair(p.data, p.kth)
}

func smallestDistancePair(nums []int, k int) int {
  sort.Ints(nums)

  size := len(nums)
  l, r := 0, nums[size-1] - nums[0]

  for l < r {
    mid := (l + r) / 2
    count, lc, rc := 0, 0, 1

    for rc < size {
      // move the window until all pairs in the window meet the
      // critiria: (lc, rc) has the distance smaller than or equal
      // to `mid`
      for nums[rc] - nums[lc] > mid {
        lc++
      }

      // pairs are (lc, rc), (lc+1, rc), (lc+2, rc) ... (rc-1, rc), such
      // that duplicate counts will be avoided
      count += rc - lc

      // now move the right side
      rc++
    }

    if count >= k {
      r = mid
    } else {
      l = mid + 1
    }
  }

  return l
}