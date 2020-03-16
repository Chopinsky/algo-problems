package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MSTEProblems ...
type MSTEProblems struct {
	set []*MSTE
}

const runs = 20

// Solve ...
func (p *MSTEProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= runs; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == runs {
				s.Print(i, p.output, result)
			}
		}
	}

	fmt.Println("Algorithm took", time.Since(start))
}

// MSTE ...
type MSTE struct {
	data   [][]string
	output int
}

// CreateMSTE ...
func CreateMSTE() s.Problem {
	set := make([]*MSTE, 0, 4)

	set = append(set, &MSTE{
		data: [][]string{
			{"#", ".", "#", "#", ".", "#"},
			{".", "#", "#", "#", "#", "."},
			{"#", ".", "#", "#", ".", "#"},
		},
		output: 4,
	})

	set = append(set, &MSTE{
		data: [][]string{
			{"#", ".", ".", ".", "#"},
			{".", "#", ".", "#", "."},
			{".", ".", "#", ".", "."},
			{".", "#", ".", "#", "."},
			{"#", ".", ".", ".", "#"},
		},
		output: 10,
	})

	set = append(set, &MSTE{
		data: [][]string{
			{".", "#"},
			{"#", "#"},
			{"#", "."},
			{"#", "#"},
			{".", "#"},
		},
		output: 3,
	})

	return &MSTEProblems{set}
}

func (p *MSTE) solve() int {
	height, width := len(p.data), len(p.data[0])
	settings, rowBest := p.getRowScores(nil, nil, p.data[0], 0, width)

	if s.DebugMode() {
		fmt.Println(settings)
	}

	for i := 1; i < height; i++ {
		settings, rowBest = p.getRowScores(settings, p.data[i-1], p.data[i], rowBest, width)

		if s.DebugMode() {
			fmt.Println(settings)
		}
	}

	// set := s.GenerateBinarySet(9, 4)
	// for _, val := range set {
	// 	fmt.Printf("%b\n", val)
	// }

	return rowBest
}

func (p *MSTE) getRowScores(lastSettings [][]int, lastRow, currRow []string, lastRowBest, width int) ([][]int, int) {
	best := lastRowBest
	lastLen := len(lastSettings)

	settings := make([][]int, 0, (1<<(uint(width)+1))-1)

	// row structure: [setting, rowCount, totalCount]
	settings = append(settings, []int{0, 0, lastRowBest})

	for i := 0; i < width; i++ {
		// if a broken chair, skip it
		if currRow[i] == "#" {
			continue
		}

		// the 1st seat in the row
		if i == 0 {
			score := 0

			if lastRow != nil && width > 1 && lastRow[1] != "#" {
				// loop over last settings and check if this one will be allowed
				for i := 0; i < lastLen; i++ {
					if lastSettings[i][0]&2 == 0 && score < lastSettings[i][2]+1 {
						score = lastSettings[i][2] + 1
					}
				}

				// if we've encountered at least 1 setting that will allow this setting, add it
				if score > 0 {
					settings = append(settings, []int{1, 1, score})
				}
			} else {
				// we don't have the last row rstriction for the given reasons, so the best score is self + last_row_best
				score = lastRowBest + 1
				settings = append(settings, []int{1, 1, score})
			}

			if score > best {
				best = score
			}

			continue
		}

		// i > 0
		leftTaken := 1 << (uint(i) - 1)
		currTaken := 1 << uint(i)
		size := len(settings)

		for j := 0; j < size; j++ {
			// the left seat is broken so it's always available;
			// if to this setting, the left seat is not taken, then it's sit-able, adding it to the settings
			if currRow[i-1] == "#" || settings[j][0]&leftTaken == 0 {
				score, setting, rowCount := 0, settings[j][0]|currTaken, settings[j][1]

				// i is guaranteed to be 1 or larger
				if lastRow != nil && lastRow[i-1] != "#" && (i == width-1 || lastRow[i+1] != "#") {
					required := (setting << 1) | (setting >> 1)
					for k := 0; k < lastLen; k++ {
						if lastSettings[k][0]&required == 0 {
							// score = total from the setting + total in the current setting so far (excluding self) + self
							currScore := lastSettings[k][2] + rowCount + 1
							if score < currScore {
								score = currScore
							}
						}
					}

					if score > 0 {
						settings = append(settings, []int{setting, rowCount + 1, score})
					}
				} else {
					score = settings[j][2] + 1
					settings = append(settings, []int{setting, rowCount + 1, score})
				}

				if score > best {
					best = score
				}
			}
		}
	}

	return settings, best
}
