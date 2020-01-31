package main

import (
	"fmt"
	s "go-problems/shared"
	"strconv"
)

// XXXProblems ...
type XXXProblems struct {
	set []*XXX
}

// Solve ...
func (p *XXXProblems) Solve() {
	fmt.Println()

	for i, p := range p.set {
		result := p.solve()
		s.Print(i, strconv.Itoa(p.output), strconv.Itoa(result))
	}
}

// XXX ...
type XXX struct {
	data   []int
	output int
}

// CreateXXX ...
func CreateXXX() s.Problem {
	set := make([]*XXX, 0, 4)

	set = append(set, &XXX{
		data:   []int{},
		output: 0,
	})

	return &XXXProblems{set}
}

func (p *XXX) solve() int {
	return 0
}
