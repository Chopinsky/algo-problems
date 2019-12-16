package problems

import (
	"fmt"
	"strconv"
)

var dir = []int{-1, 0, 1, 0, -1}
var empty = struct{}{}

func printBinary(val, count int) {
	format := "%0" + strconv.Itoa(count) + "b\n"
	fmt.Printf(format, val)
}
