package shared

import "errors"

// MonoQueue ...
type MonoQueue struct {
	data []int
	size int
}

// MonoQueueInit ...
func MonoQueueInit(size int) *MonoQueue {
	realSize := 4 * size
	if realSize <= 0 {
		size = -1
		realSize = 16
	}

	return &MonoQueue {
		data: make([]int, 0, realSize),
		size: size,
	}
}

// Peek ...
func (mq *MonoQueue) Peek() (int, error) {
	if len(mq.data) == 0 {
		return 0, errors.New("empty queue")
	}
	
	return mq.data[0], nil
}

// PopFront ...
func (mq *MonoQueue) PopFront() (int, error) {
	if len(mq.data) == 0 {
		return 0, errors.New("empty queue")
	}
	
	val := mq.data[0]
	mq.data = mq.data[1:]

	return val, nil
}

// Push ... 
func (mq *MonoQueue) Push(val int) {
	qLen := len(mq.data)

	if mq.size > 0 && qLen == mq.size {
		mq.data = mq.data[:mq.size-1]
		qLen--
	}

	idx := qLen - 1
	for idx >= 0 && val >= mq.data[idx] {
		idx--
	}

	if idx != qLen - 1 {
		mq.data = mq.data[:idx+1]
	}

	mq.data = append(mq.data, val)
}
