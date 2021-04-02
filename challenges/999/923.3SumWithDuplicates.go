package challenges

import (
	"fmt"
	"sort"
)

/**
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.


Constraints:

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300
*/

func threeSumMulti(arr []int, target int) int {
	freq := make(map[int]int)
	nums := make([]int, 0, len(arr))

	sort.Ints(arr)
	var total int

	for _, val := range arr {
		if val > target {
			break
		}

		freq[val]++
		if freq[val] == 1 {
			nums = append(nums, val)
		}
	}

	for i, vi := range nums {
		if 3*vi < target {
			continue
		}

		if 3*vi == target {
			cnt := freq[vi]
			total += cnt * (cnt - 1) * (cnt - 2) / 6
			continue
		}

		for j := 0; j <= i; j++ {
			vj := nums[j]
			vk := target - vi - vj

			if vk < 0 {
				break
			}

			if vk > vj {
				continue
			}

			fi, fj, fk := freq[vi], freq[vj], freq[vk]

			if vj == vi {
				total += (fi * (fi - 1) / 2) * fk
			} else if vj == vk {
				total += fi * (fj * (fj - 1) / 2)
			} else {
				total += fi * fj * fk
			}

			// fmt.Println(vk, vj, vi, total)
		}
	}

	return total % 1000000007
}

func threeSumMulti1(arr []int, target int) int {
	count := make(map[int][]int)

	var total int
	sort.Ints(arr)

	for i, val := range arr {
		if val > target {
			break
		}

		if _, ok := count[val]; !ok {
			count[val] = []int{i, 1}
		} else {
			count[val][1]++
		}
	}

	fmt.Println(count, len(arr))

	for i := 2; i < len(arr); i++ {
		v2 := arr[i]
		if 3*v2 < target {
			continue
		}

		for j := 1; j < i; j++ {
			v1 := arr[j]
			v0 := target - v2 - v1

			if v0 < 0 {
				break
			}

			if v0 > v1 || count[v0] == nil {
				continue
			}

			if v0 != v1 {
				total += count[v0][1]
			} else {
				total += j - count[v0][0]
			}
		}
	}

	return total % 1000000007
}
