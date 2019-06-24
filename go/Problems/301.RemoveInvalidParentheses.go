package problems

import (
	"fmt"

	d "../Utils"
)

// RIP ...
type RIP struct {
	source string
	output []string
}

// CreateRIP ...
func CreateRIP() *RIP {
	return &RIP{}
}

// Build ...
func (p *RIP) Build(test int) {
	p.ResetGlobals()

	switch test {
	case 1:
		p.source = "(a)())()"
		p.output = []string{"(a())()", "(a)()()"}

	case 2:
		p.source = ")("
		p.output = []string{}

	case 3:
		p.source = "()))))))(((*)"
		p.output = []string{"()(*)"}

	case 4:
		p.source = ")())("
		p.output = []string{"()"}

	default:
		p.source = "()())()"
		p.output = []string{"(())()", "()()()"}

	}
}

var (
	left        = byte(rune(')'))
	right       = byte(rune('('))
	validation  = make(map[string]bool)
	combination = make(map[string][]string)
	globalMax   = 0
)

const tests = 5

// Run ...
func (p *RIP) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Trial:", j, "============")

		for i := 0; i < tests; i++ {
			fmt.Println("\nTest case: ", i, ":")
			p.Build(i)

			l, r := count(p.source)
			fmt.Println("Bracket Imbalance: left ->", l, "; right ->", r)

			result := scanTrim(p.source)
			d.Output(result, p.output)
		}

		fmt.Println()
	}
}

// ResetGlobals ...
func (p *RIP) ResetGlobals() {
	validation = make(map[string]bool)
	combination = make(map[string][]string)
	globalMax = 0
}

func extract(src string) string {
	size := len(src)
	if size == 0 {
		return ""
	}

	if size == 1 {
		if src[0] == left || src[0] == right {
			return ""
		}

		return src
	}

	result := ""
	i, j := 0, size-1

	for i < size {
		if src[i] == right {
			break
		}

		if src[i] != left {
			result += string(src[i])
		}

		i++
	}

	suffix := ""
	for j > i {
		if src[j] == left {
			break
		}

		if src[j] != right {
			suffix = string(src[j]) + suffix
		}

		j--
	}

	result += src[i:j+1] + suffix

	return result
}

func scanTrim(src string) []string {
	src = extract(src)
	length := len(src)

	if length == 0 || length < globalMax {
		return []string{}
	}

	if res, ok := combination[src]; ok {
		return res
	}

	if validate(src) {
		res := []string{src}
		combination[src] = res

		if length > globalMax {
			globalMax = length
		}

		return res
	}

	max, size := 0, 0
	target := ""
	m := make(map[string]struct{})
	var combos []string

	for i := 0; i < length; i++ {
		if src[i] != left && src[i] != right {
			continue
		}

		if i > 0 && src[i] == src[i-1] {
			// skipping the case we've already visited
			continue
		}

		target = src[:i] + src[i+1:]
		if _, ok := m[target]; ok {
			continue
		}

		combos = scanTrim(target)

		for i := range combos {
			if _, ok := m[combos[i]]; ok {
				continue
			}

			size = len(combos[i])
			if size < max {
				continue
			}

			max = size
			m[combos[i]] = empty
		}
	}

	result := make([]string, 0, len(m))
	for k := range m {
		if len(k) < max {
			continue
		}

		result = append(result, k)
	}

	combination[src] = result
	return result
}

func validate(src string) bool {
	if len(src) == 0 {
		return true
	}

	if res, ok := validation[src]; ok {
		return res
	}

	score := 0
	for i := 0; i < len(src); i++ {
		if src[i] == right {
			score++
		} else if src[i] == left {
			score--
		}

		if score < 0 {
			validation[src] = false
			return false
		}
	}

	validation[src] = score == 0
	return score == 0
}

func count(src string) (int, int) {
	l, r := 0, 0
	for i := 0; i < len(src); i++ {
		if src[i] == left {
			l++
		}

		if src[i] == right {
			if l == 0 {
				r++
			} else {
				l--
			}
		}
	}

	return l, r
}

/*
func trim(src string, score int) []string {
	// get the max leagal outlayer
	src = extractMain(src)
	size := len(src)

	if size == 0 {
		return []string{}
	}

	if size == 1 && (src[0] == left || src[0] == right) {
		return []string{}
	}

	m := make(map[string]struct{})
	max := 0
	result := []string{}

	var body, remainder string
	var pos, pScore int

	// scan to the left, generate one possible combo set
	pScore, pos = scanLeft(src)
	if pScore == 0 {
		return []string{src}
	}

	if pos >= 0 {
		body, remainder = src[:pos], src[pos:]
		m, max = scanDeeper(body, remainder, max, pScore, m)
	} else {
		//todo: remove 1 and go deeper
	}

	// scan to the right, generate another possible combo set
	pScore, pos = scanRight(src)
	if pScore == 0 {
		return []string{src}
	}

	if pos >= 0 {
		remainder, body = src[:pos], src[pos:]
		m, max = scanDeeper(body, remainder, max, pScore, m)
	} else {
		//todo: remove 1 and go deeper
	}

	// flatten the final result
	for k := range m {
		if len(k) == max {
			result = append(result, k)
		}
	}

	return result
}

func scanDeeper(body, remainder string, max, score int, m map[string]struct{}) (map[string]struct{}, int) {
	res := trim(body, score)
	var temp string

	if len(res) == 0 {
		m[remainder] = empty
		if len(remainder) > max {
			max = len(remainder)
		}

		return m, max
	}

	for i := range res {
		temp = res[i] + remainder
		m[temp] = empty
		if len(temp) > max {
			max = len(temp)
		}
	}

	return m, max
}

func scanLeft(src string) (int, int) {
	i, score, lastPos := len(src)-1, 0, -1

	for i >= 0 {
		if src[i] == left {
			score--
		} else if src[i] == right {
			score++
		}

		if score == 0 {
			lastPos = i
		}

		i--
	}

	return score, lastPos
}

func scanRight(src string) (int, int) {
	i, score, lastPos := 0, 0, -1

	for i < len(src) {
		if src[i] == left {
			score--
		} else if src[i] == right {
			score++
		}

		if score == 0 {
			lastPos = i
		}

		i++
	}

	return score, lastPos
}
*/
