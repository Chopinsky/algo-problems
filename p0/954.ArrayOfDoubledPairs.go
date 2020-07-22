package p0

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// AODPProblems ...
type AODPProblems struct {
	set []*AODP
}

// Solve ...
func (p *AODPProblems) Solve() {
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

// AODP ...
type AODP struct {
	data   []int
	output bool
}

// CreateAODP ...
func CreateAODP() s.Problem {
	set := make([]*AODP, 0, 4)

	set = append(set, &AODP{
		data:   []int{},
		output: false,
	})

	return &AODPProblems{set}
}

func (p *AODP) solve() bool {
	return canReorderDoubled(p.data)
}

func canReorderDoubled(A []int) bool {
  store := make(map[int]int)
  keys := make([]int, 0, len(A))

  for _, val := range A {
    if store[val] == 0 {
      keys = append(keys, val)
    }

    store[val]++
  }

  sort.Slice(keys, func (i, j int) bool {
    if (keys[i] <= 0 && keys[j] <= 0) {
      return keys[i] > keys[j]
    }

    return keys[i] < keys[j]
  })

  // fmt.Println(keys)
  // var m int

  size := len(keys)

  for i := range keys {
    k := keys[i]
    v := store[k]

    if v <= 0 || (i < size-1 && keys[i] < 0 && keys[i+1] > 0) {
      continue
    }

    if k == 0 {
      if v % 2 == 0 {
        store[0] = 0
        continue
      }

      return false
    }

    if store[2 * k] >= v {
      // m = min(v, store[2 * k])
      store[k] -= v
      store[2 * k] -= v
    }
  }

  fmt.Println(store)

  for _, v := range store {
    if v > 0 {
      return false
    }
  }

  return true
}