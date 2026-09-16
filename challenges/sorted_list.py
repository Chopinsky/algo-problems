"""SortedList on BUCKETED BLOCKS (sqrt decomposition), from scratch.

No `bisect` library. No `list.insert`, no `pop(i)`, no `remove/index/count`.
The ONLY list mutators used are `append` (O(1)) and `pop()` with no index
(O(1) trim of the last slot). Every shift of elements is an explicit loop
so the algorithm — not C internals — is what you read.

Internal data structure
-----------------------
  self._blocks: list of sorted lists ("blocks"), e.g. [[1, 1, 3], [4, 5, 9]]
  self._size:   total number of elements
  INVARIANT: every element of block[i] <= every element of block[i+1],
  and each block holds between ~cap/2 and cap elements (cap = block_size).

  Why blocks? A single flat list shifts O(n) per insert. With ~sqrt(n)
  blocks of ~sqrt(n) items, an insert shifts only inside ONE block: O(sqrt n).
  Full production versions (e.g. `sortedcontainers`) do the same with big
  caps (~1000). Here cap defaults to 4 so splits/merges show up in the demo.
"""

from __future__ import annotations

from typing import Iterable, Iterator, List, Optional


# ------------------------------------------------------------------
# Group 0 — Hand-rolled binary search (no library)
# ------------------------------------------------------------------
# LOGIC: half-open window [lo, hi) that must contain the answer.
# Probe mid = (lo + hi) // 2, discard one half per step, O(log n).
#   - left:  a[mid] < x  -> answer is right of mid  (finds LEFTMOST slot)
#   - right: x < a[mid]  -> answer is at/left of mid (slot PAST last x)
#
# WALKING EXAMPLE with a == [1, 3, 4, 5], x == 4, left-search:
#   [0,4) mid=2 a[2]=4, 4<4? No  -> [0,2)
#   [0,2) mid=1 a[1]=3, 3<4? Yes -> [2,2) -> return 2
def _bisect_left(a: List, x, lo: int = 0, hi: Optional[int] = None) -> int:
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def _bisect_right(a: List, x, lo: int = 0, hi: Optional[int] = None) -> int:
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


# ------------------------------------------------------------------
# Group 1 — Manual shift primitives (replaces list.insert / pop(i))
# ------------------------------------------------------------------
# LOGIC: to insert at pos, grow with append then move each tail element
# one slot RIGHT, from the end backwards (so nothing is overwritten).
# To delete at pos, move each tail element one slot LEFT, then trim the
# duplicated last slot with pop() (no index -> O(1), no hidden shift).
#
# WALKING EXAMPLE with block == [1, 4, 5], insert 3 at pos 1:
#   append -> [1, 4, 5, 5]  (last slot is scratch space)
#   i=3: block[3]=block[2] -> [1, 4, 5, 5]
#   i=2: block[2]=block[1] -> [1, 4, 4, 5]
#   block[1]=3             -> [1, 3, 4, 5]
def _manual_insert_at(block: List, pos: int, x) -> None:
    block.append(x)  # scratch slot; overwritten below unless pos is the end
    i = len(block) - 1
    while i > pos:
        block[i] = block[i - 1]
        i -= 1
    block[pos] = x


def _manual_pop_at(block: List, pos: int):
    val = block[pos]
    n = len(block)
    i = pos
    while i < n - 1:
        block[i] = block[i + 1]
        i += 1
    block.pop()  # trim duplicated tail slot; O(1)
    return val


