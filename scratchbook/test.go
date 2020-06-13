package main

import (
	"fmt"
	"io/ioutil"
	"math/rand"
)

func main() {
	cmds, err := ioutil.ReadFile("cmds.json")
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println("Done ... ", string(cmds))
}

// RandomizedSet ...
type RandomizedSet struct {
	dict  map[int]int
	store []int
	size  int
}

/** Initialize your data structure here. */
func Constructor() RandomizedSet {
	return RandomizedSet{
		dict:  make(map[int]int),
		store: make([]int, 0, 64),
		size:  0,
	}
}

// Insert ...
func (this *RandomizedSet) Insert(val int) bool {
	// exists
	if _, ok := this.dict[val]; ok {
		return false
	}

	// insert

	if len(this.store) == this.size {
		this.store = append(this.store, val)
	} else {
		this.store[this.size] = val
	}

	this.dict[val] = this.size
	this.size++

	return true
}

/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {
	var pos int

	if idx, ok := this.dict[val]; ok {
		pos = idx
	} else {
		return false
	}

	delete(this.dict, val)

	if this.size > 1 {
		lastVal := this.store[this.size-1]
		this.store[pos] = lastVal
		this.dict[lastVal] = pos
	}

	this.size--

	return true
}

/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
	pos := rand.Intn(this.size)
	return this.store[pos]
}
