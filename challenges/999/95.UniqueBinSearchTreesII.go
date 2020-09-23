package challenges

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func generateTrees(n int) []*TreeNode {
	return genTrees(1, n)
}

func genTrees(l, r int) []*TreeNode {
	if l == r {
		return []*TreeNode{&TreeNode{
			Val:   l,
			Left:  nil,
			Right: nil,
		}}
	}

	ans := make([]*TreeNode, 0, 1<<4)
	var left, right []*TreeNode

	for i := l; i <= r; i++ {
		if i > l {
			left = genTrees(l, i-1)
		} else {
			left = nil
		}

		if i < r {
			right = genTrees(i+1, r)
		} else {
			right = nil
		}

		if right != nil && len(right) > 0 {
			if left != nil && len(left) > 0 {
				for j := range left {
					for k := range right {
						ans = append(ans, &TreeNode{
							Val:   i,
							Left:  left[j],
							Right: right[k],
						})
					}
				}
			} else {
				for j := range right {
					ans = append(ans, &TreeNode{
						Val:   i,
						Left:  nil,
						Right: right[j],
					})
				}
			}
		} else if left != nil && len(left) > 0 {
			for j := range left {
				ans = append(ans, &TreeNode{
					Val:   i,
					Left:  left[j],
					Right: nil,
				})
			}
		}
	}

	return ans
}
