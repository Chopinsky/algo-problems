package lfu

import (
	"errors"
	"fmt"
)

type node struct {
	key   int
	value int
}

// Cache ...
type Cache struct {
	store    map[int][]int
	storeMap map[int]*node
	capacity int
}

// InitCache ...
func InitCache(capacity int) (*Cache, error) {
	if capacity < 1 {
		return nil, errors.New("Cache capacity must be equal or larger than 1")
	}

	cache := &Cache{
		make(map[int][]int),
		make(map[int]*node),
		1,
	}

	if err := cache.SetCapacity(capacity); err != nil {
		return nil, err
	}

	return cache, nil
}

// SetCapacity ...
func (cache *Cache) SetCapacity(c int) error {
	if c == cache.capacity {
		return nil
	}

	if c < 1 {
		return fmt.Errorf("Cache capacity must be larger than 1, but receiving %d", c)
	}

	if c < cache.capacity {
		cache.shrinkBy(cache.capacity - c)
	}

	cache.capacity = c
	return nil
}

// Put ...
func (cache *Cache) Put(key, value int) {
	if n := cache.storeMap[key]; n != nil {
		if n.value != value {
			n.value = value
		}

		cache.touch(n)
		return
	}

	newNode := &node{
		key,
		value,
	}

	cache.storeMap[key] = newNode

	size := len(cache.storeMap)
	if size > cache.capacity {
		cache.shrinkBy(size - cache.capacity)
	}
}

// Get ...
func (cache *Cache) Get(key int) int {
	if n := cache.storeMap[key]; n != nil {
		cache.touch(n)
		return n.value
	}

	return -1
}

func (cache *Cache) touch(node *node) {

}

func (cache *Cache) shrinkBy(count int) {
	for {
		break
	}
}

func (node *node) detach() {
}