class SortedList:
    """Sorted container on bucketed blocks. Allows duplicates."""

    # ------------------------------------------------------------------
    # Group 2 — Block directory: storage invariant + construction
    # ------------------------------------------------------------------
    # LOGIC: _blocks[i] sorted internally, and max(block[i]) <= min(block[i+1]).
    # __init__ sorts once, then CHUNKS into blocks of cap (explicit loops,
    # append-only). Every mutation restores the invariant via split/merge.
    #
    # WALKING EXAMPLE: SortedList([5, 1, 4, 3, 2], block_size=2)
    #   sorted -> [1, 2, 3, 4, 5] -> chunks -> [[1, 2], [3, 4], [5]]
    def __init__(self, iterable: Optional[Iterable] = None, block_size: int = 4) -> None:
        self._block_size = max(2, block_size)
        self._blocks: List[List] = []
        self._size = 0

        if iterable is None:
            return

        data = list(iterable)
        data.sort()
        block: List = []
        for v in data:
            block.append(v)
            self._size += 1
            if len(block) >= self._block_size:
                self._blocks.append(block)
                block = []

        if block:
            self._blocks.append(block)

    def _block_maxes(self) -> List:
        maxes: List = []
        for b in self._blocks:
            maxes.append(b[-1])

        return maxes

    # ------------------------------------------------------------------
    # Group 3 — Search: locate the block, then binary-search inside it
    # ------------------------------------------------------------------
    # LOGIC: blocks are ordered, so scan block maxes (linear, O(#blocks))
    # to find the first block that can hold x, then _bisect_* inside that
    # one block (O(log cap)). Global rank = sizes of skipped blocks +
    # in-block position. Duplicates spanning blocks accumulate naturally.
    #
    # WALKING EXAMPLE with blocks == [[1, 1, 3], [4, 5]], x == 4:
    #   block 0: max=3, 4 > 3 -> skip, rank += 3
    #   block 1: max=5, 4 <= 5 -> stop; _bisect_left([4,5],4)=0
    #   global bisect_left(4) = 3 + 0 = 3
    def _locate_for_insert(self, x) -> int:
        for i, b in enumerate(self._blocks):
            if x <= b[-1]:
                return i

        return len(self._blocks) - 1

    def bisect_left(self, value) -> int:
        rank = 0
        for b in self._blocks:
            if value <= b[-1]:
                rank += _bisect_left(b, value)
                break

            rank += len(b)

        return rank

    def bisect_right(self, value) -> int:
        rank = 0
        for b in self._blocks:
            if not b:
                continue

            if value < b[0]:
                break

            if value >= b[-1]:
                rank += len(b)
                continue

            rank += _bisect_right(b, value)
            break

        return rank

    bisect = bisect_right

    def __contains__(self, value) -> bool:
        for b in self._blocks:
            if not b:
                continue

            if value > b[len(b) - 1]:
                continue

            pos = _bisect_left(b, value)
            return pos < len(b) and b[pos] == value

        return False

    def count(self, value) -> int:
        return self.bisect_right(value) - self.bisect_left(value)

    def _get_at(self, rank: int):
        for b in self._blocks:
            if rank < len(b):
                return b[rank]

            rank -= len(b)

        raise IndexError("rank out of range")

    def index(self, value, start: int = 0, stop: Optional[int] = None) -> int:
        stop = self._size if stop is None else stop
        i = self.bisect_left(value)
        if start <= i < stop and i < self._size and self._get_at(i) == value:
            return i
        raise ValueError(f"{value!r} is not in SortedList")

    # ------------------------------------------------------------------
    # Group 4 — Mutation: insert/split, remove/merge, pop by rank
    # ------------------------------------------------------------------
    # LOGIC (add): locate block -> in-block _bisect_right -> _manual_insert_at
    # (explicit shift) -> if block overflows (len > cap): SPLIT into halves
    # by distributing elements with append-only loops into two new blocks
    # and rebuilding the directory (also append-only).
    # LOGIC (remove/discard): scan blocks in order for the leftmost x,
    # _manual_pop_at it; drop empty blocks, merge tiny ones with a neighbour.
    # LOGIC (pop k): walk blocks by size to the owning block, pop inside it.
    #
    # WALKING EXAMPLE (cap=4), blocks == [[1, 1, 3, 4]]:
    #   add(5): block 0 (5 > max 4? last block anyway), pos=4
    #     manual shift (pos is end: just the append) -> [1, 1, 3, 4, 5]
    #     len 5 > cap 4 -> SPLIT at mid=2 -> [[1, 1], [3, 4, 5]]
    #   remove(1): block 0, _bisect_left=0, manual pop -> [[1], [3, 4, 5]]
    #     block 0 len 1 < 2 -> MERGE -> [[1, 3, 4, 5]]
    def _split(self, bi: int) -> None:
        block = self._blocks[bi]
        mid = len(block) // 2
        left: List = []
        right: List = []
        i = 0
        for v in block:
            if i < mid:
                left.append(v)
            else:
                right.append(v)
            i += 1

        new_blocks: List[List] = []
        for j, b in enumerate(self._blocks):
            if j == bi:
                new_blocks.append(left)
                new_blocks.append(right)
            else:
                new_blocks.append(b)

        self._blocks = new_blocks

    def _drop_block(self, bi: int) -> None:
        new_blocks: List[List] = []
        for j, b in enumerate(self._blocks):
            if j != bi:
                new_blocks.append(b)
        self._blocks = new_blocks

    def _merge_with_next(self, bi: int) -> None:
        first = self._blocks[bi]
        second = self._blocks[bi + 1]
        merged: List = []
        for v in first:
            merged.append(v)
        for v in second:
            merged.append(v)
        new_blocks: List[List] = []
        for j, b in enumerate(self._blocks):
            if j == bi:
                new_blocks.append(merged)
            elif j == bi + 1:
                continue
            else:
                new_blocks.append(b)
        self._blocks = new_blocks
        if len(merged) > self._block_size:
            self._split(bi)

    def _cleanup(self, bi: int) -> None:
        if bi >= len(self._blocks):
            return
        if len(self._blocks[bi]) == 0:
            self._drop_block(bi)
            return
        if len(self._blocks) > 1 and len(self._blocks[bi]) < self._block_size // 2:
            if bi + 1 < len(self._blocks):
                self._merge_with_next(bi)
            else:
                self._merge_with_next(bi - 1)

    def add(self, value) -> None:
        if not self._blocks:
            self._blocks.append([value])
            self._size = 1
            return
        bi = self._locate_for_insert(value)
        block = self._blocks[bi]
        pos = _bisect_right(block, value)
        _manual_insert_at(block, pos, value)
        self._size += 1
        if len(block) > self._block_size:
            self._split(bi)

    def remove(self, value) -> None:
        for bi, b in enumerate(self._blocks):
            if not b or value > b[len(b) - 1]:
                continue
            pos = _bisect_left(b, value)
            if pos < len(b) and b[pos] == value:
                _manual_pop_at(b, pos)
                self._size -= 1
                self._cleanup(bi)
                return
            return  # value < b[0]: ordered blocks -> cannot be later
        raise ValueError(f"{value!r} is not in SortedList")

    def discard(self, value) -> bool:
        for bi, b in enumerate(self._blocks):
            if not b or value > b[len(b) - 1]:
                continue
            pos = _bisect_left(b, value)
            if pos < len(b) and b[pos] == value:
                _manual_pop_at(b, pos)
                self._size -= 1
                self._cleanup(bi)
                return True
            return False
        return False

    def pop(self, index: int = -1):
        if self._size == 0:
            raise IndexError("pop from empty SortedList")
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError("pop index out of range")
        for bi, b in enumerate(self._blocks):
            if index < len(b):
                val = _manual_pop_at(b, index)
                self._size -= 1
                self._cleanup(bi)
                return val
            index -= len(b)
        raise IndexError("pop index out of range")  # unreachable

    def clear(self) -> None:
        self._blocks = []
        self._size = 0

    # ------------------------------------------------------------------
    # Group 5 — Access: rank reads over the block directory
    # ------------------------------------------------------------------
    # LOGIC: sl[0] walks zero blocks (min), sl[-1] walks to the last item
    # (max); iteration yields block by block, already globally sorted.
    #
    # WALKING EXAMPLE with blocks == [[1, 3], [4, 5]]:
    #   sl[0]: rank 0 < len(block0)=2 -> 1 (min, no search)
    #   sl[-1]: rank 3 -> skip block0 (3-2=1) -> block1[1] = 5 (max)
    #   list(sl): 1, 3, then 4, 5
    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.to_list()[index]
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError("SortedList index out of range")
        rank = index
        for b in self._blocks:
            if rank < len(b):
                return b[rank]
            rank -= len(b)
        raise IndexError("SortedList index out of range")  # unreachable

    def __iter__(self) -> Iterator:
        for b in self._blocks:
            for v in b:
                yield v

    def __repr__(self) -> str:
        return f"SortedList({self.to_list()!r}, blocks={self._blocks!r})"

    def to_list(self) -> List:
        out: List = []
        for b in self._blocks:
            for v in b:
                out.append(v)
        return out


