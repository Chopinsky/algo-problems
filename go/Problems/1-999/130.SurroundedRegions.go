package problems

import (
	"fmt"

	d "../../Utils"
)

const (
	x = byte('X')
	o = byte('O')
	a = byte('A')
)

// SR ...
type SR struct {
	source    [][]byte
	output    [][]byte
	testCount int
}

// CreateSR ...
func CreateSR() *SR {
	return &SR{}
}

// Build ...
func (p *SR) Build(test int) {
	p.ResetGlobals()
	p.testCount = 1

	switch test {
	default:
		p.source = [][]byte{
			{x, x, x, x},
			{x, o, o, x},
			{x, x, o, x},
			{x, o, x, x},
		}
		p.output = [][]byte{
			{x, x, x, x},
			{x, x, x, x},
			{x, x, x, x},
			{x, o, x, x},
		}

	}
}

// ResetGlobals ...
func (p *SR) ResetGlobals() {
}

// Run ...
func (p *SR) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				// d.Output(calcSR(p.source), p.output)

				fmt.Println("Calculated result:")
				printBoard(calcSR(p.source))

				fmt.Println("Expected result:")
				printBoard(p.output)
			} else {
				calcSR(p.source)
			}
		}
	}
}

func printBoard(board [][]byte) {
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			fmt.Printf("%s, ", string(board[i][j]))
		}

		fmt.Println()
	}

	fmt.Println()
}

func calcSR(board [][]byte) [][]byte {
	row, col := len(board), len(board[0])
	if row <= 1 || col <= 1 {
		return board
	}

	size := row * col
	stack := make([][]int, 0, size)

	for j := 0; j < col; j++ {
		if board[0][j] == o {
			board[0][j] = a

			if board[1][j] == o {
				stack = append(stack, []int{1, j})
			}
		}

		if board[row-1][j] == o {
			board[row-1][j] = a

			if board[row-2][j] == o {
				stack = append(stack, []int{row - 2, j})
			}
		}
	}

	for i := 1; i < row-1; i++ {
		if board[i][0] == o {
			board[i][0] = a

			if board[i][1] == o {
				stack = append(stack, []int{i, 1})
			}
		}

		if board[i][col-1] == o {
			board[i][col-1] = a

			if board[i][col-2] == o {
				stack = append(stack, []int{i, col - 2})
			}
		}
	}

	var x0, y0, nx, ny int

	for len(stack) > 0 {
		x0, y0, stack = stack[0][0], stack[0][1], stack[1:]

		if board[x0][y0] == a {
			continue
		}

		board[x0][y0] = a

		for i := 0; i < 4; i++ {
			nx, ny = x0+d.Dirs[i], y0+d.Dirs[i+1]
			if board[nx][ny] == o {
				stack = append(stack, []int{nx, ny})
			}
		}
	}

	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			if board[i][j] == a {
				board[i][j] = o
			} else if board[i][j] == o {
				board[i][j] = x
			}
		}
	}

	return board
}
