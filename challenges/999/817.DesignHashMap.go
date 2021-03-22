package challenges

// MyHashMap ...
type MyHashMap struct {
	store [][]int
}

var mod = 100019

// HMConstructor ...
func HMConstructor() MyHashMap {
	return MyHashMap{
		store: make([][]int, mod),
	}
}

// Put ...
func (t *MyHashMap) Put(key int, value int) {
	i := key % mod
	j := key / mod

	if len(t.store[i]) == 0 {
		t.store[i] = make([]int, 10)
		for k := range t.store[i] {
			t.store[i][k] = -1
		}
	}

	t.store[i][j] = value
}

// Get ...
func (t *MyHashMap) Get(key int) int {
	i := key % mod
	j := key / mod

	if len(t.store[i]) == 0 {
		return -1
	}

	return t.store[i][j]
}

// Remove ...
func (t *MyHashMap) Remove(key int) {
	i := key % mod
	j := key / mod

	if len(t.store[i]) == 0 {
		return
	}

	t.store[i][j] = -1
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */
