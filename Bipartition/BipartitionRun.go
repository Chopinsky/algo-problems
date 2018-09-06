package bipartition

import (
	"fmt"
)

// Run ...
func Run(test int, debug bool) {
	switch test {
	case 1:
		BuildGraph(4, [][]int{{1, 2}, {1, 3}, {2, 4}})
	case 2:
		BuildGraph(3, [][]int{{1, 2}, {1, 3}, {2, 3}})
	case 3:
		BuildGraph(5, [][]int{{1, 2}, {2, 3}, {3, 4}, {4, 5}, {1, 5}})
	default:
		fmt.Println("\nTest case not specified: ", test)
		return
	}

	ok, res := Search()

	fmt.Println("\nResult:", ok, res)
}
