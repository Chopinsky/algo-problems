package main

import "testing"

// TestBinarySearch ...
func TestBinarySearch(t *testing.T) {
	var pos int

	pos = BinarySearch([]int{1}, 0, 0, 1)
	if pos != 1 {
		t.Errorf("bs([1], 1) = %d; want 1", pos)
	}

	pos = BinarySearch([]int{1}, 0, 0, 0)
	if pos != 0 {
		t.Errorf("bs([1], 1) = %d; want 0", pos)
	}

	pos = BinarySearch([]int{1, 2, 3, 4, 5}, 0, 4, 3)
	if pos != 3 {
		t.Errorf("bs([1, 2, 2, 4, 5], 3) = %d; want 3", pos)
	}

	pos = BinarySearch([]int{1, 2, 2, 4, 5}, 0, 4, 2)
	if pos != 3 {
		t.Errorf("bs([1, 2, 2, 4, 5], 2) = %d; want 3", pos)
	}

	pos = BinarySearch([]int{1, 3, 5, 7, 9, 11}, 0, 5, 10)
	if pos != 5 {
		t.Errorf("bs([1, 2, 2, 4, 5], 10) = %d; want 5", pos)
	}

	pos = BinarySearch([]int{1, 3, 3, 3, 3, 3}, 0, 5, 2)
	if pos != 1 {
		t.Errorf("bs([1, 3, 3, 3, 3, 3], 2) = %d; want 1", pos)
	}

	pos = BinarySearch([]int{1, 3, 3, 3, 3, 3, 4}, 0, 6, 3)
	if pos != 6 {
		t.Errorf("bs([1, 3, 3, 3, 3, 3, 4], 3) = %d; want 6", pos)
	}
}

func TestInsertSort(t *testing.T) {
	var a []int
	base1, lb1 := []int{1, 2, 3, 4, 5}, 5

	a = []int{2, 5, 1, 3, 4}
	InsertSort(a, 0, 4)
	verifyInsertSort(t, base1, a, lb1)

	a = []int{1, 2, 3, 4, 5}
	InsertSort(a, 0, 4)
	verifyInsertSort(t, base1, a, lb1)

	a = []int{5, 4, 3, 2, 1}
	InsertSort(a, 0, 4)
	verifyInsertSort(t, base1, a, lb1)

	a = []int{5, 3, 3, 3, 1}
	InsertSort(a, 0, 4)
	verifyInsertSort(t, []int{1, 3, 3, 3, 5}, a, lb1)

	a = []int{3, 3, 3, 3, 3}
	InsertSort(a, 0, 4)
	verifyInsertSort(t, []int{3, 3, 3, 3, 3}, a, lb1)
}

func verifyInsertSort(t *testing.T, base, target []int, size int) {
	for i := 0; i < size; i++ {
		if base[i] != target[i] {
			t.Error("want:", base, "; found:", target)
			break
		}
	}
}
