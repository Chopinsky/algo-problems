package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MPIProblems ...
type MPIProblems struct {
	set []*MPI
}

// Solve ...
func (p *MPIProblems) Solve() {
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

// MPI ...
type MPI struct {
	data   string
	k      int
	output string
}

// CreateMPI ...
func CreateMPI() s.Problem {
	set := make([]*MPI, 0, 4)

	set = append(set, &MPI{
		data:   "4321",
		k:      4,
		output: "1342",
	})

	set = append(set, &MPI{
		data:   "100",
		k:      1,
		output: "010",
	})

	set = append(set, &MPI{
		data:   "36789",
		k:      1000,
		output: "36789",
	})

	set = append(set, &MPI{
		data:   "22",
		k:      22,
		output: "22",
	})

	set = append(set, &MPI{
		data:   "9438957234785635408",
		k:      23,
		output: "0345989723478563548",
	})

	return &MPIProblems{set}
}

func (p *MPI) solve() string {
	l, src := len(p.data), p.data
	k := p.k
	mv := make([]bool, l)

	ptr := 0
	best, bestPos, curr := 10, -1, 10
	res := ""

	for ptr < l && k > 0 {
		if src[ptr] == '0' {
			ptr++
			continue
		}

		curr = int(src[ptr] - '0')
		best = curr
		bestPos = -1
		shift := 1

		for i := ptr + 1; shift <= k && i < l; i++ {
			if mv[i] {
				continue
			}

			val := int(src[i] - '0')
			shift++

			if val < best {
				best = val
				bestPos = i
			}

			if val == 0 {
				break
			}
		}

		if bestPos > 0 {
			mv[bestPos] = true
			res += src[bestPos : bestPos+1]
			k -= bestPos - ptr
		} else {
			mv[ptr] = true
			res += src[ptr : ptr+1]
			ptr++
		}

		if s.DebugMode() {
			fmt.Println(ptr, best, bestPos, k, res)
		}
	}

	for i := 0; i < l; i++ {
		if !mv[i] {
			res += src[i : i+1]
		}
	}

	return res
}
