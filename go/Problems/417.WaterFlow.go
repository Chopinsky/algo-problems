package problems

// WF ...
type WF struct {
	source []int
	kth    int
}

// CreateWF ...
func CreateWF() *WF {
	return &WF{
		source: nil,
		kth:    0,
	}
}

// Build ...
func (p *WF) Build(test int) {
	switch test {
	default:
		p.source = nil
		p.kth = 0

	}
}

// Run ...
func (p *WF) Run() {
}
