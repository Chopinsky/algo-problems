package problems

import d "../Utils"

// SQRT ...
type SQRT struct {
	source int
	output float64
}

// CreateSQRT ...
func CreateSQRT() *SQRT {
	return &SQRT{}
}

// Build ...
func (p *SQRT) Build(test int) {
	switch test {
	case 1:
		p.source = 4
		p.output = 2.

	default:
		p.source = 8
		p.output = 2.82842712474619

	}
}

// Run ...
func (p *SQRT) Run() {
	d.Output(d.Sqrt(p.source), p.output)
}
