package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// SRSAProblems ...
type SRSAProblems struct {
	set []*SRSA
}

// Solve ...
func (p *SRSAProblems) Solve() {
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

// SRSA ...
type SRSA struct {
	data   []int
	tgt    int
	output int
}

// CreateSRSA ...
func CreateSRSA() s.Problem {
	set := make([]*SRSA, 0, 4)

	set = append(set, &SRSA{
		data:   []int{4,5,6,7,0,1,2},
		tgt:    0,
		output: 4,
	})

	return &SRSAProblems{set}
}

func (p *SRSA) solve() int {
	return search(p.data, p.tgt)
}

func search(nums []int, target int) int {
  size := len(nums)

  if size == 0 {
    return -1
  }

  if size == 1 {
    if nums[0] == target {
      return 0
    }

    return -1
  }

  if target > nums[size-1] && target < nums[0] {
    return -1
  }

  l, r := 0, size-1
  for l < r {
    fmt.Println(l, r, (l+r)/2)

    if l == r {
      if nums[l] == target {
        return l
      }

      return -1
    }

    if target == nums[l] {
      return l
    }

    if target == nums[r] {
      return r
    }

    if r - l == 1 {
      return -1
    }

    m := (l + r) / 2

    if target == nums[m] {
      return m
    }

    if nums[m] > nums[l] && nums[m] < nums[r] {
      if target < nums[m] {
        r = m - 1
      } else {
        l = m + 1
      }
    } else if nums[m] > nums[l] && nums[m] > nums[r] {
      if target > nums[m] {
        l = m + 1
      } else if target >= nums[l] {
        r = m - 1
      } else {
        l = m + 1
      }
    } else {
      if target < nums[m] {
        r = m - 1
      } else if target < nums[r] {
        l = m + 1
      } else {
        r = m - 1
      }
    }
  }

  if target == nums[l] {
    return l
  }

  return -1
}