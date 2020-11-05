package challenges

import "fmt"

func monotoneIncreasingDigits(n int) int {
	if n < 10 {
		return n
	}

	d := make([]int, 0, 9)
	des := false
	src := n

	for n > 0 {
		if !des && len(d) > 0 && (n%10 > d[len(d)-1]) {
			des = true
		}

		d = append(d, n%10)
		n /= 10
	}

	if !des {
		return src
	}

	fmt.Println(d)

	//todo: greed, if 0, starts from 9 and set borrow = true, then reset if conditions are met

	borrow := false
	base := make([]int, 0, len(d))

	for i, val := range d {
		fmt.Println(i, val, base, borrow)

		if val == 0 || (borrow && val == 1) {
			flipNines(base)

			base = append(base, 9)
			borrow = true

			continue
		}

		if i == 0 {
			base = append(base, val)
			continue
		}

		if borrow {
			val--
			borrow = false
		}

		if val > base[i-1] {
			flipNines(base)
			val--

			// fmt.Println("post flip:", base, val)

			base = append(base, val)
			borrow = false

			continue
		}

		base = append(base, val)
		borrow = false

		// todo: more checks and flips
	}

	if borrow {
		base = base[:len(base)-1]
	}

	ans := 0
	for j := len(base) - 1; j >= 0; j-- {
		ans = ans*10 + base[j]
	}

	return ans
}

func flipNines(src []int) {
	for i := len(src) - 1; i >= 0; i-- {
		if src[i] == 9 {
			break
		}

		src[i] = 9
	}
}
