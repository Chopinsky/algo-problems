package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// UTF8Problems ...
type UTF8Problems struct {
	set []*UTF8
}

// Solve ...
func (p *UTF8Problems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= 0; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == 0 {
				s.Print(i, p.output, result)
			}
		}
	}

	fmt.Println("Algorithm took", time.Since(start))
}

// UTF8 ...
type UTF8 struct {
	data   []int
	output bool
}

// CreateUTF8 ...
func CreateUTF8() s.Problem {
	set := make([]*UTF8, 0, 4)

	set = append(set, &UTF8{
		data:   []int{197, 130, 1},
		output: true,
	})

	set = append(set, &UTF8{
		data:   []int{235, 140, 4},
		output: false,
	})

	return &UTF8Problems{set}
}

const mask = 1<<8 - 1

const oneV = 0
const one = 1 << 7

const twoV = 1<<7 | 1<<6
const two = twoV | 1<<5

const threeV = two
const three = threeV | 1<<4

const fourV = three
const four = fourV | 1<<3

const restV = 1 << 7
const rest = restV | 1<<6

func (p *UTF8) solve() bool {
	count := 0

	for _, val := range p.data {
		num := val & mask

		if count == 0 {
			if num&one == oneV {
				count = 0
			} else if num&two == twoV {
				count = 1
			} else if num&three == threeV {
				count = 2
			} else if num&four == fourV {
				count = 3
			} else {
				return false
			}
		} else {
			if num&rest == restV {
				count--
			} else {
				return false
			}
		}

		// fmt.Println(val, num)
	}

	return true
}
