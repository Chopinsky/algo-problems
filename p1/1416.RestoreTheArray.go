package p1

import (
	"fmt"
	"math"
	"math/rand"
	"strconv"
	"time"

	s "go-problems/shared"
)

// RAProblems ...
type RAProblems struct {
	set []*RA
}

// Solve ...
func (p *RAProblems) Solve() {
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

// RA ...
type RA struct {
	data   string
	k      int
	output int
}

// CreateRA ...
func CreateRA() s.Problem {
	set := make([]*RA, 0, 4)

	num := "9"
	for i := 0; i < 99999; i++ {
		num += strconv.Itoa(rand.Intn(10))
	}

	set = append(set, &RA{
		data:   num,
		k:      1000000000,
		output: 784118384,
	})

	set = append(set, &RA{
		data:   "1000",
		k:      10000,
		output: 1,
	})

	set = append(set, &RA{
		data:   "1000",
		k:      10,
		output: 0,
	})

	set = append(set, &RA{
		data:   "1317",
		k:      2000,
		output: 8,
	})

	set = append(set, &RA{
		data:   "2020",
		k:      30,
		output: 1,
	})

	set = append(set, &RA{
		data:   "1234567890",
		k:      90,
		output: 34,
	})

	return &RAProblems{set}
}

var chart = make(map[string]int)

func (p *RA) solve() int {
	base := strconv.Itoa(p.k)
	mod := 1000000007

	l := len(base)
	size := len(p.data)

	if s.DebugMode() {
		fmt.Println(l)
	}

	dp := make([]int, size)
	count := 0

	for i := size - 1; i >= 0; i-- {
		stat := 0

		for j := 0; j < l && i+j < size; j++ {
			num := p.data[i : i+j+1]

			if s.DebugMode() {
				fmt.Println(i, j, num)
			}

			if j == 0 && num[0] == '0' {
				break
			}

			if stat <= 1 {
				if num[j] == base[j] {
					// needs to keep comparing
					stat = 1
				} else if num[j] < base[j] {
					// clear, we're smaller
					stat = 2
				} else {
					// clear, but we're larger
					stat = 3
				}
			}

			if j == l-1 && stat == 3 {
				break
			}

			if i+j < size-1 {
				dp[i] += dp[i+j+1]
			} else {
				dp[i]++
			}
		}

		if dp[i] > 0 {
			count = 0
			dp[i] %= mod
		} else {
			count++
			if count == l {
				return 0
			}
		}
	}

	if s.DebugMode() {
		if size > 10 {
			fmt.Println(dp[size-10:], p.data[size-10:], p.k)
		} else {
			fmt.Println(dp)
		}
	}

	return dp[0]
}

func (p *RA) solve1() int {
	mod := 1000000007

	l := int(math.Log10(float64(p.k))) + 1
	size := len(p.data)

	if s.DebugMode() {
		fmt.Println(l)
	}

	dp := make([]int, size)
	count := 0

	for i := size - 1; i >= 0; i-- {
		for j := 0; j < l && i+j < size; j++ {
			num := parse(p.data[i : i+j+1])

			if s.DebugMode() {
				fmt.Println(i, j, num)
			}

			if j == 0 && num == 0 {
				break
			}

			if j == l-1 && num > p.k {
				break
			}

			if i+j < size-1 {
				dp[i] += dp[i+j+1]
			} else {
				dp[i]++
			}
		}

		if dp[i] > 0 {
			count = 0
			dp[i] %= mod
		} else {
			count++
			if count == l {
				return 0
			}
		}
	}

	if s.DebugMode() {
		if size > 10 {
			fmt.Println(dp[size-10:], p.data[size-10:], p.k)
		} else {
			fmt.Println(dp)
		}
	}

	return dp[0]
}

func parse(src string) int {
	// if num, ok := chart[src]; ok {
	// 	return num
	// }

	num, err := strconv.Atoi(src)

	if err != nil {
		fmt.Println("[error] invalid string:", src)
		return 0
	}

	// chart[src] = num

	return num
}
