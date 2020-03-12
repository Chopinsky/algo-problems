package p1

import (
	"fmt"
	"time"

	s "../shared"
)

// FPSProblems ...
type FPSProblems struct {
	set []*FPS
}

// Solve ...
func (p *FPSProblems) Solve() {
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

// FPS ...
type FPS struct {
	data   [][]int
	n      int
	time   int
	target int
	output float32
}

// CreateFPS ...
func CreateFPS() s.Problem {
	set := make([]*FPS, 0, 4)

	set = append(set, &FPS{
		data: [][]int{
			{1, 2},
			{1, 3},
			{1, 7},
			{2, 4},
			{2, 6},
			{3, 5},
		},
		n:      7,
		time:   2,
		target: 4,
		output: 0.16666666667,
	})

	set = append(set, &FPS{
		data: [][]int{
			{1, 2},
			{1, 3},
			{1, 7},
			{2, 4},
			{2, 6},
			{3, 5},
		},
		n:      7,
		time:   1,
		target: 7,
		output: 0.3333333333,
	})

	set = append(set, &FPS{
		data: [][]int{
			{1, 2},
			{1, 3},
			{1, 7},
			{2, 4},
			{2, 6},
			{3, 5},
		},
		n:      7,
		time:   20,
		target: 6,
		output: 0.16666666667,
	})

	return &FPSProblems{set}
}

func (p *FPS) solve() float32 {
	m := make(map[int][]int, p.n)
	for i := 0; i < len(p.data); i++ {
		f, t := p.data[i][0], p.data[i][1]
		m[f] = append(m[f], t)
		m[t] = append(m[t], f)
	}

	count := make([]int, p.n)
	count[0] = len(m[1])

	stack := make([]int, 0, 1<<uint(p.n))
	stack = append(stack, p.encode(1, 0))

	for i := 0; i < p.time; i++ {
		if len(stack) == 0 {
			break
		}

		temp := make([]int, 0, 1<<uint(p.n))

		for j := 0; j < len(stack); j++ {
			pos, parent := p.decode(stack[j])
			base := count[pos-1]

			if next, ok := m[pos]; ok && len(next) > 0 {
				size := len(next)

				for _, val := range next {
					if val == p.target {
						if len(m[val]) == 1 || i == p.time-2 {
							return 1. / float32(base)
						}

						if s.DEBUG {
							fmt.Println(size, i)
						}

						return 0
					}

					if val == parent {
						continue
					}

					count[val-1] = base * (size - 1)
					temp = append(temp, p.encode(val, pos))
				}
			} else {
				fmt.Println("[error] the node has to be connected to the tree:", pos)
			}
		}

		stack = temp
	}

	fmt.Println("count", count)

	return 0
}

func (p *FPS) encode(pos, parent int) int {
	return parent*p.n + pos - 1
}

func (p *FPS) decode(val int) (int, int) {
	return (val % p.n) + 1, val / p.n
}
