package problems

import (
	"fmt"

	d "../../Utils"
)

// UNIII ...
type UNIII struct {
	source    []int
	nth       int
	output    int
	testCount int
}

// CreateUNIII ...
func CreateUNIII() *UNIII {
	return &UNIII{}
}

// Build ...
func (p *UNIII) Build(test int) {
	p.ResetGlobals()
	p.testCount = 4

	switch test {
	case 1:
		p.source = []int{2, 3, 4}
		p.nth = 4
		p.output = 6

	case 2:
		p.source = []int{2, 11, 13}
		p.nth = 5
		p.output = 10

	case 3:
		p.source = []int{2, 217983653, 336916467}
		p.nth = 1000000000
		p.output = 1999999972

	default:
		p.source = []int{2, 3, 5}
		p.nth = 3
		p.output = 4

	}
}

// ResetGlobals ...
func (p *UNIII) ResetGlobals() {
}

// Run ...
func (p *UNIII) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcUNIII(p.source, p.nth), p.output)
			} else {
				calcUNIII(p.source, p.nth)
			}
		}
	}
}

func calcUNIII(src []int, nth int) int {
	sort.Ints(src)
	return int(test1(uint64(nth), src))
}

func test1(n uint64, tmp []int) uint64 {
	a, b, c := uint64(tmp[0]), uint64(tmp[1]), uint64(tmp[2])
	if n == 1 {
		return a
	}

	if a*n <= b {
		return a * n
	}

	l, r := a, c*uint64(n)
	lab, lac, lbc := lcd(a, b), lcd(a, c), lcd(b, c)

	if b%a == 0 {
		b = 0
	}

	if (c%a == 0) || (b != 0 && c != 0 && c%b == 0) {
		c = 0
	}

	var total, an, bn, cn uint64
	var m uint64

	for l <= r {
		m = (l + r) / 2

		an, bn, cn = count(m, a, b, c, lab, lac, lbc)
		total = an + bn + cn

		fmt.Println(an, bn, cn, total, m)

		if total == n {
			break
		}

		if total < n {
			l = m + 1
		} else {
			r = m - 1
		}
	}

	var m1, m2, m3 uint64

	m1 = (m / a) * a

	if b != 0 {
		m2 = (m / b) * b
	}

	if c != 0 {
		m3 = (m / c) * c
	}

	fmt.Println("final totals:", m1, m2, m3)

	if m1 >= m2 && m1 >= m3 {
		return m1
	}

	if m2 >= m1 && m2 >= m3 {
		return m2
	}

	return m3
}

func count(num, a, b, c, lab, lac, lbc uint64) (uint64, uint64, uint64) {
	var an, bn, cn uint64

	an = num / a

	if b != 0 {
		bn = num/b - num/lab
	}

	if c != 0 {
		cn = num/c - num/lac

		if b != 0 {
			cn -= num / lbc
		}
	}

	return an, bn, cn
}

func lcd(a, b uint64) uint64 {
	mult := a * b

	if a == b {
		return a
	}

	if a < b {
		a, b = b, a
	}

	for b != 0 {
		a = a % b
		a, b = b, a
	}

	return mult / a
}
