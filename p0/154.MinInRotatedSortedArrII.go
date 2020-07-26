package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MRSAProblems ...
type MRSAProblems struct {
	set []*MRSA
}

// Solve ...
func (p *MRSAProblems) Solve() {
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

// MRSA ...
type MRSA struct {
	data   []int
	output int
}

// CreateMRSA ...
func CreateMRSA() s.Problem {
	set := make([]*MRSA, 0, 4)

	set = append(set, &MRSA{
		data:   []int{1, 3, 5},
		output: 1,
	})

	set = append(set, &MRSA{
		data:   []int{2, 2, 2, 0, 1},
		output: 0,
	})

	return &MRSAProblems{set}
}

func (p *MRSA) solve() int {
	return findMin(p.data)
}

func findMin(nums []int) int {
  size := len(nums)

  if size == 1 || nums[0] < nums[size-1] {
    return nums[0]
  }

  l, r := 0, size-1
  for l < r {
    for l < r && l < size-1 && nums[l] == nums[l+1] {
      l++
    }

    for l < r && r > 0 && nums[r] == nums[r-1] {
      r--
    }

    fmt.Println(l, r)

    if l == r {
      return nums[l]
    }

    if nums[l] < nums[r] {
      return nums[l]
    }

    if r - l == 1 {
      if nums[l] <= nums[r] {
        return nums[l]
      }

      return nums[r]
    }

    m := (l+r)/2

    if nums[m] < nums[r] && nums[m] <= nums[l] {
      r = m
    } else if nums[m] >= nums[l] && nums[m] > nums[r] {
      l = m
    }

  }

  return nums[l]
}