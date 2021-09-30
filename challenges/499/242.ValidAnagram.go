package challenges

/**
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
*/

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	chars := make([]int, 26)
	for i, c := range s {
		chars[int(c-'a')]++
		chars[int(t[i]-'a')]--
	}

	for _, val := range chars {
		if val != 0 {
			return false
		}
	}

	return true
}
