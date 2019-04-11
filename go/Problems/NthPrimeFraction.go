package problems

import (
	"fmt"
	"sort"

	d "../Utils"
)

type store struct {
	val float32
	src [2]int
}

// NPF ...
type NPF struct {
	source []int
	kth    int
	ans    []int
}

// CreateNPF ...
func CreateNPF() *NPF {
	return &NPF{
		source: nil,
		kth:    0,
		ans:    nil,
	}
}

// Build ...
func (p *NPF) Build(test int) {
	switch test {
	case 1:
		p.source = []int{1, 7}
		p.kth = 1
		p.ans = []int{1, 7}

	default:
		p.source = []int{1, 2, 3, 5}
		p.kth = 3
		p.ans = []int{2, 5}

	}
}

// Run ...
func (p *NPF) Run() {
	d.Debug("Running problem: Nth Prime Fraction", 0)

	len := len(p.source)
	if len < 2 || float32(p.kth) > float32(len*(len-1)/2) {
		fmt.Println(
			"Wrong parameters: (too short array lenth: ", len, ") or (kth exceeding elem count", p.kth, ")",
		)

		return
	}

	result := p.find()

	fmt.Println("Expected result: ", p.ans)
	fmt.Println("Found result: ", result)
}

func (p *NPF) find() [2]int {
	length := len(p.source)
	if p.kth == 1 {
		return [2]int{p.source[0], p.source[length-1]}
	}

	var target *store
	step := length - 2
	count := 1
	size := 2

	for step > 0 {
		if size+count < p.kth {
			count += size
			step--
			size++

			continue
		}

		container := make([]*store, size)
		for i := 0; i < length-step; i++ {
			container[i] = &store{
				val: float32(p.source[i]) / float32(p.source[i+step]),
				src: [2]int{p.source[i], p.source[i+step]},
			}
		}

		sort.Slice(container, func(i, j int) bool {
			return container[i].val < container[j].val
		})

		target = container[p.kth-count-1]
		break
	}

	return [2]int{target.src[0], target.src[1]}
}
