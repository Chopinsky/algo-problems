package problems

import (
	"fmt"
	"strconv"

	d "../../Utils"
)

// NVW ...
type NVW struct {
	words     []string
	puzzles   []string
	output    []int
	testCount int
}

// CreateNVW ...
func CreateNVW() *NVW {
	return &NVW{}
}

// Build ...
func (p *NVW) Build(test int) {
	p.ResetGlobals()
	p.testCount = 1

	switch test {
	default:
		p.words = []string{"aaaa", "asas", "able", "ability", "actt", "actor", "access"}
		p.puzzles = []string{"aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"}
		p.output = []int{1, 1, 3, 2, 4, 0}

	}
}

var dict map[int][]uint32
var baseline byte

// ResetGlobals ...
func (p *NVW) ResetGlobals() {
	baseline = byte('a')
	dict = make(map[int][]uint32, 26)
}

// Run ...
func (p *NVW) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(runNVW(p.words, p.puzzles), p.output)
			} else {
				runNVW(p.words, p.puzzles)
			}
		}
	}
}

func hashWord(src string, toDict bool) uint32 {
	var base uint32

	for i := range src {
		base |= 1 << (src[i] - baseline)
	}

	if toDict {
		num := base
		pos := 0

		for num > 0 {
			if num&1 == 1 {
				dict[pos] = append(dict[pos], base)
			}

			num >>= 1
			pos++
		}
	}

	return base
}

func runNVW(words, puzzles []string) []int {
	for i := range words {
		base := hashWord(words[i], true)

		if d.DEBUG {
			fmt.Println(words[i], " -> ", strconv.FormatInt(int64(base), 2))
		}
	}

	if d.DEBUG {
		fmt.Println(dict)
	}

	result := make([]int, len(puzzles))

	for i := range puzzles {
		key := int(puzzles[i][0] - baseline)
		if w, ok := dict[key]; ok {
			hash := hashWord(puzzles[i], false)
			for j := range w {
				if hash&w[j] == w[j] {
					result[i]++
				}
			}
		}
	}

	return result
}
