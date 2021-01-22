package challenges

/**
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Example 4:

Input: word1 = "cabbba", word2 = "aabbss"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any amount of operations.

Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
*/

func closeStrings(word1 string, word2 string) bool {
	if len(word1) != len(word2) {
		return false
	}

	c1, c2 := make([]int, 26), make([]int, 26)
	for i := range word1 {
		c1[int(word1[i]-'a')]++
		c2[int(word2[i]-'a')]++
	}

	for i := range c1 {
		if (c1[i] != 0 && c2[i] == 0) || (c1[i] == 0 && c2[i] != 0) {
			return false
		}
	}

	counts := make(map[int]int)
	for i := range c1 {
		counts[c1[i]]++
		counts[c2[i]]--
	}

	for _, val := range counts {
		if val != 0 {
			return false
		}
	}

	return true
}

func closeStrings1(word1 string, word2 string) bool {
	l1, l2 := len(word1), len(word2)
	if l1 != l2 {
		return false
	}

	m1 := make(map[byte]int, l1)
	m2 := make(map[byte]int, l2)
	c1 := make(map[int]int)
	c2 := make(map[int]int)

	for i := range word1 {
		m1[byte(word1[i])]++
		m2[byte(word2[i])]++
	}

	var orderOnly bool

	for k := range m1 {
		if m2[k] == 0 {
			return false
		}

		if m2[k] != m1[k] {
			orderOnly = false
		}

		c1[m1[k]]++
	}

	// only need to perform op1 to get word2
	if orderOnly {
		return true
	}

	for k := range m2 {
		if m1[k] == 0 {
			return false
		}

		c2[m2[k]]++
	}

	// fmt.Println(m1, m2)
	// fmt.Println(c1, c2)

	if len(c1) != len(c2) {
		return false
	}

	for k := range c1 {
		if c1[k] != c2[k] {
			return false
		}
	}

	return true
}
