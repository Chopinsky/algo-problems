package problems

import (
	"fmt"
	"sort"

	d "../../Utils"
)

// MLS ...
type MLS struct {
	source    []string
	output    int
	testCount int
}

// CreateMLS ...
func CreateMLS() *MLS {
	return &MLS{}
}

// Build ...
func (p *MLS) Build(test int) {
	p.testCount = 3

	switch test {
	case 1:
		p.source = []string{"cha", "r", "act", "ers"}
		p.output = 6

	case 2:
		p.source = []string{"abcdefghijklmnopqrstuvwxyz"}
		p.output = 26

	default:
		p.source = []string{"un", "iq", "ue"}
		p.output = 4

	}

	p.ResetGlobals(len(p.source))
}

var bitmap map[string]uint32

const charA = byte('a')

// ResetGlobals ...
func (p *MLS) ResetGlobals(count int) {
	bitmap = make(map[string]uint32, count)
}

// Run ...
func (p *MLS) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcMLS(p.source), p.output)
			} else {
				calcMLS(p.source)
			}
		}
	}
}

func buildBitmap(src []string) {
	for _, val := range src {
		insertToBitmap(val)
	}

	if d.DEBUG {
		for k, v := range bitmap {
			fmt.Printf("%s, %b \n", k, v)
		}
	}
}

func insertToBitmap(str string) {
	var bits uint32

	for i := 0; i < len(str); i++ {
		shift := str[i] - charA
		bits |= 1 << shift
	}

	bitmap[str] = bits
}

func calcMLS(src []string) int {
	buildBitmap(src)

	sort.SliceStable(src, func(i, j int) bool { return len(src[i]) < len(src[j]) })

	pos := len(src) - 1
	max := len(src[pos])

	stack := []store{store{
		len: max,
		bit: bitmap[src[pos]],
	}}

	for i := pos - 1; i >= 0; i-- {
		val, size := src[i], len(src[i])
		b := bitmap[val]

		if d.DEBUG {
			fmt.Printf("  %b %d\n", b, b)
			for _, val := range stack {
				fmt.Printf("%d %b %d\n", val.len, val.bit, val.bit)
			}

			fmt.Println("== iter done ==")
		}

		for j := 0; j < len(stack); j++ {
			if isValid(stack[j].bit, b) {
				stack[j].bit |= b
				stack[j].len += size

				if stack[j].len > max {
					max = stack[j].len
				}
			}
		}

		stack = append(stack, store{
			len: size,
			bit: b,
		})
	}

	return max
}

type store struct {
	len int
	bit uint32
}

func isValid(a, b uint32) bool {
	return (a & ^b) == a
}
