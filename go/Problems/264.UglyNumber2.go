package problems

import (
	"math"

	d "../Utils"
)

var (
	poisonPrimes = []int{7, 11, 13, 17, 19, 23, 29, 31, 37, 41}
	uglyNums     = []int{1, 2, 3, 4, 5, 6}
)

// UN2 ...
type UN2 struct {
	source int
	output int
}

// CreateUN2 ...
func CreateUN2() *UN2 {
	return &UN2{}
}

// Build ...
func (p *UN2) Build(test int) {
	switch test {
	case 1:
		p.source = 1501
		p.output = 860934420

	default:
		p.source = 10
		p.output = 12

	}
}

// Run ...
func (p *UN2) Run() {
	d.Output(find2(p.source), p.output)
}

func find(nth int) int {
	num := 0
	count := 0

	for count < nth {
		num++
		if checkUgly(num) {
			d.Debug(num, 0)

			if num > 6 {
				uglyNums = append(uglyNums, num)
			}

			count++
		}
	}

	return num
}

func checkUgly(num int) bool {
	if num <= 1681 {
		return isUgly(num)
	}

	return isUgly2(num)
}

func isUgly(num int) bool {
	if num < 7 {
		return true
	}

	upper := int(math.Sqrt(float64(num)))
	for _, val := range poisonPrimes {
		if val > num {
			// early break
			return true
		}

		if val == num {
			// found the not-so-ugly prime,
			return false
		}

		if val <= upper && num%val == 0 {
			// the num has factor other than the ugly few
			return false
		}
	}

	return true
}

func isUgly2(num int) bool {
	for {
		if num == 1 {
			return true
		}

		if num%5 == 0 {
			num /= 5
		} else if num%3 == 0 {
			num /= 3
		} else if num%2 == 0 {
			num /= 2
		} else {
			return false
		}
	}
}

func find2(nth int) int {
	base := []int{1}
	i2, i3, i5, next, last, count := 0, 0, 0, 1, 1, 1
	var num2, num3, num5 int

	for count < nth {
		num2, num3, num5 = base[i2]*2, base[i3]*3, base[i5]*5
		last = next

		next = d.Min(num2, num3)
		next = d.Min(next, num5)

		if next == num2 {
			i2++
		} else if next == num3 {
			i3++
		} else {
			i5++
		}

		if next <= last {
			// a duplidate
			continue
		}

		base = append(base, next)
		count++
	}

	d.Debug(base, 0)

	return next
}
