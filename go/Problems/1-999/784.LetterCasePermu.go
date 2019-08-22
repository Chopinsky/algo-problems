package problems

import (
	"fmt"
	"unicode"
)

// LCP ...
type LCP struct {
	source string
	output []string
}

// CreateLCP ...
func CreateLCP() *LCP {
	return &LCP{}
}

// Build ...
func (p *LCP) Build(test int) {
	switch test {
	case 1:
		p.source = "3z4"
		p.output = []string{
			"3z4",
			"3Z4",
		}

	case 2:
		p.source = "12345"
		p.output = []string{"12345"}

	default:
		p.source = "a1b2"
		p.output = []string{
			"a1b2",
			"A1b2",
			"a1B2",
			"A1B2",
		}
	}
}

// Run ...
func (p *LCP) Run() {
	result := permutCase(p.source)
	fmt.Println(result)
}

func permutCase(source string) []string {
	var first, second string
	var index int

	stack := []string{source}
	src := []rune(source)

	for i := 0; i < len(src); i++ {
		if unicode.IsNumber(src[i]) {
			continue
		}

		temp := make([]string, 2*len(stack))
		index = 0

		for _, w := range stack {
			first, second = generate(w, i)
			if len(first) > 0 {
				temp[index] = first
				index++
			}

			if len(second) > 0 {
				temp[index] = second
				index++
			}
		}

		stack = temp
	}

	return stack
}

func generate(src string, pos int) (string, string) {
	if pos >= len(src) {
		return "", ""
	}

	r := []rune(src)
	if unicode.IsLower(r[pos]) {
		r[pos] = unicode.ToUpper(r[pos])
	} else {
		r[pos] = unicode.ToLower(r[pos])
	}

	return src, string(r)
}
