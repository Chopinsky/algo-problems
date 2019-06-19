package problems

import (
	"fmt"

	d "../Utils"
)

// PESS ...
type PESS struct {
	source []int
	output bool
}

// CreatePESS ...
func CreatePESS() *PESS {
	return &PESS{}
}

// Build ...
func (p *PESS) Build(test int) {
	switch test {
	case 1:
		p.source = []int{1, 25, 27, 2, 4, 12, 31, 23, 55}
		p.output = true

	default:
		p.source = []int{1, 5, 11, 5}
		p.output = true

	}
}

// Run ...
func (p *PESS) Run() {
	// d.Output(p.find(), p.output)
	// d.Output(findDP(p.source), p.output)
	d.Output(findIter(p.source), p.output)
}

func (p *PESS) find() bool {
	r := findSum(p.source, 0)

	for _, val := range r {
		if val == 0 {
			return true
		}
	}

	return false
}

func findSum(arr []int, total int) []int {
	if len(arr) == 1 {
		return []int{total + arr[0], total - arr[0]}
	}

	result := findSum(arr[1:], total+arr[0])
	result = append(result, findSum(arr[1:], total-arr[0])...)

	return result
}

func findDP(arr []int) bool {
	total, min, max := 0, 0, 0
	size := len(arr)

	for _, val := range arr {
		total += val
		if min == 0 || val < min {
			min = val
		}

		if max == 0 || val > max {
			max = val
		}
	}

	if total%2 == 1 {
		return false
	}

	if max > total/2 {
		return false
	}

	dp := make([][]bool, size)
	for i := range dp {
		dp[i] = make([]bool, total+1)
	}

	// init condition
	dp[0][arr[0]] = true

	// dp[i][j] ==> get a sum of `j` using subarray [0, i]
	for i := 1; i < size; i++ {
		for j := min; j <= total; j++ {
			num := arr[i]
			addNum, donNotAddNum := false, false

			if i > 0 {
				donNotAddNum = dp[i-1][j]
			}

			if j >= num {
				addNum = dp[i][j-num]
			}

			dp[i][j] = addNum || donNotAddNum
		}
	}

	if d.DEBUG {
		for i, val := range dp[size-1] {
			fmt.Println("To get sum of: ", i, ", it is possible: ", val)
		}
	}

	return dp[size-1][total/2]
}

func findIter(arr []int) bool {
	total, min, max := 0, 0, 0

	for _, val := range arr {
		total += val
		if min == 0 || val < min {
			min = val
		}

		if max == 0 || val > max {
			max = val
		}
	}

	if total%2 == 1 {
		return false
	}

	threshold := total / 2
	fmt.Println("Total: ", total, "; Threshold: ", threshold)

	if max > threshold {
		return false
	}

	if max == threshold {
		return true
	}

	store := []int{arr[0]}
	var add int

	for i := 1; i < len(arr); i++ {
		temp := make([]int, 0, 2*len(store))

		// sum without this elem ...
		temp = append(temp, store...)

		// only this elem, no previous elem
		temp = append(temp, arr[i])

		// generate all possible sum with this elem
		for j := range store {
			add = store[j] + arr[i]
			if add == threshold {
				return true
			}

			if add < threshold {
				temp = append(temp, add)
			}
		}

		store = temp
	}

	return false
}
