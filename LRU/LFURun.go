package lru

import "fmt"

// Run ...
func Run(capacity int, _debug bool) {
	cache, err := InitCache(capacity)
	if err != nil {
		fmt.Println("LFU quit with errors...")
		return
	}

	cache.Put(1, 1)
	cache.Put(2, 2)
	fmt.Println(cache.Get(1))

	cache.Put(3, 3)
	fmt.Println(cache.Get(2))
	fmt.Println(cache.Get(3))

	cache.Put(4, 4)
	fmt.Println(cache.Get(1))
	fmt.Println(cache.Get(3))
	fmt.Println(cache.Get(4))

	fmt.Println("\nLFU done...")
}
