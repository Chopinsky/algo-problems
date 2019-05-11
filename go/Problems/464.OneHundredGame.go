package problems

import "fmt"

// OHG ...
type OHG struct {
	maxInt uint
	total  uint
	output bool
}

// CreateOHG ...
func CreateOHG() *OHG {
	return &OHG{}
}

// Build ...
func (p *OHG) Build(test int) {
	switch test {
	case 1:
		p.maxInt = 15
		p.total = 100
		p.output = true

	case 2:
		p.maxInt = 3
		p.total = 4
		p.output = false

	default:
		p.maxInt = 10
		p.total = 11
		p.output = false

	}
}

// Run ...
func (p *OHG) Run() {
	fmt.Println("Calculated result: ", p.canWin(p.total, 0))
	fmt.Println("Expected result: ", p.output)
}

func (p *OHG) canWin(num, mask uint) bool {
	var i uint
	for i = 1; i <= p.maxInt; i++ {
		if checkBit(mask, i-1) {
			// if the number has already been picked, skip
			continue
		}

		if i >= num {
			// if we can win with this number, return true
			return true
		}

		newMask := maskBit(mask, i-1)
		if !p.canWin(num-i, newMask) {
			// my opponent's turn, if he can't win the game, then I will
			return true
		}
	}

	return false
}

func maskBit(source, pos uint) uint {
	return source | (1 << pos)
}

func checkBit(source, pos uint) bool {
	if source&(1<<pos) != 0 {
		return true
	}

	return false
}
