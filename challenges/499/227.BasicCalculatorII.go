package challenges

func calculate(s string) int {
	nums := make([]int, 0, len(s)/2)
	ops := make([]byte, 0, len(s)/2)

	var num, lastOp, lastNum int

	for i := 0; i < len(s); i++ {
		char := s[i]

		if char == ' ' {
			continue
		}

		if char == '+' || char == '-' || char == '*' || char == '/' {
			ops = append(ops, char)
			continue
		}

		num, i = parse(s, i)

		lastOp = len(ops) - 1
		lastNum = len(nums) - 1

		if lastNum >= 0 && lastOp >= 0 && (ops[lastOp] == '*' || ops[lastOp] == '/') {
			if ops[lastOp] == '*' {
				nums[lastNum] *= num
			} else {
				nums[lastNum] /= num
			}

			ops = ops[:lastOp]
		} else {
			nums = append(nums, num)
		}
	}

	// fmt.Println(nums, ops)

	ans := nums[0]

	for i, op := range ops {
		if op == '+' {
			ans += nums[i+1]
		} else {
			ans -= nums[i+1]
		}
	}

	return ans
}

func parse(s string, idx int) (int, int) {
	var num int

	for idx < len(s) {
		char := s[idx]

		if char < '0' || char > '9' {
			idx--
			break
		}

		num = num*10 + int(char-'0')
		idx++
	}

	return num, idx
}
