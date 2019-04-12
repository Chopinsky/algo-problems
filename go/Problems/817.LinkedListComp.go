package problems

// LLC ...
type LLC struct {
	source []int
	kth    int
}

// CreateLLC ...
func CreateLLC() *LLC {
	return &LLC{
		source: nil,
		kth:    0,
	}
}

// Build ...
func (p *LLC) Build(test int) {
	switch test {
	default:
		p.source = nil
		p.kth = 0

	}
}

// Run ...
func (p *LLC) Run() {
}
