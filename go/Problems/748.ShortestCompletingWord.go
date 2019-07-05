package problems

import (
	"fmt"
	"sort"

	d "../Utils"
)

// SCW ...
type SCW struct {
	source    []string
	plate     string
	output    []string
	testCount int
}

// CreateSCW ...
func CreateSCW() *SCW {
	return &SCW{}
}

// Build ...
func (p *SCW) Build(test int) {
	p.ResetGlobals()
	p.testCount = 2

	switch test {
	case 1:
		p.source = []string{"looks", "pest", "stew", "show"}
		p.plate = "1s3 456"
		p.output = []string{"pest", "stew", "show"}

	default:
		p.source = []string{"step", "steps", "stripe", "stepple"}
		p.plate = "1s3 PSt"
		p.output = []string{"steps"}

	}
}

var dict map[string][]int

// ResetGlobals ...
func (p *SCW) ResetGlobals() {
	dict = make(map[string][]int)
}

// Run ...
func (p *SCW) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)
			buildDict(p.source)

			fmt.Println("\nTest case: ", i, ":")
			d.Output(p.searchWord(), p.output)
		}

		fmt.Println()
	}
}

func (p *SCW) searchWord() []string {
	plate := extractPlateStr(p.plate)
	if val, ok := dict[plate]; ok {
		res := make([]string, len(val)-1)

		for i := range val {
			if i > 0 {
				res[i-1] = p.source[val[i]]
			}
		}

		return res
	}

	return nil
}

func extractPlateStr(plate string) string {
	r := []rune(plate)
	res := make([]rune, 0, len(r))

	for i := range r {
		if r[i] <= 90 && r[i] >= 65 {
			res = append(res, r[i]+32)
		} else if r[i] <= 122 && r[i] >= 97 {
			res = append(res, r[i])
		}
	}

	return string(sortString(res))
}

func sortString(src []rune) []rune {
	sort.Slice(src, func(i, j int) bool { return src[i] < src[j] })
	return src
}

func buildDict(words []string) {
	for i := range words {
		insertWord(sortString([]rune(words[i])), words[i], i, len(words[i]))
	}
}

func insertWord(word []rune, src string, pos, l int) {
	size := len(word)
	if size == 0 {
		return
	}

	for i := range word {
		for j := i; j < size; j++ {
			w := string(word[i : j+1])

			if val, ok := dict[w]; ok {
				if l < val[0] {
					dict[w] = []int{l, pos}
				} else if l == val[0] {
					found := false

					for k := range val {
						if k > 0 && val[k] == pos {
							found = true
							break
						}
					}

					if !found {
						dict[w] = append(val, pos)
					}
				}
			} else {
				dict[w] = []int{l, pos}
			}
		}

		if i < size-1 {
			insertWord(word[i+1:], src, pos, l)
		}
	}
}
