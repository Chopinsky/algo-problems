package challenges

/**
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

Example 1:

Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// BSTIterator ...
type BSTIterator struct {
	root  *TreeNode
	stack []*TreeNode
}

// BSTConstructor ...
func BSTConstructor(root *TreeNode) BSTIterator {
	return BSTIterator{
		root:  root,
		stack: push(root, []*TreeNode{}),
	}
}

// Next ...
func (t *BSTIterator) Next() int {
	last := len(t.stack) - 1
	node := t.stack[last]

	t.stack = t.stack[:last]
	last--

	if node.Right != nil {
		t.stack = push(node.Right, t.stack)
	}

	return node.Val
}

// HasNext ...
func (t *BSTIterator) HasNext() bool {
	return len(t.stack) > 0
}

func push(root *TreeNode, stack []*TreeNode) []*TreeNode {
	if root == nil {
		return stack
	}

	stack = append(stack, root)

	if root.Left != nil {
		stack = push(root.Left, stack)
	}

	return stack
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
