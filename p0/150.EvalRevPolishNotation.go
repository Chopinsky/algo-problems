package p0

import (
	"fmt"
	"strconv"
	"time"

	s "go-problems/shared"
)

// ERPNProblems ...
type ERPNProblems struct {
	set []*ERPN
}

// Solve ...
func (p *ERPNProblems) Solve() {
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

// ERPN ...
type ERPN struct {
	data   []string
	output int
}

// CreateERPN ...
func CreateERPN() s.Problem {
	set := make([]*ERPN, 0, 4)

	set = append(set, &ERPN{
		data:   []string{"2", "1", "+", "3", "*"},
		output: 9,
	})

	set = append(set, &ERPN{
		data:   []string{"4", "13", "5", "/", "+"},
		output: 6,
	})

	set = append(set, &ERPN{
		data:   []string{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"},
		output: 22,
	})

	return &ERPNProblems{set}
}

func (p *ERPN) solve() int {
	stack := make([]int, 0, len(p.data))

	var last int

	for _, val := range p.data {
		last = len(stack) - 1

		switch val {
		case "+":
			stack[last-1] += stack[last]
			stack = stack[:last]

		case "-":
			stack[last-1] -= stack[last]
			stack = stack[:last]

		case "*":
			stack[last-1] *= stack[last]
			stack = stack[:last]

		case "/":
			stack[last-1] /= stack[last]
			stack = stack[:last]

		default:
			num, _ := strconv.Atoi(val)
			stack = append(stack, num)
		}
	}

	return stack[0]
}
