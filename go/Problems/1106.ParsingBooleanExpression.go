package problems

import (
	"fmt"

	d "../Utils"
)

// PBE ...
type PBE struct {
	source    string
	output    bool
	testCount int
}

// CreatePBE ...
func CreatePBE() *PBE {
	return &PBE{}
}

// Build ...
func (p *PBE) Build(test int) {
	p.ResetGlobals()
	p.testCount = 4

	switch test {
	case 1:
		p.source = "|(f,t)"
		p.output = true

	case 2:
		p.source = "&(t,f)"
		p.output = false

	case 3:
		p.source = "|(&(t,f,t),!(t))"
		p.output = false

	default:
		p.source = "!(f)"
		p.output = true

	}
}

const (
	not          = rune('!')
	or           = rune('|')
	and          = rune('&')
	leftBracket  = rune('(')
	rightBracket = rune(')')
	tVal         = rune('t')
	fVal         = rune('f')
)

// ResetGlobals ...
func (p *PBE) ResetGlobals() {
}

// Run ...
func (p *PBE) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			fmt.Println("\nTest case: ", i, ":")
			d.Output(parseBoolExpr(p.source), p.output)
		}

		fmt.Println()
	}
}

func parseBoolExpr(expr string) bool {
	size := len(expr)
	stack := make([][]int, 0, size/3)
	index := size - 1

	var currStack []int // [trueCount, falseCount]
	var op, char rune   // '!', '|', or '&'
	var res bool
	var n int

	for index >= 0 {
		char = rune(expr[index])

		if char == leftBracket {
			if index < 1 {
				fmt.Println("Failed to parse: the expression has no finishing operator", expr)
				return false
			}

			res = evalExpr(currStack, rune(expr[index-1]))
			n = len(stack)

			// we're done, no more stack to eval
			if n == 0 {
				return res
			}

			// pop the stack and update the current level
			currStack, stack = stack[n-1], stack[:n-1]
			if res {
				currStack[0]++
			} else {
				currStack[1]++
			}

			// we've evaluated the operator as well, back 1 more space
			index--
		} else if char == rightBracket {
			// push the current stack into the stack queue, if it exists
			if currStack != nil {
				stack = append(stack, currStack)
			}

			// open a new stack for the current level
			currStack = make([]int, 2)
		} else if char == tVal {
			currStack[0]++
		} else if char == fVal {
			currStack[1]++
		}

		// the last case is delimiter ',', no need to handle it since we're in the current stack
		index--
	}

	return evalExpr(currStack, op)
}

func evalExpr(vals []int, op rune) bool {
	d.Debug(fmt.Sprintln("Evaluating: ", vals, string(op)), 0)

	if op == not {
		if vals[0] == 1 {
			return false
		}

		if vals[1] == 1 {
			return true
		}

		fmt.Println("Illegal argument to eval: ", vals, op)
		return false
	}

	if op == and {
		return !(vals[1] > 0)
	}

	if op == or {
		return vals[0] > 0
	}

	fmt.Println("Illegal argument to eval: ", vals, op)
	return false
}
