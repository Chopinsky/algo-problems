package lfu

import (
	"errors"
	"fmt"

	"../Support"
)

// Cache ...
type Cache struct {
	freqStore map[int]*support.List
	mapStore  map[int]*support.Node
	capacity  int
}

// InitCache ...
func InitCache(capacity int) (*Cache, error) {
	if capacity < 1 {
		return nil, errors.New("Cache capacity must be equal or larger than 1")
	}

	cache := &Cache{
		make(map[int]*support.List),
		make(map[int]*support.Node),
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
	if node := cache.mapStore[key]; node != nil {
		if node.GetValue() != value {
			node.SetValue(value)
		}

		cache.touch(node)
		return
	}

	// get space for the new entry
	size := len(cache.mapStore)
	if size >= cache.capacity {
		cache.shrinkBy(size - cache.capacity + 1)
	}

	newNode := support.NewNode(key, value)
	cache.mapStore[key] = newNode

	if store, ok := cache.freqStore[1]; ok {
		store.Push(newNode)
	} else {
		cache.freqStore[1] = support.NewList(newNode)
	}
}

// Get ...
func (cache *Cache) Get(key int) int {
	if node := cache.mapStore[key]; node != nil {
		cache.touch(node)
		return node.GetValue()
	}

	return -1
}

func (cache *Cache) touch(node *support.Node) {
	freq := node.GetFreq()
	node.Detach()

	if store, ok := cache.freqStore[freq]; ok {
		if store.IsEmpty() {
			delete(cache.freqStore, freq)
		}
	}

	freq++
	node.Touch()

	if store, ok := cache.freqStore[freq]; ok {
		store.Push(node)
	} else {
		cache.freqStore[freq] = support.NewList(node)
	}
}

func (cache *Cache) shrinkBy(count int) {
	var key int
	freq := 1

	for {
		if store, ok := cache.freqStore[freq]; ok {
			for {
				if !store.IsEmpty() {
					key = store.PopFront().GetKey()
					delete(cache.mapStore, key)

					count--
					if count == 0 {
						return
					}
				}

				if store.IsEmpty() {
					delete(cache.freqStore, freq)
					break
				}
			}
		}

		freq++
	}
}
