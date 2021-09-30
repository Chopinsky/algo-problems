package challenges

/*
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.
You call next() the final time and it returns 3, the last element.
Calling hasNext() after that should return false.
Follow up: How would you extend your design to be generic and work with all types, not just integer?
*/

//Below is the interface for Iterator, which is already defined for you.

// Iterator ...
type Iterator struct {
	nextPtr *Iterator
	val     int
}

func (t *Iterator) hasNext() bool {
	return t.nextPtr != nil
}

func (t *Iterator) next() int {
	if t.nextPtr == nil {
		return -1
	}

	val := t.val
	t.nextPtr = t.nextPtr.nextPtr

	return val
}

// PeekingIterator ...
type PeekingIterator struct {
	cursor     *Iterator
	nextQueued bool
	nextVal    int
}

// Constructor ...
func ConstructorPI(iter *Iterator) *PeekingIterator {
	return &PeekingIterator{
		cursor:     iter,
		nextQueued: false,
		nextVal:    0,
	}
}

// hasNext ...
func (t *PeekingIterator) hasNext() bool {
	if t.nextQueued {
		return true
	}

	return t.cursor.hasNext()
}

// next ...
func (t *PeekingIterator) next() int {
	if t.nextQueued {
		val := t.nextVal
		t.nextQueued = false
		t.nextVal = -1
		return val
	}

	return t.cursor.next()
}

// peek ...
func (t *PeekingIterator) peek() int {
	if t.nextQueued {
		return t.nextVal
	}

	t.nextQueued = true
	t.nextVal = t.cursor.next()

	return t.nextVal
}
