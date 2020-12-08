package p1

import (
	"fmt"
	"strconv"
	"time"

	s "go-problems/shared"
)

// MIProblems ...
type MIProblems struct {
	set []*MI
}

// Solve ...
func (p *MIProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= 0; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == 0 {
				s.Print(i, p.output, result)
			}
		}
	}

	fmt.Println("Algorithm finished in:", time.Since(start))
}

// MI ...
type MI struct {
	data   []int
	k      int
	output int
}

// CreateMI ...
func CreateMI() s.Problem {
	set := make([]*MI, 0, 4)

	set = append(set, &MI{
		data:   []int{1, 2, 1, 4},
		k:      2,
		output: 4,
	})

	set = append(set, &MI{
		data:   []int{6, 3, 8, 1, 3, 1, 2, 2},
		k:      4,
		output: 6,
	})

	set = append(set, &MI{
		data:   []int{5, 3, 3, 6, 3, 3},
		k:      3,
		output: -1,
	})

	return &MIProblems{set}
}

func (p *MI) solve() int {
	l := len(p.data)
	c := l / p.k
	nums := p.data

	// idea is to store the min sum after picking the numbers
	// under the index represented by the mask (i.e. the row index),
	// and for certain arrangement, we will get this min sum and saved
	// the value to dp[mask][i], where the optimal arrangement ends
	// with i-th number from the original array, and contains numbers
	// selected from the indices of the numbers in the original array,
	// as represented in the "mask"
	dp := make([][]int, 1<<l)
	for i := range dp {
		dp[i] = make([]int, l)

		for j := range dp[i] {
			dp[i][j] = mod
		}
	}

	// init state: pick only 1 digit from the original group, the current
	// array ends with i-th number, and sum == 0, meaning mask == 1<<i, and
	// dp[1<<i][i] = 0, all other combinations are illegal, hence equal -1.
	for i := 0; i < l; i++ {
		dp[1<<i][i] = 0
	}

	// fmt.Println("dp built, limit:", 1<<l)

	// looping over all posible selections of the numbers from the array,
	// and calculate the min-sum that can be obtained with the mask and
	// ending number
	for s := 1; s < (1 << l); s++ {
		cnt := countDigits(s)

		// fmt.Println(s, cnt)

		// loop over dp[s][i]
		for i := 0; i < l; i++ {
			// dp[s][i] is illegal since s does not contains i-th number
			if s&(1<<i) == 0 {
				continue
			}

			// loop over the next state that can be reached from state s, that is,
			// state s|(1<<j)
			for j := 0; j < l; j++ {
				// dp[s|j][j] is illegal, since s already contain j-th number; we
				// also only consider numbers that are larger than the last one,
				// to guarantee no repeats and sum can be updated
				if s&(1<<j) == 1 {
					continue
				}

				next := s | (1 << j)

				if cnt%c == 0 {
					dp[next][j] = min(dp[next][j], dp[s][i])
				} else if nums[j] > nums[i] {
					dp[next][j] = min(dp[next][j], dp[s][i]+nums[j]-nums[i])
				}
			}
		}
	}

	fmt.Println("final states:", dp[1<<l-1])

	minSum := mod
	for _, val := range dp[1<<l-1] {
		if minSum < 0 || val < minSum {
			minSum = val
		}
	}

	if minSum == mod {
		return -1
	}

	return minSum
}

func countDigits(s int) int {
	count := 0

	for s > 0 {
		if s&1 == 1 {
			count++
		}

		s >>= 1
	}

	return count
}

func (p *MI) solve1() int {
	k := p.k
	n := 0
	nums := make(map[int]int)
	unique := make([]int, 0, k)

	for _, val := range p.data {
		nums[val]++

		if nums[val] > k {
			return -1
		}

		if nums[val] == 1 {
			unique = append(unique, val)
			n |= (1 << (val - 1))
		}
	}

	settings := make(map[int]int)
	buildSettings(settings, unique, 0, 0, 0, len(p.data)/k)

	s := make([]int, 0, len(settings))
	for key := range settings {
		s = append(s, key)
	}

	fmt.Println("num:", strconv.FormatInt(int64(n), 2), settings)

	return minSum(s, settings, nums, 0, 0, k, 0, n)
}

func buildSettings(settings map[int]int, unique []int, key, i, j, k int) {
	if j == k {
		settings[key] = countIC(key)
		return
	}

	for jj := i; jj < len(unique); jj++ {
		buildSettings(settings, unique, key|(1<<(unique[jj]-1)), jj+1, j+1, k)
	}
}

func minSum(settings []int, dist, nums map[int]int, i, j, k, sum, num int) int {
	if j == k {
		return sum
	}

	ans := -1

	for ii := i; ii < len(settings); ii++ {
		s := settings[ii]

		// the remainder numbers can't make up this setting, skip
		if s&num != s {
			continue
		}

		idx := 1
		next := sum + dist[s]

		for s > 0 {
			if s&1 == 1 {
				nums[idx]--

				if nums[idx] == 0 {
					num ^= (1 << (idx - 1))
				}
			}

			s >>= 1
			idx++
		}

		ms := minSum(settings, dist, nums, ii+1, j+1, k, next, num)
		// fmt.Println(i, j, k, ii, next, ms)

		if ans < 0 || (ms >= 0 && ms < ans) {
			ans = ms
		}

		s = settings[ii]
		idx = 1

		for s > 0 {
			if s&1 == 1 {
				nums[idx]++

				if nums[idx] == 1 {
					num |= (1 << (idx - 1))
				}
			}

			s >>= 1
			idx++
		}
	}

	return ans
}

func countIC(s int) int {
	min, max := -1, -1
	idx := 0

	for s > 0 {
		if s&1 == 1 {
			if min < 0 {
				min = idx
			}

			if max < 0 || idx > max {
				max = idx
			}
		}

		s >>= 1
		idx++
	}

	return max - min
}
