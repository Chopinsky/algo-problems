package shared

import (
	// "fmt"
	"testing"
)

var a = []string{"c", "b", "a", "b", "a", "c"}
var b = []string{"a", "b", "c", "a", "b", "b", "a"}

func TestStrEdits(t *testing.T) {
	edits := StrEdits(a, b)

	if edits != 5 {
		t.Errorf("calculated edits: %d; want %d", edits, 5)
	}
}

func TestStrDiffs(t *testing.T) {
	edits := StrDiffs(a, b)

	if len(edits) != 9 {
		t.Errorf("calculated edits: %v; want %d", edits, 9)
	}
}
