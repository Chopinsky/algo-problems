package problems

import d "../../Utils"

// BTBSS ...
type BTBSS struct {
	source []int
	output int
}

// CreateBTBSS ...
func CreateBTBSS() *BTBSS {
	return &BTBSS{}
}

// Build ...
func (p *BTBSS) Build(test int) {
	switch test {
	case 1:
		p.source = []int{7, 11, 5, 3, 6, 4}
		p.output = 4

	case 2:
		p.source = []int{7, 6, 4, 3, 1}
		p.output = 0

	case 3:
		p.source = []int{7, 2, 6, 4, 3, 1, 9}
		p.output = 8

	default:
		p.source = []int{7, 1, 5, 3, 6, 4}
		p.output = 5

	}
}

// Run ...
func (p *BTBSS) Run() {
	d.Output(scan(p.source), p.output)
}

func scan(prices []int) int {
	maxProfit := -1
	currLow := prices[0]

	for i := 1; i < len(prices); i++ {
		profit := prices[i] - currLow
		if profit > maxProfit && profit >= 0 {
			maxProfit = profit
		}

		if prices[i] < currLow {
			// a new low is found
			currLow = prices[i]
		}
	}

	return maxProfit
}
