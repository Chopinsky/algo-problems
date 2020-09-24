package challenges

import "fmt"

func runMEII() {
	fmt.Println(majorityElement([]int{4, 2, 1, 1}))
	fmt.Println(majorityElement([]int{1, 1, 1, 3, 3, 2, 2, 2}))
}

func majorityElement(nums []int) []int {
	var c1, c2, n1, n2 int
	var v1, v2 bool

	for _, val := range nums {
		if (!v1 || c1 == 0) && (!v2 || val != n2) {
			n1 = val
			v1 = true
		} else if (!v2 || c2 == 0) && (!v1 || val != n1) {
			n2 = val
			v2 = true
		}

		if val == n1 {
			c1++
		} else if val == n2 {
			c2++
		} else {
			c1--
			c2--
		}

		// fmt.Println("walking", n1, c1, n2, c2)
	}

	// fmt.Println("final", n1, c1, n2, c2)

	c1, c2 = 0, 0
	for _, val := range nums {
		if val == n1 {
			c1++
		}

		if val == n2 && v2 {
			c2++
		}
	}

	ans := make([]int, 0, 2)
	if c1 > len(nums)/3 {
		ans = append(ans, n1)
	}

	if c2 > len(nums)/3 {
		ans = append(ans, n2)
	}

	return ans
}
