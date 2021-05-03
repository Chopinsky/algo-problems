package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MNGGProblems ...
type MNGGProblems struct {
	set []*MNGG
}

// Solve ...
func (p *MNGGProblems) Solve() {
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

// MNGG ...
type MNGG struct {
	data   []int
	batch  int
	output int
}

// CreateMNGG ...
func CreateMNGG() s.Problem {
	set := make([]*MNGG, 0, 4)

	set = append(set, &MNGG{
		data:   []int{1, 2, 3, 4, 5, 6},
		batch:  3,
		output: 4,
	})

	set = append(set, &MNGG{
		data:   []int{1, 3, 2, 5, 2, 2, 1, 6},
		batch:  4,
		output: 4,
	})

	return &MNGGProblems{set}
}

func (p *MNGG) solve() int {
	batch := p.batch
	cnts := make([]int, batch)
	cnt := 0

	// the idea is that if batch is 4, then group of 2, 6, or 10
	// customers will yield a 2 donuts leftover whatsoever, so
	// we can compress states: wether it's a group of 2, 6, or 10
	// people coming in, we treate these groups as the same as
	// the i-th group.
	for _, val := range p.data {
		if val%batch == 0 {
			cnt++
			continue
		}

		cnts[val%batch]++
	}

	total := mixGroups(cnts, make(map[string]int), 0, batch)
	// fmt.Println(cnts, cnt, total)

	return cnt + total
}

func mixGroups(cnts []int, cache map[string]int, leftover, batch int) int {
	key := fmt.Sprint(cnts)
	if val, ok := cache[key]; ok {
		return val
	}

	var ans, happyCount int
	if leftover == 0 {
		happyCount = 1
	}

	for i := 1; i < batch; i++ {
		if cnts[i] == 0 {
			continue
		}

		// take this group in
		cnts[i]--

		// dp recursion: total leftover after taking in customer i is
		// left-over-from-previous-group + (batch - i), where batch - i
		// is the extra leftovers from this group.
		next := happyCount + mixGroups(cnts, cache, (leftover+batch-i)%batch, batch)
		ans = max(ans, next)

		// restore this group
		cnts[i]++
	}

	cache[key] = ans

	return ans
}

func (p *MNGG) solve1() int {
	src := make([]int, 0, len(p.data))
	batch := p.batch
	cnt := 0

	for _, val := range p.data {
		if val%batch == 0 {
			cnt++
		}

		src = append(src, val)

	}

	n := len(src)
	dp := make([]map[int]int, batch)
	next := make([]map[int]int, batch)

	var lo int
	for i, num := range src {
		if num <= batch {
			lo = batch - num
		} else {
			lo = num % batch
		}

		if dp[lo] == nil {
			dp[lo] = make(map[int]int)
		}

		dp[lo][1<<i] = 1
	}

	fmt.Println("before:", dp, cnt)
	var ans int

	for i := 1; i < n; i++ {
		for left, groups := range dp {
			if len(groups) == 0 {
				continue
			}

			for group, cnt := range groups {
				for j, num := range src {
					if group&(1<<j) > 0 {
						continue
					}

					ng := group | (1 << j)
					rem := left + num

					if rem <= batch {
						lo = batch - rem
					} else {
						lo = rem % batch
					}

					if next[lo] == nil {
						next[lo] = make(map[int]int)
					}

					if left == 0 {
						// this group is happy
						next[lo][ng] = max(next[lo][ng], cnt+1)
					} else {
						// the group is not happy, count remains the same
						next[lo][ng] = max(next[lo][ng], cnt)
					}

					if i == n-1 && next[lo][ng] > ans {
						ans = next[lo][ng]
					}
				}
			}
		}

		dp, next = next, dp
		for i := range next {
			next[i] = nil
		}
	}

	fmt.Println("after:", dp, ans)

	return ans + cnt
}
