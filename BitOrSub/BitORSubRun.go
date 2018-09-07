package bitorsub

import (
	"fmt"
)

// Run ...
func Run(test int, debug bool) {
	var num uint
	var res []uint

	switch test {
	case 2:
		//num, res = runDP2d([]uint{1, 1, 2})
		num, res = runDP1d([]uint{1, 1, 2})
	case 3:
		//num, res = runDP2d([]uint{1, 2, 4})
		num, res = runDP1d([]uint{1, 2, 4})
	case 4:
		//num, res = runDP2d([]uint{1, 2, 4})
		num, res = runDP1d([]uint{1, 2, 3, 4, 5})
	default:
		//num, res = runDP2d([]uint{1})
		num, res = runDP1d([]uint{1})
	}

	fmt.Println("- Number of possible unique outputs: ", num)
	fmt.Println("- All possible unique outputs: ", res)
}
