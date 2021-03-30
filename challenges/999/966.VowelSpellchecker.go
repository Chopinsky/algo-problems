package challenges

/**
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

Example 1:

Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

Note:

1 <= wordlist.length <= 5000
1 <= queries.length <= 5000
1 <= wordlist[i].length <= 7
1 <= queries[i].length <= 7
All strings in wordlist and queries consist only of english letters.
*/

import "strings"

func spellchecker(wordlist []string, queries []string) []string {
	original := make(map[string]string)
	capitalization := make(map[string]string)
	vowels := make(map[string]string)

	for _, w := range wordlist {
		original[w] = w

		next := strings.ToLower(w)
		if _, ok := capitalization[next]; !ok {
			capitalization[next] = w
		}

		next = repl(next)
		if _, ok := vowels[next]; !ok {
			vowels[next] = w
		}
	}

	// fmt.Println(original, capitalization, vowels)

	ans := make([]string, len(queries))
	for i, w := range queries {
		if w0, ok := original[w]; ok {
			ans[i] = w0
			continue
		}

		next := strings.ToLower(w)
		if w0, ok := capitalization[next]; ok {
			ans[i] = w0
			continue
		}

		next = repl(next)
		if w0, ok := vowels[next]; ok {
			ans[i] = w0
			continue
		}

		ans[i] = ""
	}

	return ans
}

func repl(w string) string {
	b := []byte(w)

	for i, c := range b {
		if c == byte('a') || c == byte('e') || c == byte('i') || c == byte('o') || c == byte('u') {
			b[i] = byte('*')
		}
	}

	return string(b)
}

func spellchecker1(wordlist []string, queries []string) []string {
	root := &ctrie{
		word:     "",
		priority: -1,
		children: make([]*ctrie, 52),
	}

	for i, w := range wordlist {
		root.insert(w, 0, i)
	}

	ans := make([]string, 0, len(queries))

	for _, w := range queries {
		a, _ := root.find(w, 0)
		ans = append(ans, a)
	}

	return ans
}

var vowels = []int{0, 4, 8, 14, 20, 26, 30, 34, 40, 46}

type ctrie struct {
	word     string
	priority int
	children []*ctrie
}

func (t *ctrie) insert(word string, idx, priority int) {
	if idx >= len(word) {
		return
	}

	var pos int
	if word[idx] >= 'a' && word[idx] <= 'z' {
		pos = int(word[idx]-'a') + 26
	} else {
		pos = int(word[idx] - 'A')
	}

	if t.children[pos] == nil {
		t.children[pos] = &ctrie{
			word:     "",
			priority: -1,
			children: make([]*ctrie, 52),
		}
	}

	if idx < len(word)-1 {
		t.children[pos].insert(word, idx+1, priority)
	} else {
		t.children[pos].word = word

		if t.children[pos].priority < 0 {
			t.children[pos].priority = priority
		}
	}
}

func (t *ctrie) find(word string, idx int) (string, int) {
	if idx >= len(word) {
		return t.word, t.priority
	}

	var pos, alt int
	var ans string
	priority := -1

	if word[idx] >= 'a' && word[idx] <= 'z' {
		pos = int(word[idx]-'a') + 26
		alt = pos - 26
	} else {
		pos = int(word[idx] - 'A')
		alt = pos + 26
	}

	if t.children[pos] != nil {
		a, p := t.children[pos].find(word, idx+1)
		if p >= 0 {
			priority = p
			ans = a
		}

		if a == word {
			return a, 0
		}
	}

	// switch case
	if t.children[alt] != nil {
		a, p := t.children[alt].find(word, idx+1)
		if p >= 0 && (priority < 0 || p < priority) {
			priority = p
			ans = a
		}
	}

	// switch vowels
	if isVowel(word, idx) {
		for _, pos := range vowels {
			if t.children[pos] == nil {
				continue
			}

			a, p := t.children[pos].find(word, idx+1)
			if p >= 0 && (priority < 0 || p < priority) {
				priority = p
				ans = a
			}
		}
	}

	return ans, priority
}

func isVowel(word string, idx int) bool {
	return word[idx] == 'a' || word[idx] == 'e' || word[idx] == 'i' || word[idx] == 'o' || word[idx] == 'u' || word[idx] == 'A' || word[idx] == 'E' || word[idx] == 'I' || word[idx] == 'O' || word[idx] == 'U'
}
