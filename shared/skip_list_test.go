package shared

import (
	// "fmt"
	"testing"
)

var test1 = []int{1, 4, 5, 7, 9, 12}

func TestSkipList(t *testing.T) {
	s := MakeSkipList(test1)

	if !s.Search(1) {
		t.Errorf("should find 1")
	}

	if s.Search(2) {
		t.Errorf("should not find 2")
	}
}
