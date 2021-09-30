package challenges

/**
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.

Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Example 4:

Input: arr = [6,1,9]
Output: 2

Example 5:

Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3

Constraints:

1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8
*/

func minJumps(arr []int) int {
	if len(arr) <= 1 {
		return 0
	}

	l := len(arr)
	links := make(map[int][]int, l)

	for i, val := range arr {
		links[val] = append(links[val], i)
	}

	// fmt.Println(links)

	steps := 0
	visited := make([]bool, l)
	stack := make([]int, 0, l)
	tmp := make([]int, 0, l)

	stack = append(stack, 0)

	for len(stack) > 0 {
		// fmt.Println(steps, stack, visited)

		for _, idx := range stack {
			visited[idx] = true
			// fmt.Println("inside:", steps, idx)

			if idx+1 == l-1 {
				return steps + 1
			}

			if idx-1 > 0 && !visited[idx-1] {
				tmp = append(tmp, idx-1)
				visited[idx-1] = true
			}

			if idx+1 < l && !visited[idx+1] {
				tmp = append(tmp, idx+1)
				visited[idx+1] = true
			}

			if next, ok := links[arr[idx]]; ok && len(next) > 0 {
				for _, nidx := range next {
					if nidx == l-1 {
						return steps + 1
					}

					if !visited[nidx] {
						tmp = append(tmp, nidx)
						visited[nidx] = true
					}
				}

				delete(links, arr[idx])
			}
		}

		// fmt.Println("after:", tmp)

		stack, tmp = tmp, stack
		tmp = tmp[:0]
		steps++
	}

	return steps
}
