package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// SCIIProblems ...
type SCIIProblems struct {
	set []*SCII
}

// Solve ...
func (p *SCIIProblems) Solve() {
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

// SCII ...
type SCII struct {
	data   string
	k      int
	output int
}

// CreateSCII ...
func CreateSCII() s.Problem {
	set := make([]*SCII, 0, 4)

	set = append(set, &SCII{
		data:   "aaabcccd",
		k:      2,
		output: 4,
	})

	set = append(set, &SCII{
		data:   "aabbaa",
		k:      2,
		output: 2,
	})

	set = append(set, &SCII{
		data:   "aaaaaaaaaaa",
		k:      0,
		output: 3,
	})

	return &SCIIProblems{set}
}

func (p *SCII) solve() int {
	size := len(p.data)
	if p.k >= size {
		return 0
	}

	// dp: for every move, create dp with 26 x (k+1) grid, each bearing [2]int,
	//     where grid[i][j][0] = current count; grid[i][j][1] = total length
	//     except the current character

	dp := make([][][][][]int, size)
	for i := range dp {
		dp[i] = make([][][][]int, p.k+1)

		for j := range dp[i] {
			dp[i][j] = make([][][]int, 26)
		}
	}

	char := int(p.data[0] - 'a')
	dp[0][0][char] = [][]int{{ 1, 0, }}
	var d [][]int

	for i := 1; i < size; i++ {
		char = int(p.data[i] - 'a')

		// delete all characters before this one
		if i <= p.k {
			dp[i][i][char] = [][]int{{ 1, 0, }}
		}

		for j := 0; j <= p.k; j++ {
			for k := 0; k < 26; k++ {
				d = dp[i-1][j][k]

				// not seen previously
				if d == nil || len(d) == 0 {
					continue
				}

				for l := range d {
					// if we delete the current char
					if j < p.k {
						setVal(dp, i, j+1, k, d[l][0], d[l][1])
					}

					// if we add the current char to the string
					if char == k {
						// same char, increatment the count
						setVal(dp, i, j, char, d[l][0]+1, d[l][1])
					} else {
						// different char, update the total, count's reset to 1
						setVal(dp, i, j, char, 1, getScore(d[l][0], d[l][1]))
					}
				}
			}
		}

		// fmt.Println("\n+++", i+1, "-", string(p.data[i]), "+++")
		// for j := range dp[i] {
		// 	fmt.Println(j, ":", dp[i][j][:4])
		// }
	}

	var best, total int
	// fmt.Println(dp[size-1])

	for j := 0; j <= p.k; j++ {
		for k := 0; k < 26; k++ {
			d = dp[size-1][j][k]

			if d == nil || len(d) == 0 {
				continue
			}

			total = getScore(d[0][0], d[0][1])
			if best == 0 || total < best {
				best = total
			}
		}
	}

	return best
}

func setVal(dp [][][][][]int, i, j, k, count, total int) {
	d := dp[i][j][k]
	if d == nil || len(d) == 0 {
		dp[i][j][k] = [][]int{{ count, total, }}
		return
	}

	last := getScore(d[0][0], d[0][1])
	curr := getScore(count, total)

	if curr > last {
		return
	}

	// clearing out
	if curr < last {
		dp[i][j][k] = dp[i][j][k][len(d):]
	}

	dp[i][j][k] = append(dp[i][j][k], []int{ count, total })
}

func getScore(count, total int) int {
	if count == 1 {
		return total + 1
	}

	c := 0
	for count > 0 {
		count /= 10
		c++
	}

	return total + c + 1
}

type info struct {
	last      byte
	lastCount int
	total     int
}

func (n *info) update() {
	if n.lastCount == 1 {
		n.total++
		return
	}

	t := n.lastCount
	c := 0

	for t > 0 {
		t /= 10
		c++
	}

	n.total += c + 1
}
