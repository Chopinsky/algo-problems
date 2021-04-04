package challenges

type MyCircularQueue struct {
	store []int
	l     int
	r     int
	count int
}

func Constructor(k int) MyCircularQueue {
	return MyCircularQueue{
		store: make([]int, k),
		l:     0,
		r:     -1,
		count: 0,
	}
}

func (t *MyCircularQueue) EnQueue(value int) bool {
	if t.IsFull() {
		return false
	}

	t.r++
	t.count++

	if t.r >= len(t.store) {
		t.r = 0
	}

	t.store[t.r] = value
	return true
}

func (t *MyCircularQueue) DeQueue() bool {
	if t.IsEmpty() {
		return false
	}

	t.l++
	t.count--

	if t.l >= len(t.store) {
		t.l = 0
	}

	return true
}

func (t *MyCircularQueue) Front() int {
	if t.IsEmpty() {
		return -1
	}

	return t.store[t.l]
}

func (t *MyCircularQueue) Rear() int {
	if t.IsEmpty() {
		return -1
	}

	return t.store[t.r]
}

func (t *MyCircularQueue) IsEmpty() bool {
	return t.count == 0
}

func (t *MyCircularQueue) IsFull() bool {
	return t.count == len(t.store)
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.EnQueue(value);
 * param_2 := obj.DeQueue();
 * param_3 := obj.Front();
 * param_4 := obj.Rear();
 * param_5 := obj.IsEmpty();
 * param_6 := obj.IsFull();
 */
