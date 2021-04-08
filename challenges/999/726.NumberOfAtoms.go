package challenges

import (
	"sort"
	"strconv"
)

func countOfAtoms(formula string) string {
	_, m := countPart(formula)
	store := make([][]string, 0, len(m))

	// fmt.Println(m)

	var cstr string
	for k, c := range m {
		if c == 1 {
			cstr = ""
		} else {
			cstr = strconv.Itoa(c)
		}

		store = append(store, []string{k, cstr})
	}

	sort.Slice(store, func(i, j int) bool {
		return store[i][0] < store[j][0]
	})

	// fmt.Println(store)

	ans := ""
	for _, k := range store {
		ans += k[0] + k[1]
	}

	return ans
}

type a struct {
	atom  string
	count int
}

func countPart(f string) (int, map[string]int) {
	counts := make(map[string]int)

	var next map[string]int
	var num, shift int
	var atom string

	for i := 0; i < len(f); i++ {
		ch := f[i]

		if ch == '(' {
			if update(counts, next, atom, num) {
				next = nil
				atom = ""
				num = 0
			}

			shift, next = countPart(f[i+1:])
			i += shift + 1
		} else if ch == ')' {
			if update(counts, next, atom, num) {
				next = nil
				atom = ""
				num = 0
			}

			return i, counts
		} else if ch >= 'A' && ch <= 'Z' {
			if update(counts, next, atom, num) {
				next = nil
				atom = ""
				num = 0
			}

			atom = string(ch)
		} else if ch >= 'a' && ch <= 'z' {
			atom += string(ch)
		} else {
			// if num > 0 && update(counts, next, atom, num) {
			//   next = nil
			//   atom = ""
			//   num = 0
			// }

			num = num*10 + int(ch-'0')
		}
	}

	if update(counts, next, atom, num) {
		next = nil
		atom = ""
		num = 0
	}

	// fmt.Println("return:", f, counts)

	return len(f) - 1, counts
}

func update(counts, next map[string]int, atom string, num int) bool {
	// fmt.Println("merging:", next, atom, num)

	if num >= 0 && len(atom) > 0 {
		if num > 0 {
			counts[atom] += num
		} else {
			counts[atom]++
		}

		// fmt.Println("merging:", counts, next, atom, num)

		return true
	} else if num >= 0 && next != nil {
		for a, c := range next {
			if num > 0 {
				counts[a] += num * c
			} else {
				counts[a] += c
			}
		}

		// fmt.Println("merging:", counts, next, atom, num)

		return true
	}

	return false
}
