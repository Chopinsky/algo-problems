package problems

import (
	"fmt"

	d "../Utils"
)

var gloablSmall = -1

// CCHG ...
type CCHG struct {
	source []int
	amount int
	output int
}

// CreateCCHG ...
func CreateCCHG() *CCHG {
	return &CCHG{}
}

// Build ...
func (p *CCHG) Build(test int) {
	switch test {
	default:
		p.source = []int{1, 2, 5}
		p.amount = 11
		p.output = 3

	}
}

// Run ...
func (p *CCHG) Run() {
	d.Output(p.findCombo3(), p.output)
}

func (p *CCHG) findCombo() int {
	dp := make([]int, p.amount+1)

	for i := len(p.source) - 1; i >= 0; i-- {
		dp = setBase(dp, p.source[i], p.amount)
	}

	for i := p.source[0] + 1; i < p.amount+1; i++ {
		dp = update(dp, i)
	}

	fmt.Println(dp)

	if dp[p.amount] == 0 {
		return -1
	}

	return dp[p.amount]
}

func setBase(dp []int, base, amount int) []int {
	i := 1
	var val int

	for {
		val = base * i
		if val > amount {
			break
		}

		if dp[val] == 0 || i < dp[val] {
			dp[val] = i
		}

		i++
	}

	d.Debug(fmt.Sprintln(base, dp), 0)

	return dp
}

func update(dp []int, index int) []int {
	for i := 1; i <= index/2; i++ {
		if dp[i] == 0 || dp[index-i] == 0 {
			// invalid combo
			continue
		}

		// calc the new possible combo
		val := dp[i] + dp[index-i]
		if val < dp[index] {
			dp[index] = val
		}
	}

	return dp
}

func (p *CCHG) findCombo2() int {
	dp := make([]int, p.amount+1)

	for i := 0; i < len(p.source); i++ {
		dp = updateCombo(dp, p.source[i])
	}

	return dp[p.amount]
}

func updateCombo(dp []int, base int) []int {
	if base >= len(dp) {
		return dp
	}

	for i := base; i < len(dp); i++ {
		if i > base && dp[i-base] == 0 {
			// invalid combo
			continue
		}

		// only need 1 coin now
		val := dp[i-base] + 1
		if dp[i] == 0 || val < dp[i] {
			dp[i] = val
		}
	}

	return dp
}

func (p *CCHG) findCombo3() int {
	return bfsCoinChange(p.source, p.amount, 0)
}

func bfsCoinChange(coins []int, amount, total int) int {
	if amount < 0 {
		return -1
	}

	if amount == 0 {
		// end game: if we've reached limit
		if gloablSmall == -1 || total < gloablSmall {
			gloablSmall = total
		}

		return 0
	}

	size := len(coins)
	base := coins[size-1]
	smallest := -1
	var finalCount int

	for count := amount / base; count >= 0; count-- {
		if gloablSmall != -1 && total+count > gloablSmall {
			// skip the larger counts
			continue
		}

		remainder := amount - base*count
		if size > 1 {
			// what we can get with the remaining portion of coins
			finalCount = bfsCoinChange(coins[:size-1], remainder, total+count)
		} else if remainder == 0 {
			// total + count is a final match
			finalCount = total + count
		} else {
			// we have no more coins to spare
			finalCount = -1
		}

		if finalCount != -1 && (smallest == -1 || finalCount < smallest) {
			smallest = finalCount
			if gloablSmall == -1 || smallest < gloablSmall {
				gloablSmall = smallest
			}
		}
	}

	return smallest
}
