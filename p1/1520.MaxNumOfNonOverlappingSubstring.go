package p1

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// MNNSProblems ...
type MNNSProblems struct {
	set []*MNNS
}

// Solve ...
func (p *MNNSProblems) Solve() {
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

// MNNS ...
type MNNS struct {
	data   string
	output []string
}

// CreateMNNS ...
func CreateMNNS() s.Problem {
	set := make([]*MNNS, 0, 4)

	set = append(set, &MNNS{
		data:   "adefaddaccc",
		output: []string{"e", "f", "ccc"},
	})

	set = append(set, &MNNS{
		data:   "abbaccd",
		output: []string{"d", "bb", "cc"},
	})

	return &MNNSProblems{set}
}

func (p *MNNS) solve() []string {
	m := make(map[byte][]int)

	for i := range p.data {
		c := p.data[i]

		if arr, ok := m[c]; ok {
			arr[2] = i
		} else {
			m[c] = []int{int(c), i, i}
		}
	}

	arr := make([][]int, 0, len(m))
	for _, v := range m {
		arr = append(arr, v)
	}

	sort.Slice(arr, func (i, j int) bool {
		return arr[i][2]-arr[i][1] < arr[j][2]-arr[j][1]
	})

	next := make([][]int, 0, len(m))
	merged := make(map[byte]bool)

	for _, v := range arr {
		c, l, r := v[0], v[1], v[2]
		rngStart := l

		if merged[byte(c)] {
			continue
		}

		merged[byte(c)] = true
		real := make([]int, 3)
		skip := false

		for l <= r {
			info := m[p.data[l]]
			c0 := byte(info[0])

			if !merged[c0] {
				start, end := info[1], info[2]

				// illegal case, we only expand to the right
				if start < rngStart {
					skip = true
					break
				}

				if end > r {
					if end > r {
						r = end
					}

					merged[c0] = true
				}
			}

			l++
		}

		if !skip {
			real[1], real[2] = rngStart, r
			next = append(next, real)
		}
	}

	arr = next
	sort.Slice(arr, func (i, j int) bool {
		return arr[i][1] < arr[j][1]
	})

	// fmt.Println(arr)

	size := len(arr)
	idx := size - 1
	dp := make([][][]int, len(p.data))

	dp[arr[size-1][1]] = [][]int{
		{ idx },
		{ 1, arr[size-1][2] - arr[size-1][1] + 1 },
	}

	for i := arr[size-1][1] - 1; i >= 0; i-- {
		dp[i] = dp[i+1]

		if idx >= 0 && i <= arr[idx-1][1] {
			idx--
			last := arr[idx][2] + 1

			// fmt.Println("checking:", i, last, size)

			if last < len(p.data) {
				lastBest := dp[last]

				if len(lastBest) == 2 && (lastBest[1][0] + 1 > dp[i][1][0] || (lastBest[1][0] + 1 == dp[i][1][0] && lastBest[1][1] + arr[idx][2] - arr[idx][1] + 1 < dp[i][1][1])) {
					base := append([]int(nil), lastBest[0]...)
					base = append(base, idx)

					dp[i] = [][]int{
						base,
						{ len(base), lastBest[1][1] + arr[idx][2] - arr[idx][1] + 1 },
					}
				}
			}
		}
	}

	/*
	fmt.Println("arr:", arr)
	for i := range dp {
		fmt.Println(dp[i])
	}
	*/

	res := make([]string, 0, len(dp[0]))
	for _, i := range dp[0][0] {
		l, r := arr[i][1], arr[i][2]+1
		res = append(res, p.data[l:r])
	}

	return res
}
