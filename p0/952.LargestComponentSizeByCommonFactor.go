package p0

import (
	"fmt"
	"math"
	"sort"
	"time"

	s "go-problems/shared"
)

// LCSProblems ...
type LCSProblems struct {
	set []*LCS
}

// Solve ...
func (p *LCSProblems) Solve() {
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

// LCS ...
type LCS struct {
	data   []int
	output int
}

// CreateLCS ...
func CreateLCS() s.Problem {
	set := make([]*LCS, 0, 4)

	set = append(set, &LCS{
		data:   []int{2, 3, 6, 7, 4, 12, 21, 39},
		output: 8,
	})

	return &LCSProblems{set}
}

func (p *LCS) solve() int {
	return 0
}

func largestComponentSize(a []int) int {
	size := len(a)
	if size == 1 {
		return 1
	}

	sort.Ints(a)
	u := make([]int, size)
	factors := make(map[int]int)

	for i := range u {
		u[i] = i
	}

	for i := 0; i < size; i++ {
		addFactors(a[i], i, u, factors)
	}

	count := make(map[int]int)
	ans := 0

	for i := range u {
		root := findLCS(u, i)
		count[root]++

		if count[root] > ans {
			ans = count[root]
		}
	}

	return ans
}

func addFactor(u []int, factors map[int]int, f, i int) int {
	pos := i
	if j, ok := factors[f]; ok {
		pos = unionLCS(u, i, j)
	} else {
		factors[f] = i
	}

	return pos
}

func addFactors(n, i int, u []int, factors map[int]int) {
	// Print the number of 2s that divide n
	added := false
	for n%2 == 0 {
		if !added {
			added = true
			i = addFactor(u, factors, 2, i)
		}

		n /= 2
	}

	// n must be odd at this point. So we can skip
	// one element (Note i = i +2)
	upper := int(math.Sqrt(float64(n)))
	for j := 3; j <= upper; j += 2 {
		// While i divides n, print i and divide n
		added = false
		for n%j == 0 {
			if !added {
				added = true
				i = addFactor(u, factors, j, i)
			}

			n /= j
		}
	}

	// This condition is to handle the case when n
	// is a prime number greater than 2
	if n > 2 {
		addFactor(u, factors, n, i)
	}
}

func unionLCS(arr []int, i, j int) int {
	ri, rj := findLCS(arr, i), findLCS(arr, j)
	if ri == rj {
		return ri
	}

	if ri < rj {
		arr[rj] = ri
		return ri
	}

	arr[ri] = rj
	return rj
}

func findLCS(arr []int, i int) int {
	for arr[i] != i {
		i = arr[i]
	}

	return i
}
