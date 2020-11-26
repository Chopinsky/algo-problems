package p1

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// DPIProblems ...
type DPIProblems struct {
	set []*DPI
}

// Solve ...
func (p *DPIProblems) Solve() {
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

// DPI ...
type DPI struct {
	data   []int
	q      []int
	output bool
}

// CreateDPI ...
func CreateDPI() s.Problem {
	set := make([]*DPI, 0, 4)

	set = append(set, &DPI{
		data:   []int{1, 2, 3, 4},
		q:      []int{2},
		output: false,
	})

	set = append(set, &DPI{
		data:   []int{1, 2, 3, 3},
		q:      []int{2},
		output: true,
	})

	set = append(set, &DPI{
		data:   []int{1, 1, 2, 2},
		q:      []int{2, 2},
		output: true,
	})

	set = append(set, &DPI{
		data:   []int{1, 1, 2, 3},
		q:      []int{2, 2},
		output: false,
	})

	set = append(set, &DPI{
		data:   []int{1, 1, 1, 1, 1},
		q:      []int{2, 3},
		output: true,
	})

	return &DPIProblems{set}
}

func (p *DPI) solve() bool {
	nums, q := p.data, p.q
	store := make(map[int]int)

	max := 0
	for _, v := range nums {
		store[v]++

		if store[v] > max {
			max = store[v]
		}
	}

	sum := 0
	for _, v := range q {
		sum += v

		// the biggest customer supply won't be met
		if v > max {
			return false
		}

		// total demand is larger than the supply, can't do it
		if sum > len(nums) {
			return false
		}
	}

	sort.Slice(q, func(i, j int) bool {
		return q[i] > q[j]
	})

	return dfs(q, 0, store, make(map[string]bool))
}

func dfs(q []int, idx int, store map[int]int, cache map[string]bool) bool {
	if idx >= len(q) {
		return true
	}

	key := fmt.Sprint(idx) + fmt.Sprint(store)
	if ans, ok := cache[key]; ok {
		return ans
	}

	var ans bool
	demand := q[idx]

	for k := range store {
		if store[k] < demand {
			continue
		}

		store[k] -= demand

		ans = dfs(q, idx+1, store, cache)
		if ans {
			break
		}

		store[k] += demand
	}

	cache[key] = ans
	return ans
}
