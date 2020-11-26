package challenges

import (
	"math"
	"math/bits"
)

func racecar(target int) int {
	visited := make([]int, target*2)

	if target == 0 {
		return 0
	}

	return walk(target, visited)
}

func walk(target int, visited []int) int {
	if visited[target] > 0 {
		return visited[target]
	}

	if target == 0 {
		return 0
	}

	// now do the math, t must fall in a range: 2^(n-1) <= t <= 2^n - 1,
	// and consider the lower range first: we've not reached the target,
	// so let's take

	// n is the boundary that we don't need to cross
	n := int(math.Ceil(math.Log2(float64(target + 1))))
	b0, b1 := 1<<(n-1), 1<<n-1

	// we can get to the target with full A^n steps
	if b0 == target {
		visited[target] = n
		return n
	}

	// recursively finding the steps to reach the
	// target: (A^n)R....., or: n 1 + remainder;
	// this case also covers the (b1 == target) condition
	visited[target] = (n + 1) + walk(b1-target, visited)

	// now, assume that we run some and then turn back, and calculate
	// the remainder diest to the target: A^(n-1)RA^(m)R, and find a
	// better solution --> total steps are (n-1) + 1 + m + 1 => n+m+1
	for m := 0; m < n; m++ {
		dist := b0 - 1<<m
		visited[target] = min(visited[target], n+m+1+walk(target-dist, visited))
	}

	return visited[target]
}

func racecar1(target int) int {
	dp := make([]int, target+3)
	for i := range dp {
		if i == 0 {
			dp[0] = 0
		}

		if i == 1 {
			dp[1] = 1
		}

		if i == 2 {
			dp[2] = 4
		}

		if i > 2 {
			dp[i] = -1
		}
	}

	if target <= 2 {
		return dp[target]
	}

	var k, base, start int

	for i := 3; i <= target; i++ {
		// k = 32 - bits.LeadingZeros32(uint32(i))
		k = bits.Len(uint(i))
		base = 1 << k

		// case 1: the car can get here with A^(k-1)/R moves, which gets us
		//         to (2^k)-1, and cost (k - 1 + 1) -> k steps to get there
		if i == base-1 {
			dp[i] = k
			continue
		}

		// case 2: the car can get here with A^(k-1)/R/A^j/R moves, which gets
		//         us to 2^(k-1) - 2^j, and it costs (k-1 + 1 + j + 1)
		//         -> (k + j + 1) steps
		for j := 0; j < k-1; j++ {
			start = dp[i-(1<<(k-1))+(1<<j)]
			if start < 0 {
				continue
			}

			dp[i] = minRC(dp[i], start+k+j+1)
		}

		// case 3: the car drives cross the target at A^k/R moves, with
		//         the cost of k + 1
		if base-1-i < i {
			start = dp[base-1-i]
			if start >= 0 {
				dp[i] = minRC(dp[i], start+k+1)
			}
		}
	}

	// fmt.Println(dp)

	return dp[target]
}

func minRC(a, b int) int {
	if a < 0 {
		return b
	}

	if b < 0 {
		return a
	}

	if a <= b {
		return a
	}

	return b
}
