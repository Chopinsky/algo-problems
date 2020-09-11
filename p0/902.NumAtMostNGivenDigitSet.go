package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// NAMNGDSProblems ...
type NAMNGDSProblems struct {
	set []*NAMNGDS
}

// Solve ...
func (p *NAMNGDSProblems) Solve() {
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

// NAMNGDS ...
type NAMNGDS struct {
	data   []string
	n      int
	output int
}

// CreateNAMNGDS ...
func CreateNAMNGDS() s.Problem {
	set := make([]*NAMNGDS, 0, 4)

	set = append(set, &NAMNGDS{
		data:   []string{"1", "3", "5", "7"},
		n:      100,
		output: 20,
	})

	set = append(set, &NAMNGDS{
		data:   []string{"1", "4", "9"},
		n:      1000000000,
		output: 29523,
	})

	set = append(set, &NAMNGDS{
		data:   []string{"1", "4", "9"},
		n:      14889,
		output: 165,
	})

	return &NAMNGDSProblems{set}
}

func (p *NAMNGDS) solve() int {
	return atMostNGivenDigitSet(p.data, p.n)
}

func atMostNGivenDigitSet(D []string, n int) int {
	size := len(D)
	d := make([]int, 10)

	for i := range D {
		d[int(D[i][0]-'0')] = 1
	}

	presum := make([]int, 10)

	for i := 1; i < 10; i++ {
		presum[i] = presum[i-1]

		if d[i] == 1 {
			presum[i]++
		}
	}

	if n < 10 {
		return presum[n]
	}

	fmt.Println(presum)

	ans, base := size, size
	nums := make([]int, 0, 9)

	for n > 0 {
		nums = append(nums, n%10)
		n /= 10
	}

	counts := make([]int, len(nums)-1)
	counts[0] = size

	for i := 2; i < len(nums); i++ {
		base *= size
		ans += base
		counts[i-1] = base
	}

	var val, count int
	base = 1
	fmt.Println("base", ans)

	for i := len(nums) - 1; i >= 0; i-- {
		val = nums[i]
		count = presum[val]

		if count == 0 {
			// b0, b1 = 0, 0
			base = 0
			break
		}

		// todo: more complex cases -- for d[val] == 1, count the high number and repeat,
		//       and update `base` ...

		if i == 0 {
			ans += count
			break
		}

		if d[val] == 1 {
			ans += (count - 1) * counts[i-1]
		} else {
			ans += count * counts[i-1]
			break
		}

		fmt.Println(val, count, counts[i-1])
	}

	// fmt.Println(ans, b0, b1)

	return ans
}
