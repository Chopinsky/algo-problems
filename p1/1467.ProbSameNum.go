package p1

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// PTBSNProblems ...
type PTBSNProblems struct {
	set []*PTBSN
}

// Solve ...
func (p *PTBSNProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= 0; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == 0 {
				s.Print(i, p.output, result)
				// fmt.Println(p.output * float32(result))
			}
		}
	}

	fmt.Println("Algorithm took", time.Since(start))
}

// PTBSN ...
type PTBSN struct {
	data   []int
	output float32
}

// CreatePTBSN ...
func CreatePTBSN() s.Problem {
	set := make([]*PTBSN, 0, 4)

	set = append(set, &PTBSN{
		data:   []int{1, 1},
		output: 1.0,
	})

	set = append(set, &PTBSN{
		data:   []int{2, 1, 1},
		output: 0.66667,
	})

	set = append(set, &PTBSN{
		data:   []int{1, 2, 1, 2},
		output: 0.60000,
	})

	set = append(set, &PTBSN{
		data:   []int{3, 2, 1},
		output: 0.30000,
	})

	set = append(set, &PTBSN{
		data:   []int{6, 6, 6, 6, 6, 6},
		output: 0.90327,
	})

	return &PTBSNProblems{set}
}

var factors map[int]uint64
var counts map[int]uint64
var store [][]uint64
var sum []int

func (p *PTBSN) solve() float64 {
	factors = make(map[int]uint64)
	counts = make(map[int]uint64)

	store = make([][]uint64, 0, 1<<uint(len(p.data)))
	sum = make([]int, len(p.data)+1)

	sort.Ints(p.data)

	count, size := p.count(), len(p.data)
	base1 := make([]int, size)
	base2 := make([]int, size)

	// fmt.Println("metadata:", count, p.data, sum, factors)

	p.fillAndCalc(base1, base2, count/2, 0, size, 0, 0, count/2)

	// if len(store) < 100 {
	// 	fmt.Println("store", store)
	// }

	return findRatio(count)
}

func (p *PTBSN) count() int {
	count, max := 0, 0
	// arr := append([]int(nil), p.data...)

	for idx, val := range p.data {
		count += val
		sum[idx+1] = sum[idx] + val

		if val > max {
			max = val
		}
	}

	factors[0] = 1
	for i := 1; i <= max; i++ {
		factors[i] = factors[i-1] * uint64(i)
	}

	return count
}

func (p *PTBSN) fillAndCalc(base, other []int, cells, idx, size, c1, c2, remainder int) {
	if remainder == 0 {
		for i := idx; i < size; i++ {
			base[i] = 0
			other[i] = p.data[idx]
			c2++
		}

		//todo: run calculations
		accum(base, other, size, cells, c1 == c2)

		return
	}

	leftover := remainder - sum[size] + sum[idx+1]

	// all balls in [idx:size] needs to fall into the 1st box
	if p.data[idx] == leftover {
		for i := idx; i < size; i++ {
			base[i] = p.data[i]
			other[i] = 0
			c1++
		}

		//todo: run calculations
		accum(base, other, size, cells, c1 == c2)

		return
	}

	var o1, o2 int

	if idx < size-1 {
		start := 0
		end := p.data[idx]

		if leftover > 0 {
			start = leftover
		}

		if end > remainder {
			end = remainder
		}

		for i := start; i <= end; i++ {
			if i > 0 {
				o1 = 1
			} else {
				o1 = 0
			}

			if i < p.data[idx] {
				o2 = 1
			} else {
				o2 = 0
			}

			base[idx] = i
			other[idx] = p.data[idx] - i

			p.fillAndCalc(base, other, cells, idx+1, size, c1+o1, c2+o2, remainder-i)

			//todo: run calculations
			// l, r = p.calc(base, size, cells), p.calc(other, size, cells)
		}

		return
	}

	if remainder > 0 {
		c1++
	}

	if remainder < p.data[idx] {
		c2++
	}

	base[idx] = remainder
	other[idx] = p.data[idx] - remainder

	//todo: run calculations

	accum(base, other, size, cells, c1 == c2)

	return
}

func calc(src []int, size, cells int) uint64 {
	arr := append([]int(nil), src...)
	sort.Ints(arr)

	key := 0
	for i := size - 1; i >= 0; i-- {
		if arr[i] == 0 {
			break
		}

		key = key*10 + arr[i]
	}

	if val, ok := counts[key]; ok {
		return val
	}

	last, base := size-1, uint64(1)
	factor := factors[arr[last]]

	for i := uint64(cells); i > 1; i-- {
		base *= i

		if factor > 1 && base%factor == 0 {
			base /= factor

			if last > 0 {
				last--
				factor = factors[arr[last]]
			} else {
				factor = 1
			}
		}
	}

	// if size > 4 {
	// 	fmt.Println(arr, base)
	// }

	counts[key] = base

	return base
}

func accum(base, other []int, size, cells int, valid bool) {
	l, r := calc(base, size, cells), calc(other, size, cells)

	var diff uint64
	if valid {
		diff = 1
	} else {
		diff = 0
	}

	store = append(store, []uint64{diff, l, r})
}

func findRatio(count int) float64 {
	var valid, total uint64
	var gcd uint64

	if count >= 8 {
		// find common denominators
		for _, vals := range store {
			if len(vals) == 0 {
				continue
			}

			if gcd == 0 {
				gcd = s.GCDUint64(vals[1], vals[2])
			} else {
				gcd = s.GCDUint64(vals[1], gcd)
				gcd = s.GCDUint64(vals[2], gcd)
			}
		}
	} else {
		gcd = 1
	}

	// fmt.Println("GCD:", gcd)

	// do easy multi
	for _, vals := range store {
		if len(vals) == 0 {
			continue
		}

		base := (vals[1] / gcd) * (vals[2] / gcd)
		total += base

		if vals[0] == 1 {
			valid += base
		}
	}

	return float64(valid) / float64(total)
}
