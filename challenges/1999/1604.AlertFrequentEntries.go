package challenges

import (
	"sort"
	"strings"
)

/**
LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.

You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.

Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.

Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period.


Example 1:

Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
Output: ["daniel"]
Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").

Example 2:

Input: keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
Output: ["bob"]
Explanation: "bob" used the keycard 3 times in a one-hour period ("21:00","21:20", "21:30").

Example 3:

Input: keyName = ["john","john","john"], keyTime = ["23:58","23:59","00:01"]
Output: []

Example 4:

Input: keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"], keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
Output: ["clare","leslie"]

*/

func alertNames(keyName []string, keyTime []string) []string {
	store := make(map[string][]int)

	for i, name := range keyName {
		if arr, ok := store[name]; ok {
			arr = append(arr, parseTime(keyTime[i]))
			store[name] = arr
		} else {
			store[name] = []int{parseTime(keyTime[i])}
		}
	}

	ans := make([]string, 0, len(store))
	for name, times := range store {
		sort.Ints(times)

		// fmt.Println(name, times)

		for i := 2; i < len(times); i++ {
			if times[i]-times[i-2] <= 60 {
				ans = append(ans, name)
				// fmt.Println(name, times[i])
				break
			}
		}
	}

	sort.Strings(ans)

	return ans
}

func parseTime(t string) int {
	time := strings.SplitN(t, ":", 2)
	return parseDigits(time[0])*60 + parseDigits(time[1])
}

func parseDigits(t string) int {
	var time int
	for _, char := range t {
		time = time*10 + int(char-'0')
	}

	return time
}
