package utils

import (
	"fmt"
)

// Output ...
func Output(calculated, expected interface{}) {
	fmt.Println("Calculated result: ", calculated)
	fmt.Println("Expected result:   ", expected)
}
