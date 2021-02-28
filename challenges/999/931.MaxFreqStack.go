package challenges

// FreqStack ...
type FreqStack struct {
	stack [][]int
	freq  map[int]int
}

// FSConstructor ...
func FSConstructor() FreqStack {
	return FreqStack{
		stack: [][]int{},
		freq:  make(map[int]int),
	}
}

// Push ...
func (t *FreqStack) Push(x int) {
	t.freq[x]++
	count := t.freq[x]

	if count > len(t.stack) {
		t.stack = append(t.stack, []int{})
	}

	t.stack[count-1] = append(t.stack[count-1], x)
	// fmt.Println("push", x, t.stack)
}

// Pop ...
func (t *FreqStack) Pop() int {
	top := len(t.stack) - 1
	if top < 0 {
		return -1
	}

	idx := len(t.stack[top]) - 1
	last := t.stack[top][idx]

	t.stack[top] = t.stack[top][:idx]
	t.freq[last]--

	if len(t.stack[top]) == 0 {
		t.stack = t.stack[:top]
	}

	// fmt.Println("pop", last, t.stack)

	return last
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 */

// FreqStack1 ...
type FreqStack1 struct {
	idx   int
	stack []*num
	count map[int]*num
}

type num struct {
	idx int
	val int
	pos []int
}

// FreqConstructor ...
func FreqConstructor() FreqStack1 {
	return FreqStack1{
		idx:   0,
		stack: []*num{},
		count: make(map[int]*num),
	}
}

// Push ...
func (t *FreqStack1) Push(x int) {
	if n, ok := t.count[x]; ok {
		n.pos = append(n.pos, t.idx)
		t.up(n.idx)
	} else {
		n = &num{
			idx: len(t.stack),
			val: x,
			pos: []int{t.idx},
		}

		t.count[x] = n
		t.stack = append(t.stack, n)
		t.up(len(t.stack) - 1)
	}

	// fmt.Println("push:", x)
	// for _, n := range t.stack {
	//     fmt.Println(n)
	// }

	t.idx++
}

func (t *FreqStack1) up(i int) int {
	c := len(t.stack[i].pos)
	last := t.stack[i].pos[c-1]

	for i > 0 {
		p := (i - 1) / 2
		cp := len(t.stack[p].pos)
		pLast := t.stack[p].pos[cp-1]

		if cp > c || (cp == c && pLast > last) {
			break
		}

		t.stack[i], t.stack[p] = t.stack[p], t.stack[i]
		t.stack[i].idx = i
		t.stack[p].idx = p

		i = p
	}

	return i
}

func (t *FreqStack1) down(i int) int {
	c := len(t.stack[i].pos)
	size := len(t.stack)

	for i < size {
		l, r := 2*i+1, 2*i+2
		next := i
		nextCount := c
		nextLast := -1

		if nextCount > 0 {
			nextLast = t.stack[next].pos[nextCount-1]
		}

		if l < size {
			lCount := len(t.stack[l].pos)
			lLast := -1

			if lCount > 0 {
				lLast = t.stack[l].pos[lCount-1]
			}

			if lCount > nextCount || (lCount == nextCount && lLast > nextLast) {
				next = l
				nextCount = lCount
				nextLast = lLast
			}
		}

		if r < size {
			rCount := len(t.stack[r].pos)
			rLast := -1

			if rCount > 0 {
				rLast = t.stack[r].pos[rCount-1]
			}

			if rCount > nextCount || (rCount == nextCount && rLast > nextLast) {
				next = r
			}
		}

		if next == i {
			break
		}

		t.stack[i], t.stack[next] = t.stack[next], t.stack[i]
		t.stack[i].idx = i
		t.stack[next].idx = next

		i = next
	}

	return i
}

// Pop ...
func (t *FreqStack1) Pop() int {
	if len(t.stack) == 0 {
		return -1
	}

	n := t.stack[0]
	n.pos = n.pos[:len(n.pos)-1]
	t.down(0)

	for i := len(t.stack) - 1; i >= 0; i-- {
		if len(t.stack[i].pos) > 0 {
			t.stack = t.stack[:i+1]
			break
		}

		delete(t.count, t.stack[i].val)
		t.stack[i] = nil
	}

	// fmt.Println("pop", n)
	// for _, n := range t.stack {
	//     fmt.Println(n)
	// }

	return n.val
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 */
