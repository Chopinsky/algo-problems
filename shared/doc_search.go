package shared

import (
	// "fmt"
	"strings"
)

// SearchKeywords ...
func SearchKeywords(doc string, keywords string) string {
	wordIdx := make(map[string][]int)
	for _, w := range strings.Split(keywords, " ") {
		wordIdx[w] = make([]int, 0, 16)
	}

	docWords := strings.Split(doc, " ,.")
	for i, w := range docWords {
		if len(w) == 0 {
			continue
		}

		if _, ok := wordIdx[w]; ok {
			wordIdx[w] = append(wordIdx[w], i)
		}
	}

	count := -1
	rareKeyword := ""
	var rareKeywordIdx []int

	for k, v := range wordIdx {
		// keyword is not found in the source document
		if len(v) == 0 {
			return ""
		}

		// get the rarest keyword as the search base
		if count < 0 || len(v) < count {
			count = len(v)
			rareKeyword = k
			rareKeywordIdx = v
		}
	}

	delete(wordIdx, rareKeyword)
	segStart, segEnd := -1, -1

	for _, idx := range rareKeywordIdx {
		start, end := findRange(wordIdx, idx)
		if start < 0 || end < 0 || end < start {
			continue
		}

		if segStart < 0 || (end-start) < (segEnd-segStart) {
			segStart, segEnd = start, end
		}
	}

	ans := ""
	if segStart < 0 || segEnd < 0 {
		return ans
	}

	for i := segStart; i <= segEnd; i++ {
		ans += docWords[i]
	}

	return ans
}

func findRange(src map[string][]int, idx int) (int, int) {
	// seen := make(map[int]bool)

	return 0, 0
}
