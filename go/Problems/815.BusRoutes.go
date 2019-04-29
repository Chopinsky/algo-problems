package problems

import (
	"fmt"

	d "../Utils"
)

// BR ...
type BR struct {
	routes [][]int
	start  int
	target int
	output int
}

// CreateBR ...
func CreateBR() *BR {
	return &BR{}
}

// Build ...
func (p *BR) Build(test int) {
	switch test {
	default:
		p.routes = [][]int{
			{1, 2, 7},
			{3, 6, 7},
		}
		p.start = 1
		p.target = 6
		p.output = 2

	}
}

// Run ...
func (p *BR) Run() {
	var result int
	for i := 0; i < 1000; i++ {
		result = p.calcAlt()
	}

	fmt.Println("Calculated bus routes: ", result)
	fmt.Println("Expected bus routes: ", p.output)
}

func (p *BR) calc() int {
	if p.start == p.target {
		return 1
	}

	// stop -> buses
	stops := make(map[int][]int)

	// buses -> stop
	buses := make(map[int][]int)

	// build the maps
	for i := range p.routes {
		// i = bus
		for _, j := range p.routes[i] {
			// j = stop
			stops[j] = append(stops[j], i)
			buses[i] = append(buses[i], j)
		}
	}

	d.Debug(stops, 0)
	d.Debug(buses, 0)

	var curr []info
	if buses, ok := stops[p.start]; ok {
		curr = make([]info, len(buses))
		for i, bus := range buses {
			curr[i] = info{p.start, bus, 1}
		}
	} else {
		return -1
	}

	visited := make(map[int]struct{}) // stops we have visited
	size := 0
	count := -1

	for {
		size = len(curr)
		if size == 0 {
			// can't reach the destination, break
			d.Debug("Break because exhausted...", 0)
			break
		}

		temp := []info{}

		for _, stopInfo := range curr {
			visited[stopInfo.stop] = empty
			conn := stops[stopInfo.stop]

			for _, bus := range conn {
				next := buses[bus]
				for _, nextStop := range next {
					if _, ok := visited[nextStop]; ok {
						continue
					} else {
						c := stopInfo.count
						if stopInfo.bus != bus {
							c++
						}

						if nextStop == p.target && (count < 0 || c < count) {
							count = c
						}

						temp = append(temp, info{nextStop, bus, c})
					}
				}
			}
		}

		curr = temp
	}

	return count
}

func (p *BR) calcAlt() int {
	if p.start == p.target {
		return 1
	}

	count := -1

	// stop -> buses
	stops := make(map[int][][]int)
	buses := make(map[int][]int)

	// build the bi-directional graph
	for i := range p.routes {
		// i = bus
		last := len(p.routes[i]) - 1
		for pos := range p.routes[i] {
			left := pos - 1
			right := pos + 1
			stop := p.routes[i][pos]

			if pos == 0 {
				left = last
			}

			if pos == last {
				right = 0
			}

			stops[stop] = append(stops[stop], []int{p.routes[i][left], i})
			stops[stop] = append(stops[stop], []int{p.routes[i][right], i})

			buses[stop] = append(buses[stop], i)
		}
	}

	d.Debug(stops, 0)

	var curr []info
	if b, ok := buses[p.start]; ok {
		curr = make([]info, len(b))
		for i, bus := range b {
			curr[i] = info{p.start, bus, 1}
		}
	} else {
		return -1
	}

	visited := make(map[int]struct{})
	for {
		size := len(curr)
		if size == 0 {
			break
		}

		temp := []info{}
		for _, me := range curr {
			visited[me.stop] = empty

			for _, neighbor := range stops[me.stop] {
				if _, ok := visited[neighbor[0]]; ok {
					continue
				}

				c := me.count
				if me.bus != neighbor[1] {
					c++
				}

				if neighbor[0] == p.target && (count < 0 || c < count) {
					count = c
				}

				temp = append(temp, info{neighbor[0], neighbor[1], c})
			}
		}

		curr = temp
	}

	return count
}

type info struct {
	stop  int
	bus   int
	count int
}
