package p0

import (
  "fmt"
  "sort"
	"time"

	s "go-problems/shared"
)

// FAAProblems ...
type FAAProblems struct {
	set []*FAA
}

// Solve ...
func (p *FAAProblems) Solve() {
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

// FAA ...
type FAA struct {
	data   []int
	output int
}

// CreateFAA ...
func CreateFAA() s.Problem {
	set := make([]*FAA, 0, 4)

	set = append(set, &FAA{
		data:   []int{16, 16},
		output: 2,
	})

	set = append(set, &FAA{
		data:   []int{20,30,100,110,120},
		output: 3,
  })

	set = append(set, &FAA{
		data:   []int{16, 17, 18},
		output: 2,
  })

	return &FAAProblems{set}
}

func (p *FAA) solve() int {
  return numFriendRequests(p.data)
}

// n
func numFriendRequests(ages []int) int {
  if ages == nil || len(ages) <= 1 {
    return 0
  }

  m := make(map[int]int)
  count := 0

  for i := range ages {
    m[ages[i]]++
  }

  for a, c0 := range m {
    if a > 14 {
      // min age to friend each other: 14, because it's the min number to
      // meet the critira: 0.5*A + 7 < A
      count += c0 * (c0-1)
    }

    for l := (a/2 + 8); l < a; l++ {
      if c1, ok := m[l]; ok {
        count += c0 * c1
      }
    }
  }

  return count
}

// n*Log(n) + 2*n
func numFriendRequests1(ages []int) int {
  if ages == nil || len(ages) <= 1 {
    return 0
  }

  sort.Ints(ages)
  count := 0
  size := len(ages)

  // fmt.Println(ages)

  l, r := 0, 1
  last := ages[l]
  sameAges := 0

  for r < size {
    if ages[r] == last && last > 14 {
      sameAges++
      count += sameAges
    } else {
      last = ages[r]
      sameAges = 0
    }

    for l < r && !check(ages, l, r) {
      l++
    }

    count += r - l
    r++
  }


  return count
}

func check(ages []int, l, r int) bool {
  return float32(ages[r])/2 + 7 < float32(ages[l])
}
