package main

import (
	"fmt"
	"io/ioutil"
	"math/rand"
	"strconv"
	"strings"
)

func main() {
	rawCmds, err := ioutil.ReadFile("cmds.json")
	if err != nil {
		fmt.Println("error", err)
		return
	}

	cmds := strings.Split(string(rawCmds), "\r\n")
	size := len(cmds)
	// fmt.Println(size)

	rawParams, err := ioutil.ReadFile("params.json")
	if err != nil {
		fmt.Println("error", err)
		return
	}

	params := strings.Split(string(rawParams), ",")
	// size = len(params)
	// fmt.Println(params[0], params[size-1])

	obj := Constructor()
	var res bool
	var val int

	fmt.Println("starting ... ")

	for i := 0; i < size; i++ {
		cmd := strings.Trim(cmds[i], " \",")
		// fmt.Println("running", cmd)

		switch cmd {
		case "insert":
			val = parseParam(params[i-1])
			res = obj.Insert(val)

			if val == 3675 {
				fmt.Println("insert:", val, res)
			}

		case "remove":
			val = parseParam(params[i-1])
			res = obj.Remove(val)

			if val == 3675 {
				fmt.Println("remove:", val, res)
				fmt.Println(obj.dict[3675], obj.size)
			}
		}

		// fmt.Println(cmds[i], val, res)
	}
}

func parseParam(param string) int {
	arr := strings.Split(param, "\r\n")
	val, _ := strconv.Atoi(strings.Trim(arr[2], " "))
	return val
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
		// if idx < 0 {
		// 	return false
		// }

		pos = idx
	} else {
		return false
	}

	delete(this.dict, val)
	// this.dict[val] = -1

	if this.size > 1 {
		lastVal := this.store[this.size-1]

		if lastVal != val {
			this.store[pos] = lastVal
			this.dict[lastVal] = pos
		}
	}

	this.size--

	return true
}

/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
	pos := rand.Intn(this.size)
	return this.store[pos]
}
