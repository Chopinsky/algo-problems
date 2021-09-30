package challenges

/**
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
*/

func numPairsDivisibleBy60(time []int) int {
	mod := make(map[int]int)
	count := 0

	for _, val := range time {
		mod[val%60]++
	}

	if mod[0] > 0 {
		count += mod[0] * (mod[0] - 1) / 2
	}

	if mod[30] > 0 {
		count += mod[30] * (mod[30] - 1) / 2
	}

	for i := 1; i < 30; i++ {
		count += mod[i] * mod[60-i]
	}

	return count
}

func numPairsDivisibleBy601(time []int) int {
	mods := make(map[int]int)
	count := 0

	for _, val := range time {
		rem := val % 60

		for r, c := range mods {
			if (rem+r)%60 == 0 {
				count += c
			}
		}

		mods[rem]++
	}

	return count
}
