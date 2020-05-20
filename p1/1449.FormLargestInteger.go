package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// FLIProblems ...
type FLIProblems struct {
	set []*FLI
}

// Solve ...
func (p *FLIProblems) Solve() {
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

// FLI ...
type FLI struct {
	data   []int
	target int
	output int
}

// CreateFLI ...
func CreateFLI() s.Problem {
	set := make([]*FLI, 0, 4)

	set = append(set, &FLI{
		data:   []int{4, 3, 2, 5, 6, 7, 2, 5, 5},
		target: 9,
		output: 7772,
	})

	set = append(set, &FLI{
		data:   []int{7, 6, 5, 5, 5, 6, 8, 7, 8},
		target: 12,
		output: 85,
	})

	set = append(set, &FLI{
		data:   []int{2, 4, 6, 2, 4, 6, 4, 4, 4},
		target: 5,
		output: 0,
	})

	set = append(set, &FLI{
		data:   []int{6, 10, 15, 40, 40, 40, 40, 40, 40},
		target: 47,
		output: 32211,
	})

	return &FLIProblems{set}
}

func (p *FLI) solve() int {
	store := make(map[int]int)
	data := p.data
	lb, ub := 5999, 0

	for i := 0; i < 9; i++ {
		store[data[i]] = i + 1
		if data[i] < lb {
			lb = data[i]
		}

		if data[i] > ub {
			ub = data[i]
		}
	}

	dp := make([]*num, p.target + 1)
	dp[lb] = newNum(store[lb])

	for i := lb + 1; i <= p.target; i++ {
		if i <= ub && store[i] > 0 {
			dp[i]	= newNum(store[i])
		}

		for k, v := range store {
			if i <= k || dp[i-k] == nil {
				continue
			}

			// a match is found, add the new digit and continue
			if dp[i] == nil {
				dp[i] = dp[i-k].getNext(v)
				continue
			}

			diff := dp[i-k].count - dp[i].count

			if diff == -1 {
				for j := 9; j >= 0; j-- {
					curr, nextVal := dp[i].numbers[j], dp[i-k].numbers[j]

					if j == v {
						nextVal++	
					}
					
					if curr == 0 && nextVal == 0 {
						continue
					}

					if curr > nextVal {
						break
					}

					if nextVal > curr {
						diff = 1
						break
					}
				}
			}

			if diff >= 0 {
				dp[i] = dp[i-k].getNext(v)
			}
		}
	}

	if s.DebugMode() {
		fmt.Println(dp[p.target])		
	}

	if dp[p.target] != nil {
		result := 0
		numbers := dp[p.target].numbers

		for i := 9; i > 0; i-- {
			count := numbers[i]

			for count > 0 {
				result = (result * 10) + i
				count--
			}
		}

		return result
	}

	return 0
}

type num struct {
	numbers map[int]int
	count int
	largest int
}

func newNum(val int) *num {
	return &num{
		numbers: map[int]int{ val: 1 },
		count: 1,
		largest: val,
	}
}

func (n *num) getNext(val int) *num {
	var largest int
	if val > n.largest {
		largest = val
	} else {
		largest = n.largest
	}

	next := &num{
		numbers: make(map[int]int, len(n.numbers)),
		count: n.count + 1,
		largest: largest,
	}

	for k, v := range n.numbers {
		next.numbers[k] = v
	}

	next.numbers[val]++

	return next
}
