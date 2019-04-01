package problems

// NGN ...
type NGN struct {
	source []int
	kth    int
}

// CreateNGN ...
func CreateNGN() *NGN {
	return &NGN{
		source: nil,
		kth:    0,
	}
}

// Build ...
func (p *NGN) Build(test int) {
	switch test {
	default:
		p.source = nil
		p.kth = 0

	}
}

// Run ...
func (p *NGN) Run() {
}
