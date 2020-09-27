package challenges

import (
	"sort"
	"strconv"
)

func largestNumber(nums []int) string {
	size := len(nums)
	if size == 0 {
		return ""
	}

	if size == 1 {
		return strconv.Itoa(nums[0])
	}

	nstr := make([]string, size)
	for i, val := range nums {
		nstr[i] = strconv.Itoa(val)
	}

	sort.Slice(nstr, func(i, j int) bool {
		si, sj := nstr[i]+nstr[j], nstr[j]+nstr[i]
		if si == sj {
			if len(nstr[i]) <= len(nstr[j]) {
				return true
			}

			return false
		}

		if si > sj {
			return true
		}

		return false
	})

	// fmt.Println(nstr)

	ans := ""
	for _, s := range nstr {
		ans += s
	}

	if ans[0] == '0' {
		return "0"
	}

	return ans
}
