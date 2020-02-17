package problems

import "fmt"

// NGN ...
type NGN struct {
	source []int
	target []int
	stack  mStack
}

// CreateNGN ...
func CreateNGN() *NGN {
	return &NGN{
		source: nil,
		target: nil,
		stack: mStack{
			inner: []int{},
		},
	}
}

// Build ...
func (p *NGN) Build(test int) {
	switch test {
	case 1:
		p.source = []int{2, 7, 4, 3, 5}
		p.target = []int{7, 0, 5, 5, 0}

	case 2:
		p.source = []int{1, 7, 5, 1, 9, 2, 5, 1}
		p.target = []int{7, 9, 9, 9, 0, 5, 0, 0}

	default:
		p.source = []int{2, 1, 5}
		p.target = []int{5, 5, 0}

	}
}

// Run ...
func (p *NGN) Run() {
	length := len(p.source)
	ans := make([]int, length)

	for i := length - 1; i >= 0; i-- {
		val := p.stack.push(p.source[i])
		ans[i] = val
	}

	fmt.Println("Expected answer: ", p.target)
	fmt.Println("Calculated answer: ", ans)
}

type mStack struct {
	inner []int
}

func (s *mStack) push(val int) int {
	length := len(s.inner)
	if length == 0 {
		s.inner = []int{val}
		return 0
	}

	if val < s.inner[0] {
		s.inner = append([]int{val}, s.inner...)
		return s.inner[1]
	}

	pos := length
	for i := length - 1; i >= 0; i-- {
		if val >= s.inner[i] {
			// found the elem to truncate from in the stack, keep from i+1
			pos = i + 1
			break
		}
	}

	if pos == length {
		s.inner = []int{val}
		return 0
	}

	s.inner = append([]int{val}, s.inner[pos:]...)
	return s.inner[1]
}

func (s *mStack) peek() int {
	if len(s.inner) == 0 {
		return -1
	}

	return s.inner[0]
}

func (s *mStack) pop() int {
	if len(s.inner) == 0 {
		return -1
	}

	res := s.inner[0]
	s.inner = s.inner[1:]

	return res
}

func (s *mStack) size() int {
	return len(s.inner)
}
