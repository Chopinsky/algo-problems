package problems

import "fmt"

// XXX ...
type XXX struct {
	source    []int
	output    int
	testCount int
}

// CreateXXX ...
func CreateXXX() *XXX {
	return &XXX{}
}

// Build ...
func (p *XXX) Build(test int) {
	p.ResetGlobals()
	p.testCount = 1

	switch test {
	default:
		p.source = nil
		p.output = 0

	}
}

// ResetGlobals ...
func (p *XXX) ResetGlobals() {
}

// Run ...
func (p *XXX) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			//TODO: write code here ...

			fmt.Println("\nTest case: ", i, ":")
			// d.Output(result, p.output)
		}

		fmt.Println()
	}
}
