package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// NWSSProblems ...
type NWSSProblems struct {
	set []*NWSS
}

// Solve ...
func (p *NWSSProblems) Solve() {
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

// NWSS ...
type NWSS struct {
	data   string
	output int
}

// CreateNWSS ...
func CreateNWSS() s.Problem {
	set := make([]*NWSS, 0, 4)

	set = append(set, &NWSS{
		data:   "10101",
		output: 4,
	})

	set = append(set, &NWSS{
		data:   "1001",
		output: 0,
	})

	set = append(set, &NWSS{
		data:   "0000",
		output: 3,
	})

	set = append(set, &NWSS{
		data:   "100100010100110",
		output: 12,
	})

	return &NWSSProblems{set}
}

func (p *NWSS) solve() int {
	s := p.data
	l := len(s)
	if l < 3 {
		return 0
	}

	arr := make([]int, 0, l)
	for i, char := range s {
		if char == '1' {
			arr = append(arr, i)
		}
	}

	size := len(arr)
	if size == 0 {
		return int((int64(l-1) * int64(l-2) / int64(2)) % int64(mod))
	}

	if size%3 != 0 || size < 3 {
		return 0
	}

	// fmt.Println(arr)

	s1 := arr[size/3] - arr[(size/3)-1]
	s2 := arr[2*(size/3)] - arr[2*(size/3)-1]

	return int(int64(s1*s2) % int64(mod))
}
