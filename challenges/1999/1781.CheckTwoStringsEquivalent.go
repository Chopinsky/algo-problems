package challenges

/**
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.
*/

func arrayStringsAreEqual(word1 []string, word2 []string) bool {
	var j, jj int
	l1, l2 := len(word1), len(word2)
	if (l1 == 0 && l2 > 0) || (l1 > 0 && l2 == 0) {
		return false
	}

	ll1, ll2 := len(word1[l1-1]), len(word2[l2-1])

	for i, w := range word1 {
		for ii, c := range w {
			// fmt.Println("pos:", i, ii, j, jj)

			if byte(c) != word2[j][jj] {
				// fmt.Println("diff", w, string(c), word2[j], string(word2[j][jj]))
				return false
			}

			if i == l1-1 && ii == ll1-1 {
				break
			}

			jj++

			if jj >= len(word2[j]) {
				j++
				jj = 0
			}

			if j >= l2 {
				// fmt.Println("more", w, string(c))
				return false
			}
		}
	}

	return j == l2-1 && jj == ll2-1
}
