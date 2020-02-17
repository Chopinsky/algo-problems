package utils

import (
	"bytes"
	"fmt"
)

// DEBUG ...
var DEBUG = false

// Debug ...
func Debug(text interface{}, level int) {
	if !DEBUG {
		return
	}

	var buffer bytes.Buffer
	for i := 0; i < level; i++ {
		buffer.WriteString("  ")
	}

	fmt.Print(">> " + buffer.String())
	fmt.Println(text)
}
