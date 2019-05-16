package problems

// SWM ...
type SWM struct {
	source []int
	output int
}

// CreateSWM ...
func CreateSWM() *SWM {
	return &SWM{}
}

// Build ...
func (p *SWM) Build(test int) {
	switch test {
	default:
		p.source = nil
		p.output = 0

	}
}

// Run ...
func (p *SWM) Run() {
}