def demo() -> None:
    """Walking example: add numbers (watch splits), then query."""
    print("=== SortedList walking example (bucketed blocks, cap=4) ===")
    sl = SortedList(block_size=4)
    print(f"start: blocks={sl._blocks}")

    for x in [5, 1, 4, 1, 3, 9, 2, 0, 6]:
        sl.add(x)
        print(f"add({x}): blocks={sl._blocks} flat={sl.to_list()}")

    print(f"\nfinal flat: {sl.to_list()}")
    print(f"len: {len(sl)}, min sl[0]={sl[0]}, max sl[-1]={sl[-1]}, sl[2]={sl[2]}")
    print(f"contains 4? {4 in sl}, contains 9? {9 in sl}")
    print(f"bisect_left(4)={sl.bisect_left(4)}, bisect_right(4)={sl.bisect_right(4)}")
    print(f"count(1)={sl.count(1)}, index(3)={sl.index(3)}")
    print(f"iterate: {list(sl)}")

    sl.remove(1)
    print(f"\nafter remove(1): blocks={sl._blocks} flat={sl.to_list()}")
    print(f"discard(9) -> {sl.discard(9)}, blocks={sl._blocks}")
    print(f"pop(0) -> {sl.pop(0)} (removes min), flat={sl.to_list()}")
    print(f"pop() -> {sl.pop()} (removes max), flat={sl.to_list()}")


if __name__ == "__main__":
    demo()
