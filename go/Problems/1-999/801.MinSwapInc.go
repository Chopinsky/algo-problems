package problems

import (
	"fmt"

	d "../../Utils"
)

// MSI ...
type MSI struct {
	srcA  []int
	srcB  []int
	swaps int
}

// CreateMSI ...
func CreateMSI() *MSI {
	return &MSI{
		srcA:  nil,
		srcB:  nil,
		swaps: 0,
	}
}

// Build ...
func (p *MSI) Build(test int) {
	switch test {
	default:
		p.srcA = []int{1, 3, 5, 4}
		p.srcB = []int{1, 2, 3, 7}
		p.swaps = 1

	}
}

// Run ...
func (p *MSI) Run() {
	fmt.Println("Expected result: ", p.swaps)
	fmt.Println("Calculated result: ", p.findAlt(1))
}

func (p *MSI) find() int {
	size := len(p.srcA)
	if size < 2 {
		return 0
	}

	count := 0
	for i := size - 1; i > 0; i-- {
		if (p.srcA[i] <= p.srcA[i-1] && (i == size-1 || p.srcA[i] < p.srcB[i+1])) || (p.srcB[i] <= p.srcB[i-1] && (i == size-1 || p.srcB[i] < p.srcA[i+1])) {
			p.swap(i)
			count++
		}
	}

	if count >= len(p.srcA)/2 {
		count = len(p.srcA) - count
	}

	d.Debug(p.srcA, 0)
	d.Debug(p.srcB, 0)

	return count
}

func (p *MSI) findAlt(method int) int {
	size := len(p.srcA)
	if size < 2 {
		return 0
	}

	swap := make([]int, size)
	keep := make([]int, size)

	swap[0] = 1
	keep[0] = 0

	if method == 0 {
		for i := 1; i < size; i++ {
			swap[i] = d.MaxInt
			keep[i] = d.MaxInt

			// attribute satisfied
			if p.srcA[i] > p.srcA[i-1] && p.srcB[i] > p.srcB[i-1] {
				keep[i] = keep[i-1]     // if keep, no need to update
				swap[i] = swap[i-1] + 1 // need to swap A[i] and B[i] as well
			}

			// swap possible
			if p.srcA[i] > p.srcB[i-1] && p.srcB[i] > p.srcA[i-1] {
				keep[i] = d.Min(keep[i], swap[i-1])
				swap[i] = d.Min(swap[i], keep[i-1]+1)
			}
		}
	} else {
		for i := 1; i < size; i++ {
			if p.srcA[i] <= p.srcA[i-1] || p.srcB[i] <= p.srcB[i-1] {
				// not satisfying the condition, swap this pos or the last pos
				swap[i] = keep[i-1] + 1
				keep[i] = swap[i-1]
			} else {
				// satisfying the conditions, can swap or not?
				if p.srcA[i] > p.srcB[i-1] && p.srcB[i] > p.srcA[i-1] {
					// can also swap
					swap[i] = d.Min(swap[i-1], keep[i-1]) + 1
					keep[i] = d.Min(swap[i-1], keep[i-1])
				} else {
					// can't swap, must keep the order in sync
					swap[i] = swap[i-1] + 1
					keep[i] = keep[i-1]
				}
			}
		}
	}

	if d.DEBUG == true {
		fmt.Println(swap, keep)
	}

	return d.Min(swap[size-1], keep[size-1])
}

func (p *MSI) swap(pos int) {
	if pos >= len(p.srcA) {
		return
	}

	temp := p.srcA[pos]
	p.srcA[pos] = p.srcB[pos]
	p.srcB[pos] = temp
}
