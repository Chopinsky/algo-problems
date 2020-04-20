package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// KDProblems ...
type KDProblems struct {
	set []*KD
}

// Solve ...
func (p *KDProblems) Solve() {
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

	fmt.Println("Algorithm took", time.Since(start))
}

// KD ...
type KD struct {
	data   int
	output uint64
}

// CreateKD ...
func CreateKD() s.Problem {
	set := make([]*KD, 0, 4)

	set = append(set, &KD{
		data:   1,
		output: 10,
	})

	set = append(set, &KD{
		data:   2,
		output: 20,
	})

	set = append(set, &KD{
		data:   3,
		output: 46,
	})

	set = append(set, &KD{
		data:   5000,
		output: 947624200,
	})

	return &KDProblems{set}
}

func (p *KD) solve() uint64 {
	var mod uint64 = 1000000007

	count := [][]uint64{{1, 1, 1, 1, 1, 1, 1, 1, 1, 1}}

	jump := [][]uint64{
		{0, 0, 0, 0, 0, 1, 0, 1, 0, 0}, // 1
		{0, 0, 0, 0, 0, 0, 1, 0, 1, 0}, // 2
		{0, 0, 0, 1, 0, 0, 0, 1, 0, 0}, // 3
		{0, 0, 1, 0, 0, 0, 0, 0, 1, 1}, // 4
		{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, // 5
		{1, 0, 0, 0, 0, 0, 1, 0, 0, 1}, // 6
		{0, 1, 0, 0, 0, 1, 0, 0, 0, 0}, // 7
		{1, 0, 1, 0, 0, 0, 0, 0, 0, 0}, // 8
		{0, 1, 0, 1, 0, 0, 0, 0, 0, 0}, // 9
		{0, 0, 0, 1, 0, 1, 0, 0, 0, 0}, // 0
	}

	n := p.data - 1
	for n > 0 {
		/* naive loop: */
		// count = s.MtrxMulti(count, jump, mod)
		// n--

		/* fast loop */
		if n&1 == 1 {
			count = s.MtrxMulti(count, jump, mod)
		}

		if n > 1 {
			jump = s.MtrxMulti(jump, jump, mod)
		}

		n >>= 1
	}

	sum := uint64(0)
	for i := 0; i < len(count[0]); i++ {
		sum = (sum + count[0][i]) % mod
	}

	return sum
}
