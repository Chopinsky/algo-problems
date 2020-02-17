package problems

import (
	"fmt"

	d "../../Utils"
)

// PPII ...
type PPII struct {
	source    string
	output    int
	testCount int
}

// CreatePPII ...
func CreatePPII() *PPII {
	return &PPII{}
}

// Build ...
func (p *PPII) Build(test int) {
	switch test {
	case 1:
		p.source = "null"
		p.output = 2

	case 2:
		p.source = "aabbaaccd"
		p.output = 2

	case 3:
		p.source = "aaabbaaccd"
		p.output = 3

	default:
		p.source = "aab"
		p.output = 1

	}

	p.testCount = 4
	p.ResetGlobals(len(p.source))
}

// Run ...
func (p *PPII) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcPPII(p.source), p.output)
			} else {
				calcPPII(p.source)
			}
		}
	}
}

var cache map[string]bool

// ResetGlobals ...
func (p *PPII) ResetGlobals(size int) {
	cache = make(map[string]bool, size*(size-1))
}

func calcPPII(src string) int {
	size := len(src)
	preprocess(src, size)

	dp := make([]int, size)
	dp[0] = 0

	for i := 1; i < size; i++ {
		if res, ok := cache[src[:i+1]]; res && ok {
			// the substring itself is a palindrome
			dp[i] = 0
			continue
		}

		// the substring is not a palindrome, try divide it
		dp[i] = 1 + dp[i-1]
		for j := 2; j <= i; j++ {
			if res, ok := cache[src[i-j+1:i+1]]; res && ok {
				dp[i] = d.Min(dp[i], dp[i-j]+1)
			}
		}
	}

	if !d.DEBUG {
		fmt.Println(dp)
	}

	return dp[size-1]
}

func preprocess(src string, size int) {
	for i := 0; i < size-1; i++ {
		for j := i + 1; j < size; j++ {
			isPalindrome(src[i:j+1], j+1-i)
		}
	}

	if d.DEBUG {
		fmt.Println(cache)
	}
}

func isPalindrome(tgt string, size int) bool {
	if size == 0 {
		return false
	} else if size == 1 {
		return true
	} else if size == 2 {
		cache[tgt] = tgt[0] == tgt[1]
		return tgt[0] == tgt[1]
	}

	if res, ok := cache[tgt]; ok {
		return res
	}

	start, end := (size-1)/2, size/2

	if size%2 == 1 {
		start--
		end++
	}

	for start >= 0 && end < size {
		if tgt[start] != tgt[end] {
			cache[tgt] = false
			return false
		}

		start--
		end++
	}

	cache[tgt] = true
	return true
}
