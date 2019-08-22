package problems

import (
	"fmt"

	d "../../Utils"
)

// WSII ...
type WSII struct {
	source    [][]rune
	dict      []string
	output    []string
	testCount int
}

var root trieNode

// CreateWSII ...
func CreateWSII() *WSII {
	return &WSII{}
}

// Build ...
func (p *WSII) Build(test int) {
	p.testCount = 1

	switch test {
	default:
		p.source = [][]rune{
			{'o', 'a', 'a', 'n'},
			{'e', 't', 'a', 'e'},
			{'i', 'h', 'k', 'r'},
			{'i', 'f', 'l', 'v'},
		}

		p.dict = []string{"oath", "open", "pea", "eat", "rain"}
		p.output = []string{"eat", "oath"}

	}

	p.ResetGlobals(p.dict)
}

// ResetGlobals ...
func (p *WSII) ResetGlobals(dict []string) {
	root = trieNode{
		val:      0,
		children: make(map[rune]*trieNode),
		word:     "",
	}

	for i := range dict {
		root.insert(dict[i], dict[i])
	}

	if d.DEBUG {
		for i := range root.children {
			fmt.Println(string(root.children[i].val), len(root.children[i].children))
		}

		fmt.Println("oath ->", root.findWord("oath"))
		fmt.Println("orange ->", root.findWord("orange"))
		fmt.Println("oat ->", root.findWord("oat"))
	}

}

// Run ...
func (p *WSII) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")

				sizeX, sizeY := len(p.source), len(p.source[0])
				visited := make([][]bool, sizeX)

				for i := range visited {
					visited[i] = make([]bool, sizeY)
				}

				result := make(map[string]struct{}) //[]string{}

				for i := range p.source {
					for j := range p.source[i] {
						result = calcWSII(p.source, visited, i, j, sizeX, sizeY, result, &root)
					}
				}

				arr := make([]string, 0, len(result))
				for key := range result {
					arr = append(arr, key)
				}

				d.Output(arr, p.output)
			} else {
				sizeX, sizeY := len(p.source), len(p.source[0])
				visited := make([][]bool, sizeX)

				for i := range visited {
					visited[i] = make([]bool, sizeY)
				}

				result := make(map[string]struct{}) //[]string{}

				for i := range p.source {
					for j := range p.source[i] {
						result = calcWSII(p.source, visited, i, j, sizeX, sizeY, result, &root)
					}
				}
			}
		}
	}
}

func calcWSII(board [][]rune, visited [][]bool, x, y, sizeX, sizeY int, result map[string]struct{}, root *trieNode) map[string]struct{} {
	// we've found a word, add it to the final results
	if len(root.word) > 0 {
		// result = append(result, root.word)
		result[root.word] = empty
	}

	// update the visited board
	visited[x][y] = true

	// loop through all the unvisited neighbours
	for i := 0; i < 4; i++ {
		nextX, nextY := x+dir[i], y+dir[i+1]

		// illegal coord, continue
		if nextX < 0 || nextY < 0 || nextX >= sizeX || nextY >= sizeY {
			continue
		}

		// already visited, continue
		if visited[nextX][nextY] {
			continue
		}

		r := board[nextX][nextY]
		if next, ok := root.children[r]; ok {
			result = calcWSII(board, visited, nextX, nextY, sizeX, sizeY, result, next)
		}
	}

	// reset the visited board
	visited[x][y] = false

	return result
}

type trieNode struct {
	val      rune
	children map[rune]*trieNode
	word     string
}

func (t *trieNode) insert(word, src string) {
	if len(word) == 0 {
		t.word = src
		return
	}

	first, rest := rune(word[0]), word[1:]

	if child, ok := t.children[first]; ok {
		child.insert(rest, src)
	} else {
		node := &trieNode{
			val:      first,
			children: make(map[rune]*trieNode),
			word:     "",
		}

		t.children[first] = node
		node.insert(rest, src)
	}
}

func (t *trieNode) findWord(word string) string {
	if len(word) == 0 {
		return t.word
	}

	first, rest := rune(word[0]), word[1:]

	if child, ok := t.children[first]; ok {
		return child.findWord(rest)
	}

	return ""
}

func (t *trieNode) trace(r rune) *trieNode {
	if child, ok := t.children[r]; ok {
		return child
	}

	return nil
}
