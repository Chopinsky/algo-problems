package problems

import (
	"fmt"
	"strconv"

	d "../../Utils"
)

// TR ...
type TR struct {
	source    []int
	output    int
	testCount int
}

// CreateTR ...
func CreateTR() *TR {
	return &TR{}
}

// Build ...
func (p *TR) Build(test int) {
	p.ResetGlobals()
	p.testCount = 3

	switch test {
	case 1:
		p.source = []int{5, 8}
		p.output = 5

	case 2:
		p.source = []int{11, 13}
		p.output = 6

	default:
		p.source = []int{2, 3}
		p.output = 3

	}
}

var cache map[string]int
var test int

// ResetGlobals ...
func (p *TR) ResetGlobals() {
	cache = make(map[string]int)
}

// Run ...
func (p *TR) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)
			test = i

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcTR(p.source[0], p.source[1]), p.output)

				if d.DEBUG {
					fmt.Println("\n\nBest cases: ", cache)
				}
			} else {
				calcTR(p.source[0], p.source[1])
			}
		}
	}
}

func calcTR(n, m int) int {
	if n == m {
		return 1
	}

	if n <= 0 || m <= 0 {
		return 0
	}

	if n > m {
		// make sure the rectangle is under consistant assumption: n < m
		n, m = m, n
	}

	if n == 1 {
		// the base case
		return m
	}

	key := toKey(n, m)
	if val, ok := cache[key]; ok {
		return val
	}

	// initial best is always filling the rectangle with 1x1 cubics.
	currBest := n * m
	var store []string

	// loop over, divide and conqer
	for a := n; a >= n/2; a-- {
		for b := d.Min(m-a, n); b >= n-a; b-- {
			count := 1
			if b > 0 {
				count++
			}

			ew, eh := m-a-b, b+a-n
			cw, ch := m-b, n-a
			dw, dh := n-b, m-a

			if ew > 0 && eh > 0 {
				count += calcTR(ew, eh)
			}

			if cw > 0 && ch > 0 {
				count += calcTR(cw, ch)
			}

			if dw > 0 && dh > 0 {
				count += calcTR(dw, dh)
			}

			if count < currBest {
				currBest = count

				if d.DEBUG {
					store = []string{
						toKey(a, a), toKey(b, b), toKey(cw, ch),
						toKey(dw, dh), toKey(ew, eh),
					}
				}
			}
		}
	}

	cache[key] = currBest

	if d.DEBUG {
		fmt.Println(key, currBest, store)
	}

	return currBest
}

func toKey(n, m int) string {
	if n > m {
		n, m = m, n
	}

	return strconv.Itoa(n) + "," + strconv.Itoa(m)
}
