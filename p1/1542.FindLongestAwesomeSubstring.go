package p1

import (
	"fmt"
	"strconv"
	"time"

	s "go-problems/shared"
)

// FLSProblems ...
type FLSProblems struct {
	set []*FLS
}

// Solve ...
func (p *FLSProblems) Solve() {
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

// FLS ...
type FLS struct {
	data   string
	output int
}

// CreateFLS ...
func CreateFLS() s.Problem {
	set := make([]*FLS, 0, 4)

	set = append(set, &FLS{
		data:   "3242415",
		output: 5,
	})

	set = append(set, &FLS{
		data:   "12345678",
		output: 1,
	})

	set = append(set, &FLS{
		data:   "213123",
		output: 6,
	})

	set = append(set, &FLS{
		data:   "00",
		output: 2,
	})

	return &FLSProblems{set}
}

func (p *FLS) solve() int {
	if len(p.data) == 1 {
		return 1
	}

	store := make(map[int]int)
	presum := 1 << int(p.data[0]-'0')

	if s.DebugMode() {
		fmt.Println("0", strconv.FormatInt(int64(presum), 2))
	}

	store[presum] = 0
	best := 1

	for i := 1; i < len(p.data); i++ {
		presum ^= 1 << int(p.data[i]-'0')

		if s.DebugMode() {
			fmt.Println(i, strconv.FormatInt(int64(presum), 2))
		}

		if presum == 0 {
			best = i + 1
			continue
		}

		base := 1 << 9

		for j := 0; j < 10; j++ {
			if pos, ok := store[presum^base]; ok && i-pos > best {
				best = i - pos
			}

			base >>= 1
		}

		if _, ok := store[presum]; !ok {
			store[presum] = i
		}
	}

	return best
}
