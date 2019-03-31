package main

import (
	"bytes"
	"fmt"
)

// Debug ...
func Debug(text string, level int) {
	if !DEBUG {
		return
	}

	var buffer bytes.Buffer
	for i := 0; i < level; i++ {
		buffer.WriteString("  ")
	}

	fmt.Println("\n>> " + buffer.String() + text)
}
