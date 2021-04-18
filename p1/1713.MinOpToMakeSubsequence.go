package p1

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// MOMSProblems ...
type MOMSProblems struct {
	set []*MOMS
}

// Solve ...
func (p *MOMSProblems) Solve() {
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

// MOMS ...
type MOMS struct {
	data   []int
	arr    []int
	output int
}

// CreateMOMS ...
func CreateMOMS() s.Problem {
	set := make([]*MOMS, 0, 4)

	set = append(set, &MOMS{
		data:   []int{5, 1, 3},
		arr:    []int{9, 4, 2, 3, 4},
		output: 2,
	})

	set = append(set, &MOMS{
		data:   []int{6, 4, 8, 1, 3, 2},
		arr:    []int{4, 7, 6, 2, 3, 8, 6, 1},
		output: 3,
	})

	return &MOMSProblems{set}
}

func (p *MOMS) solve() int {
	pos := make(map[int][][2]int)
	l0, l1 := len(p.arr), len(p.data)
	last := p.data[l1-1]

	for i, val := range p.arr {
		num := l1 + 1
		if val == last {
			num = 0
		}

		pos[val] = append(pos[val], [2]int{i, num})
	}

	// fmt.Println(pos)

	pos[last] = append(pos[last], [2]int{l0, 1})
	curr := pos[last]
	temp := make([][2]int, 0, len(curr))

	for i := l1 - 2; i >= 0; i-- {
		val := p.data[i]
		posArr := pos[val]

		if len(posArr) == 0 {
			// number not found in the target, increment every position with
			// an insertion before the position
			for i := range curr {
				curr[i][1]++
			}

			continue
		}

		// get the best solution from the before first appearence
		k := sort.Search(len(curr), func(idx int) bool {
			return curr[idx][0] >= posArr[0][0]
		})

		for j := 0; j < k; j++ {
			temp = append(temp, [2]int{curr[j][0], curr[j][1] + 1})
		}

		// find best matches after
		for _, jval := range posArr {
			k := sort.Search(len(curr), func(idx int) bool {
				return jval[0] <= curr[idx][0]
			})

			// fmt.Println("found:", jval, curr[k])

			jval[1] = curr[k][1]
			for len(temp) > 0 && jval[1] < temp[len(temp)-1][1] {
				temp = temp[:len(temp)-1]
			}

			temp = append(temp, jval)
			if k >= len(curr)-1 {
				break
			}
		}

		lp := len(curr) - 1
		curr[lp][1]++
		temp = append(temp, curr[lp])

		// fmt.Println(val, temp)

		// reset
		curr, temp = temp, curr
		temp = temp[:0]
	}

	// loop over the 1st number and find the best solutions
	ans := l1
	for _, count := range curr {
		if count[1] < ans {
			ans = count[1]
		}
	}

	return ans
}
