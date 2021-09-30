package challenges

import (
	"strconv"
	"strings"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// Codec ...
type Codec struct{}

// CodecConstructor ...
func CodecConstructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string.
func (t *Codec) serialize(root *TreeNode) string {
	res := ser(root)
	return res
}

func ser(root *TreeNode) string {
	if root == nil {
		return ""
	}

	base := strconv.Itoa(root.Val) + ","

	if root.Left != nil {
		base += ser(root.Left)
	}

	if root.Right != nil {
		base += ser(root.Right)
	}

	return base
}

// Deserializes your encoded data to tree.
func (t *Codec) deserialize(data string) *TreeNode {
	src := strings.Split(strings.Trim(data, ","), ",")
	if len(src) == 0 {
		return nil
	}

	// fmt.Println(src, len(src))

	vals := make([]int, 0, len(src))
	for _, v := range src {
		if v == "" {
			continue
		}

		num, _ := strconv.Atoi(v)
		vals = append(vals, num)
	}

	// fmt.Println(vals)

	return der(vals)
}

func der(vals []int) *TreeNode {
	size := len(vals)
	if size == 0 {
		return nil
	}

	root := &TreeNode{
		Val:   vals[0],
		Left:  nil,
		Right: nil,
	}

	if size == 1 {
		return root
	}

	base := vals[0]
	if vals[1] > base {
		root.Right = der(vals[1:])
		return root
	}

	if vals[size-1] < base {
		root.Left = der(vals[1:])
		return root
	}

	l, r := 1, size

	for l < r {
		m := (l + r) / 2
		if vals[m] > base {
			r = m - 1
		} else {
			l = m + 1
		}
	}

	if vals[l] > base {
		l--
	}

	root.Left = der(vals[1 : l+1])
	root.Right = der(vals[l+1:])

	return root
}

/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor()
 * deser := Constructor()
 * tree := ser.serialize(root)
 * ans := deser.deserialize(tree)
 * return ans
 */
