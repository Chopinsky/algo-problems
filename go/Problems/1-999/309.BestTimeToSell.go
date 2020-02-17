package problems

import (
	"math"

	d "../../Utils"
)

// BTTS ...
type BTTS struct {
	source []int
	max    int
	output []string
}

// CreateBTTS ...
func CreateBTTS() *BTTS {
	return &BTTS{}
}

// Build ...
func (p *BTTS) Build(test int) {
	switch test {
	case 1:
		p.source = []int{5, 4, 3, 2, 1, 0, 10}
		p.max = 10
		p.output = []string{"c", "c", "c", "c", "c", "c"}

	default:
		p.source = []int{1, 2, 3, 0, 2}
		p.max = 3
		p.output = []string{"b", "s", "c", "b", "s"}

	}
}

// Run ...
func (p *BTTS) Run() {
	d.Output(p.calc(), p.output)
}

func (p *BTTS) calc() int {
	size := len(p.source)
	if size < 2 {
		return 0
	}

	var profit, prev, max int
	dp := make([]int, size)

	for i := 1; i < size; i++ {
		// we can always have the previous max by not operating since the
		// date we achieved this current max profit forward
		dp[i] = max

		for j := 0; j < i; j++ {
			profit = d.Max(p.source[i]-p.source[j], 0)
			if j >= 3 {
				// a cooldown is possible, and dp[i] >= 0 guranteed
				prev = dp[j-2]
			} else {
				// if not a possible previous profit, use 0
				prev = 0
			}

			// calc the max profit at day i
			dp[i] = d.Max(dp[i], profit+prev)
			if dp[i] > max {
				// update the max so far
				max = dp[i]
			}
		}
	}

	d.Debug(dp, 0)

	return dp[size-1]
}

func (p *BTTS) calc2() int {
	// rest -- no stock in holding, can be from a rest from last turn, or a sold at last turn
	// hold -- after buy, can be a new buy or a holding from previous holding
	// sold -- sell stock this turn: from holding last turn plus the profit
	var sold, rest, hold int
	hold = math.MinInt32

	for _, val := range p.source {
		hold = d.Max(hold, rest-val) // hold from last buy, or a new buy (from rest)
		rest = d.Max(rest, sold)     // rest from do nothing still, or sold last turn (meaning we have to rest this turn)
		sold = hold + val            // sold from last hold
	}

	return d.Max(rest, sold)
}
