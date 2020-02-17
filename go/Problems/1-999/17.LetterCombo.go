package problems

import (
	"math"

	d "../../Utils"
)

// LC ...
type LC struct {
	source string
	output []string
}

// CreateLC ...
func CreateLC() *LC {
	return &LC{}
}

// Build ...
func (p *LC) Build(test int) {
	switch test {
	default:
		p.source = "23"
		p.output = []string{"ad", "bd", "cd", "ae", "be", "ce", "af", "bf", "cf"}

	}
}

var padMap map[int][]string

const zero = rune('0')

// Run ...
func (p *LC) Run() {
	buildPadMap()
	d.Output(genCombo(p.source), p.output)
}

func buildPadMap() {
	padMap = make(map[int][]string, 10)

	var count rune
	r := rune('a')
	digit := 1

	padMap[0] = []string{"_"}
	padMap[1] = []string{"?"}

	count = 0
	for count < 26 {
		if count < 15 && count%3 == 0 {
			digit++
		} else if count == 19 {
			digit++
		} else if count == 22 {
			digit++
		}

		char := string(r + count)
		padMap[digit] = append(padMap[digit], char)

		count++
	}
}

func genCombo(digits string) []string {
	size := len(digits)
	result := make([]string, 0, int(math.Pow(4., float64(size))))
	result = append(result, getPadChars(digits[0])...)

	for i := 1; i < size; i++ {
		chars := getPadChars(digits[i])
		lc := len(chars)

		dup := result
		for j := 0; j < lc-1; j++ {
			result = append(result, dup...)
		}

		pos := 0
		for c := 0; c < len(result); c++ {
			if c > 0 && c%lc == 0 {
				pos++
			}
			result[c] += chars[pos]
		}
	}

	return result
}

func getPadChars(num byte) []string {
	key := int(rune(num) - zero)
	return padMap[key]
}
