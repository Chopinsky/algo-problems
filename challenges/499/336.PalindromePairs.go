package challenges

/**
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
*/

func palindromePairs(words []string) [][]int {
	root := &trie{
		word: "",
		next: make([]*trie, 26),
	}

	dict := make(map[string]int)
	blankIdx := -1

	for i, w := range words {
		if len(w) > 0 {
			root.insert(w, w)
		} else {
			blankIdx = i
		}

		dict[w] = i
	}

	// fmt.Println(dict)

	ans := make([][]int, 0, len(words))
	for i, w := range words {
		pairs := root.find(w, w, []string{})

		// fmt.Println(w, pairs)

		for _, next := range pairs {
			if next != w {
				ans = append(ans, []int{i, dict[next]})
			}
		}

		if blankIdx >= 0 && i != blankIdx && isPalidrome(w) {
			ans = append(ans, []int{i, blankIdx})
		}
	}

	return ans
}

type trie struct {
	word string
	next []*trie
}

func (t *trie) insert(word, src string) {
	l := len(word) - 1
	if l < 0 {
		t.word = src
		return
	}

	ch := int(word[l] - 'a')
	if t.next[ch] == nil {
		t.next[ch] = &trie{
			word: "",
			next: make([]*trie, 26),
		}
	}

	t.next[ch].insert(word[:l], src)
}

func (t *trie) find(word, src string, ans []string) []string {
	l := len(word) - 1

	if l < 0 {
		ans = t.gather(len(src), ans)
		return ans
	}

	if len(t.word) > 0 && isPalidrome(word) {
		ans = append(ans, t.word)
	}

	ch := int(word[0] - 'a')
	if t.next[ch] != nil {
		ans = t.next[ch].find(word[1:], src, ans)
	}

	return ans
}

func (t *trie) gather(l int, ans []string) []string {
	if len(t.word) > 0 {
		check := t.word[:len(t.word)-l]

		if isPalidrome(check) {
			ans = append(ans, t.word)
		}
	}

	for _, next := range t.next {
		if next == nil {
			continue
		}

		ans = next.gather(l, ans)
	}

	return ans
}

func isPalidrome(word string) bool {
	size := len(word)
	if size <= 1 {
		return true
	}

	for i := 0; i < size/2; i++ {
		if word[i] != word[size-1-i] {
			return false
		}
	}

	return true
}
