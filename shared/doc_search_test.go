package shared

import (
	// "fmt"
	"testing"
)

var src = "Eleven journalists and media workers have been killed so far in 2020 in Afghanistan. Five in the past two months alone."

func TestSearchDoc0(t *testing.T) {
	s := SearchKeywords(src, "media have so")
	t.Errorf("calculated edits: '%s'; want: '%s'", s, "media workers have been killed so")
}
