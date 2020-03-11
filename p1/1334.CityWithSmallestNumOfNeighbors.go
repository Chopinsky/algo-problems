package p1

import (
	"fmt"

	s "../shared"
)

// CSNNProblems ...
type CSNNProblems struct {
	set []*CSNN
}

// Solve ...
func (p *CSNNProblems) Solve() {
	fmt.Println()

	for i, p := range p.set {
		result := p.solve()

		fmt.Println("=== Problem", i, "===")
		fmt.Println("Expecting:  ", p.output)
		fmt.Println("Caculation: ", result)
		fmt.Println()
	}
}

// CSNN ...
type CSNN struct {
	data   [][]int
	num    int
	th     int
	output int
}

// CreateCSNN ...
func CreateCSNN() s.Problem {
	set := make([]*CSNN, 0, 4)

	set = append(set, &CSNN{
		data:   [][]int{{0, 1, 3}, {1, 2, 1}, {1, 3, 4}, {2, 3, 1}},
		num:    4,
		th:     4,
		output: 3,
	})

	set = append(set, &CSNN{
		data:   [][]int{{0, 1, 2}, {0, 4, 8}, {1, 2, 3}, {1, 4, 2}, {2, 3, 1}, {3, 4, 1}},
		num:    5,
		th:     2,
		output: 0,
	})

	return &CSNNProblems{set}
}

func (p *CSNN) solve() int {
	edges := make([][][]int, p.num)
	costs := make([][]int, p.num)
	stack := make([][]int, p.num)

	for i := 0; i < p.num; i++ {
		costs[i] = make([]int, p.num)
		// costs[i][i] = 1
	}

	for _, pair := range p.data {
		start, end, cost := pair[0], pair[1], pair[2]

		edges[start] = append(edges[start], []int{end, cost})
		edges[end] = append(edges[end], []int{start, cost})

		costs[start][end] = cost
		costs[end][start] = cost

		if cost <= p.th {
			stack[start] = append(stack[start], end)
			stack[end] = append(stack[end], start)
		}
	}

	for true {
		if s.DebugMode() {
			fmt.Println(stack)
		}

		size := -1
		city := -1

		for i := p.num - 1; i >= 0; i-- {
			length := len(stack[i])

			if length == 0 {
				// node i is not connected to any city within the threshold distance
				return i
			}

			if s.DebugMode() {
				fmt.Println(costs[p.num-i-1])
			}

			temp := make([]int, 0, length)

			for j := 0; j < length; j++ {
				curr := stack[i][j]

				for _, edge := range edges[curr] {
					next, cost := edge[0], costs[i][curr]+edge[1]

					if i == next {
						// skip the origin
						continue
					}

					if costs[i][next] == 0 || cost < costs[i][next] {
						// update with the new value
						costs[i][next] = cost

						// if we still have bandwidth to travel from this node, add it to the next iteration
						if cost <= p.th {
							temp = append(temp, next)
						}
					}
				}
			}

			if len(temp) == 0 {
				if size < 0 || length < size {
					size = length
					city = i
				}
			} else {
				stack[i] = temp
			}
		}

		if size >= 0 {
			return city
		}
	}

	return p.num - 1
}
