package p0

import (
	"fmt"
	"strings"
	"time"

	s "go-problems/shared"
)

// ITEWProblems ...
type ITEWProblems struct {
	set []*ITEW
}

// Solve ...
func (p *ITEWProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= 0; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == 0 {
				s.Print(i, p.output, result)
			}
		}
	}

	fmt.Println("Algorithm finished in:", time.Since(start))
}

// ITEW ...
type ITEW struct {
	data   int
	output string
}

// CreateITEW ...
func CreateITEW() s.Problem {
	set := make([]*ITEW, 0, 4)

	set = append(set, &ITEW{
		data:   1234567891,
		output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One",
	})

	return &ITEWProblems{set}
}

func (p *ITEW) solve() string {
	return numberToWords(p.data)
}

func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}

	var base int
	var res, rem string

	for num > 0 {
		rem, num = strings.Trim(toNum(num%1000), " "), num/1000

		if base == 0 {
			res = rem
		} else if base == 1 && rem != "" {
			res = rem + " Thousand " + res
		} else if base == 2 && rem != "" {
			res = rem + " Million " + res
		} else if rem != "" {
			res = rem + " Billion " + res
		}

		base++
	}

	return strings.Trim(res, " ")
}

func toNum(n int) string {
	if n == 0 {
		return ""
	}

	var h, t, rem int
	base := ""

	h, rem = n/100, n%100

	if h > 0 {
		base += pronounce(h) + " Hundred"
	}

	if rem == 0 {
		return base
	}

	if rem <= 20 {
		base += " " + pronounce(rem)
	} else {
		t, rem = 10*(rem/10), rem%10
		base += " " + pronounce(t)

		if rem > 0 {
			base += " " + pronounce(rem)
		}
	}

	return base
}

func pronounce(n int) string {
	if n == 0 {
		return ""
	}

	switch n {
	case 1:
		return "One"

	case 2:
		return "Two"

	case 3:
		return "Three"

	case 4:
		return "Four"

	case 5:
		return "Five"

	case 6:
		return "Six"

	case 7:
		return "Seven"

	case 8:
		return "Eight"

	case 9:
		return "Nine"

	case 10:
		return "Ten"

	case 11:
		return "Eleven"

	case 12:
		return "Twelve"

	case 13:
		return "Thirteen"

	case 14:
		return "Fourteen"

	case 15:
		return "Fifteen"

	case 16:
		return "Sixteen"

	case 17:
		return "Seventeen"

	case 18:
		return "Eighteen"

	case 19:
		return "Nineteen"

	case 20:
		return "Twenty"

	case 30:
		return "Thirty"

	case 40:
		return "Forty"

	case 50:
		return "Fifty"

	case 60:
		return "Sixty"

	case 70:
		return "Seventy"

	case 80:
		return "Eighty"

	case 90:
		return "Ninety"
	}

	return ""
}
