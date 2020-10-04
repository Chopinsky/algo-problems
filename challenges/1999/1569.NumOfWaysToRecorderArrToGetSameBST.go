package challenges

import "fmt"

var mod = int64(1000000007)

func numOfWays(nums []int) int {
	if len(nums) <= 2 {
		return 0
	}

	root := &nodeBST{
		val:   nums[0],
		count: 1,
		left:  nil,
		right: nil,
	}

	for i := 1; i < len(nums); i++ {
		root.insert(nums[i])
	}

	c := make([][]int64, len(nums))
	for i := range c {
		c[i] = make([]int64, len(nums))
		c[i][0] = 1
		c[i][1] = int64(i)
	}

	// minus 1 of the order from `nums`
	ans := root.calc(c) - 1
	fmt.Println(ans)

	return int(ans)
}

type nodeBST struct {
	val   int
	count int
	left  *nodeBST
	right *nodeBST
}

func (n *nodeBST) insert(val int) {
	n.count++

	if val < n.val {
		if n.left != nil {
			n.left.insert(val)
		} else {
			n.left = &nodeBST{
				val:   val,
				count: 1,
				left:  nil,
				right: nil,
			}
		}

		return
	}

	if n.right != nil {
		n.right.insert(val)
	} else {
		n.right = &nodeBST{
			val:   val,
			count: 1,
			left:  nil,
			right: nil,
		}
	}
}

func (n *nodeBST) calc(c [][]int64) int64 {
	if n.left == nil && n.right == nil {
		return 1
	}

	l, r := int64(1), int64(1)

	if n.left != nil {
		l = n.left.calc(c)

		if n.right == nil {
			return l
		}
	}

	if n.right != nil {
		r = n.right.calc(c)

		if n.left == nil {
			return r
		}
	}

	// fmt.Println(n.val, l, r, n.count-1, combo(c, n.count-1, n.left.count))
	// fmt.Println(n.val, n.count, n.left.count, n.right.count)

	ans := combo(c, n.count-1, n.left.count)
	ans = (ans * l) % mod
	ans = (ans * r) % mod

	return ans
}

func combo(c [][]int64, n, k int) int64 {
	if k == 0 || n == 0 || n == k {
		return 1
	}

	if k == 1 {
		return int64(n)
	}

	if n-k < k {
		k = n - k
	}

	if c[n][k] > 0 {
		return c[n][k]
	}

	// method 1: not going to work on large n, because of the divisions
	// c[n][k] = (combo(c, n-1, k-1) / int64(k) * int64(n)) % mod

	// method 2:
	c[n][k] = (combo(c, n-1, k) + combo(c, n-1, k-1)) % mod

	return c[n][k]
}

func run() {
	fmt.Println(numOfWays([]int{9, 4, 2, 1, 3, 6, 5, 7, 8, 14, 11, 10, 12, 13, 16, 15, 17, 18}))
}
