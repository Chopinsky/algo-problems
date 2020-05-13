package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// LSWDProblems ...
type LSWDProblems struct {
	set []*LSWD
}

// Solve ...
func (p *LSWDProblems) Solve() {
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

// LSWD ...
type LSWD struct {
	data   []int
	limit  int
	output int
}

// CreateLSWD ...
func CreateLSWD() s.Problem {
	set := make([]*LSWD, 0, 4)

	set = append(set, &LSWD{
		data:   []int{8, 2, 4, 7},
		limit:  4,
		output: 2,
	})

	set = append(set, &LSWD{
		data:   []int{10, 1, 2, 4, 7, 2},
		limit:  5,
		output: 4,
	})


	set = append(set, &LSWD{
		data:   []int{4, 2, 2, 2, 4, 4, 2, 2},
		limit:  0,
		output: 3,
	})

	return &LSWDProblems{set}
}

func (p *LSWD) solve() int {
	size, data, limit := len(p.data), p.data, p.limit
	if size == 1 {
		return 1
	}

	var diff int
	if size == 2 {
		diff = data[0] - data[1]

		if diff <= limit && (-1 * diff) <= limit {
			return 2
		}

		return 1
	}

	maxq := make([]int, 0, size)
	minq := make([]int, 0, size)
	
	maxq = append(maxq, 0)
	minq = append(minq, 0)

	if s.DebugMode() {
		for i := 0; i < size; i++ {		
			maxq = insertIntoMax(maxq, data, i)
			minq = insertIntoMin(minq, data, i)
		}

		for _, val := range maxq {
			fmt.Print(data[val], " ")
		}

		fmt.Println()

		for _, val := range minq {
			fmt.Print(data[val], " ")
		}

		fmt.Println()
	}

	max := 1
	left, right := 0, 0
	
	for right < size - 1 {
		right++
		
		maxq = insertIntoMax(maxq, data, right)
		minq = insertIntoMin(minq, data, right)
		
		// new number making the abs diff above the limit, seek the
		// next possible subarray meeting the criteria
		for data[maxq[0]] - data[minq[0]] > limit && right != left {
			left++

			// dequeue all numbers not in the range
			for len(maxq) > 0 && maxq[0] < left {
				maxq = maxq[1:]
			}
			
			// dequeue all numbers not in the range
			for len(minq) > 0 && minq[0] < left {
				minq = minq[1:]
			}
		}

		if right - left + 1 > max {
			max = right - left + 1
			fmt.Println("new longest:", left, right, max)
		}
	}

	return max
}

func insertIntoMax(queue, data []int, i int) []int {
	last := len(queue) - 1
	pos := last

	for pos >= 0 && data[queue[pos]] <= data[i] {
		pos--
	}

	if pos != last {
		queue = queue[:pos+1]
	}

	queue = append(queue, i)

	return queue
}

func insertIntoMin(queue, data []int, i int) []int {
	last := len(queue) - 1
	pos := last

	for pos >= 0 && data[queue[pos]] >= data[i] {
		pos--
	}

	if pos != last {
		queue = queue[:pos+1]
	}

	queue = append(queue, i)

	return queue
}
