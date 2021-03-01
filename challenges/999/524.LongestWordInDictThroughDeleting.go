package challenges

/**
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"

Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"

Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
*/

import "sort"

func findLongestWord(s string, d []string) string {
	dict := make([][]int, 26)
	for i := range dict {
		dict[i] = make([]int, 0, 100)
	}

	for i, ch := range s {
		idx := int(ch - 'a')
		dict[idx] = append(dict[idx], i)
	}

	// fmt.Println(dict)

	var l int
	var word string

	for _, w := range d {
		if verify(dict, w) && len(w) >= l {
			if len(w) > l || (len(w) == l && w < word) {
				l = len(w)
				word = w
			}
		}
	}

	return word
}

func verify(dict [][]int, w string) bool {
	pos := -1
	var size, idx int

	for _, ch := range w {
		idx = int(ch - 'a')
		size = len(dict[idx])

		if size == 0 || (pos >= 0 && dict[idx][size-1] < pos) {
			return false
		}

		if pos < 0 {
			pos = dict[idx][0]
			continue
		}

		next := sort.SearchInts(dict[idx], pos)
		if pos == dict[idx][next] {
			next++
		}

		if next < size && dict[idx][next] > pos {
			pos = dict[idx][next]
		} else {
			return false
		}
	}

	// fmt.Println("found:", w)

	return true
}
