package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MAPRProblems ...
type MAPRProblems struct {
	set []*MAPR
}

// Solve ...
func (p *MAPRProblems) Solve() {
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

// MAPR ...
type MAPR struct {
	data   [][]int
	extra  int
	output float32
}

// CreateMAPR ...
func CreateMAPR() s.Problem {
	set := make([]*MAPR, 0, 4)

	set = append(set, &MAPR{
		data: [][]int{
			{1, 2}, {3, 5}, {2, 2},
		},
		extra:  2,
		output: 0.78333,
	})

	set = append(set, &MAPR{
		data: [][]int{
			{2, 4}, {3, 9}, {4, 5}, {2, 10},
		},
		extra:  4,
		output: 0.53485,
	})

	return &MAPRProblems{set}
}

func (p *MAPR) solve() float32 {
	q := make(FloatQueue, 0, len(p.data))
	for _, class := range p.data {
		s := float32(class[0])
		t := float32(class[1])
		q.Push([]float32{-(s+1)/(t+1) + s/t, s, t})
	}

	// fmt.Println(q)

	extra := p.extra
	for extra > 0 {
		a := q.Pop().([]float32)

		a[1] += 1.0
		a[2] += 1.0
		a[0] = -(a[1]+1)/(a[2]+1) + a[1]/a[2]

		q.Push(a)
		extra--
	}

	total := float32(0)
	div := float32(0)

	for q.Len() > 0 {
		a := q.Pop().([]float32)
		// fmt.Println(a)

		total += a[1] / a[2]
		div += 1.0
	}

	// fmt.Println(total, div)

	return total / div
}
