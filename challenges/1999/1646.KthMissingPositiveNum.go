package challenges

/**
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
*/

func findKthPositive(arr []int, k int) int {
	if arr == nil || len(arr) == 0 || arr[0] > k {
		return k
	}

	if arr[0] > 1 {
		k -= arr[0] - 1
	}

	l := len(arr)
	missing := arr[l-1] - arr[0] + 1 - l

	if missing == 0 {
		return arr[l-1] + k
	}

	if missing < k {
		k -= missing
		return arr[l-1] + k
	}

	// fmt.Println("start:", k)

	for i := 1; i < l; i++ {
		if arr[i] == arr[i-1]+1 {
			continue
		}

		missing = arr[i] - arr[i-1] - 1

		// fmt.Println("iter:", arr[i], k, missing)

		if missing >= k {
			return arr[i-1] + k
		}

		k -= missing
	}

	return arr[l-1] + k
}
