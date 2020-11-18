package challenges

// MountainArray ...
type MountainArray struct {
	vals []int
}

func (t *MountainArray) get(index int) int {
	return t.vals[index]
}

func (t *MountainArray) length() int {
	return len(t.vals)
}

/**
You may recall that an array A is a mountain array if and only if:

A.length >= 3, there exists some i with 0 < i < A.length - 1 such that:

A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.

Submissions making more than 100 calls to MountainArray.get will be judged *Wrong Answer*. Also, any solutions that attempt to circumvent the judge will result in disqualification.

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.

*/

func findInMountainArray(target int, m *MountainArray) int {
	size := m.length()
	l, r := 0, size

	if size == 3 {
		if m.get(0) == target {
			return 0
		}

		if m.get(1) == target {
			return 1
		}

		if m.get(2) == target {
			return 2
		}

		return -1
	}

	if target < m.get(0) && target < m.get(size-1) {
		return -1
	}

	peak := -1
	for l < r {
		mid := (l + r) / 2
		if mid == 0 {
			peak = 1
			break
		}

		if mid == size-1 {
			peak = size - 2
			break
		}

		vl, v, vr := m.get(mid-1), m.get(mid), m.get(mid+1)
		if vl < v && v < vr {
			l = mid + 1
		} else if vl > v && v > vr {
			r = mid - 1
		} else {
			peak = mid
			break
		}

		// fmt.Println(mid, l, r, vl, v, vr)
	}

	if peak < 0 {
		peak = l
	}

	// fmt.Println(peak)

	if target > m.get(peak) {
		return -1
	}

	idx := find(target, peak, size, true, m)
	if idx >= 0 {
		return idx
	}

	idx = find(target, peak, size, false, m)
	return idx
}

func find(t, peak, size int, isLeft bool, m *MountainArray) int {
	var l, r int

	if isLeft {
		l, r = 0, peak+1
	} else {
		l, r = peak, size
	}

	for l < r {
		mid := (l + r) / 2
		val := m.get(mid)

		if val == t {
			return mid
		}

		if val < t {
			if isLeft {
				l = mid + 1
			} else {
				r = mid - 1
			}
		} else {
			if isLeft {
				r = mid - 1
			} else {
				l = mid + 1
			}
		}
	}

	if m.get(l) == t {
		return l
	}

	return -1
}
