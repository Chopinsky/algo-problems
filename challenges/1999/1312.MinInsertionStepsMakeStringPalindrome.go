package challenges

import "sort"

func minInsertions(s string) int {
	l := len(s)
	if l <= 1 {
		return 0
	}

	dp := make([][]int, l)
	for i := range dp {
		dp[i] = make([]int, l)
	}

	for i := l - 1; i >= 0; i-- {
		for j := i + 1; j < l; j++ {
			// if s[i] == s[j] for range [i, j], then insertions equals
			// the number of insertions for range [i+1, j-1] if i+1 <= j-1
			if s[i] == s[j] {
				dp[i][j] = dp[i+1][j-1]
				continue
			}

			// if s[i] != s[j] for range [i, j], then insert s[i] if [i+1, j]
			// has less insertions, or s[j] if [i, j-1] has less insertions
			dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
		}
	}

	// for _, r := range dp {
	// 	fmt.Println(r)
	// }

	return dp[0][l-1]
}

func minInsertions1(s string) int {
	if len(s) <= 1 {
		return 0
	}

	pos := make([][]int, 26)
	for i := range pos {
		pos[i] = make([]int, 0, len(s)/26)
	}

	for i, ch := range s {
		idx := int(ch - 'a')
		pos[idx] = append(pos[idx], i)
	}

	// fmt.Println(pos)

	dp := make([][]int, len(s))
	for i := range dp {
		dp[i] = make([]int, len(s))
	}

	best := 1
	for i, ch := range s {
		idx := int(ch - 'a')
		set := pos[idx]

		if len(set) == 0 || i == set[len(set)-1] {
			continue
		}

		count := 2 + buildMS(s, pos, dp, i, set[len(set)-1])
		if count > best {
			best = count
		}
	}

	// for _, row := range dp {
	//   fmt.Println(row)
	// }

	return len(s) - best
}

func buildMS(s string, pos, dp [][]int, l, r int) int {
	if l < 0 || r >= len(s) || l+1 >= r {
		return 0
	}

	// only 1 within the range
	if l+2 == r {
		return 1
	}

	if dp[l][r] > 0 {
		return dp[l][r]
	}

	best := 1
	idx := r - 1
	var count int

	for idx > l {
		ch := int(s[idx] - 'a')
		if len(pos[ch]) == 1 || idx == pos[ch][0] {
			idx--
			continue
		}

		p := sort.SearchInts(pos[ch], l)
		if p < len(pos[ch]) && pos[ch][p] == l {
			p++
		}

		if p < len(pos[ch]) && pos[ch][p] <= idx {
			if pos[ch][p] == idx {
				count = 1
			} else {
				count = 2 + buildMS(s, pos, dp, pos[ch][p], idx)
			}

			if count > best {
				best = count
			}
		}

		idx--
	}

	dp[l][r] = best
	return best
}
