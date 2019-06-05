package problems

import (
	"fmt"
	"sort"

	d "../Utils"
)

var (
	tasks = make(map[string]int)
	keys  []string
)

// TSE ...
type TSE struct {
	source   []string
	interval int
	output   int
}

// CreateTSE ...
func CreateTSE() *TSE {
	return &TSE{}
}

// Build ...
func (p *TSE) Build(test int) {
	switch test {
	case 1:
		p.source = []string{"A", "A", "A", "B", "B", "C"}
		p.interval = 2
		p.output = 7

	case 2:
		p.source = []string{"A", "A", "A", "B", "B", "A"}
		p.interval = 3
		p.output = 13

	default:
		p.source = []string{"A", "A", "A", "B", "B", "B"}
		p.interval = 2
		p.output = 8

	}
}

// Run ...
func (p *TSE) Run() {
	// p.build()
	// d.Output(p.schedule(), p.output)

	d.Output(p.schedule2(p.build2()), p.output)
}

func (p *TSE) build() {
	keys = make([]string, len(p.source))

	for _, task := range p.source {
		if _, ok := tasks[task]; !ok {
			keys = append(keys, task)
		}

		tasks[task]++
	}
}

func (p *TSE) schedule() int {
	queue := make([]string, 0, len(p.source))
	for len(tasks) > 0 {
		for _, key := range keys {
			if val, ok := tasks[key]; ok {
				queue = append(queue, key)

				if val > 1 {
					tasks[key] = val - 1
				} else {
					delete(tasks, key)
				}
			}

			if len(tasks) == 0 {
				break
			}
		}
	}

	actual := make([]string, 0, p.interval*len(p.source))
	window := make(map[string]int)
	qi, ai := 0, 0

	for qi < len(queue) {
		// if task already in the window (i.e. val > 0), needs to add an idle period;
		// otherwise, add the latest elem into the window. Regardless, we will push
		// out the front elem, yet we're still at elem {i}
		next := queue[qi]

		if window[next] == 0 {
			// value not yet in the window
			qi++
		} else {
			// adding an idle period
			next = "IDLE"
		}

		if ai >= p.interval {
			// push out the front elem if we've enough elem in the window
			if window[actual[ai-p.interval]] > 0 {
				window[actual[ai-p.interval]]--
			}
		}

		ai++
		window[next]++
		actual = append(actual, next)

		// fmt.Println(ai, qi, window)
	}

	d.Debug(actual, 0)

	return len(actual)
}

type task struct {
	key   string
	count int
}

func (p *TSE) build2() []*task {
	for _, task := range p.source {
		tasks[task]++
	}

	t := make([]*task, 0, len(tasks))
	for k, v := range tasks {
		t = append(t, &task{
			key:   k,
			count: v,
		})
	}

	sort.Slice(t, func(i, j int) bool {
		return t[i].count > t[j].count
	})

	// for _, task := range t {
	// 	fmt.Println(task)
	// }

	return t
}

func (p *TSE) schedule2(t []*task) int {
	slots, length := t[0].count, p.interval+1
	size := slots * length
	queue := make([]string, size)

	for s := 0; s < slots; s++ {
		idx := 0
		for p := 0; p < length; p++ {
			for {
				if idx >= len(t) {
					// out of the bound
					break
				}

				if t[idx].count > 0 {
					// found the task to fulfill
					break
				}

				// moving on
				idx++
			}

			if idx >= len(t) {
				// done with all the remaining tasks, moving on to the next slot
				break
			}

			// set the task to be executed at this time period (slot+offset); also update the
			// global states of the remaining tasks
			queue[s*length+p] = t[idx].key
			t[idx].count--
			idx++
		}
	}

	if d.DEBUG {
		for i, val := range queue {
			fmt.Println(i, val)
		}
	}

	for i := size - 1; i >= 0; i-- {
		if len(queue[i]) > 0 {
			return i + 1
		}
	}

	return 0
}
