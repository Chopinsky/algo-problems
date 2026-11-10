"""Hand-rolled ``SortedList`` -- a dependency-free port of
``sortedcontainers.SortedList``.

Every public method of sortedcontainers 2.4.0's ``SortedList`` is
implemented, plus the dunder operators.  Nothing is imported: binary
search, merging, comparison and iteration are all written out by hand.

Storage is one plain Python list of ``(sort_key, value)`` pairs kept in
ascending sort-key order.  When ``key`` is ``None`` the sort key is the
value itself.  Insert and delete are O(n) because of list shifting;
lookups are O(log n) comparisons.  That trade-off keeps the code
readable -- this is an exercise, not an attempt to reproduce
sortedcontainers' block index and its benchmark numbers.

Comparisons against other sequences are lexicographic, exactly like the
library.  ``append``, ``extend``, ``insert``, ``reverse`` and
``__setitem__`` raise ``NotImplementedError`` on purpose, matching
upstream behaviour.

The ``key`` argument (upstream dispatches it to ``SortedKeyList``) is
accepted here and handled in place, so a single class covers both modes.
"""


def _first(pair):
    """Sort key for a ``(sort_key, value)`` pair."""
    return pair[0]


def _is_sequence(obj):
    """Return True if *obj* behaves like ``collections.abc.Sequence``.

    Implemented without importing ``collections.abc``: the built-in
    sequence types are named explicitly, and anything else has to expose
    ``__len__`` and ``__getitem__`` without looking like a mapping.
    """
    if isinstance(obj, (list, tuple, str, bytes, bytearray, range)):
        return True
    cls = type(obj)
    return (hasattr(cls, '__len__') and hasattr(cls, '__getitem__')
            and not hasattr(obj, 'keys'))


def _op_eq(left, right):
    return left == right


def _op_ne(left, right):
    return left != right


def _op_lt(left, right):
    return left < right


def _op_le(left, right):
    return left <= right


def _op_gt(left, right):
    return left > right


def _op_ge(left, right):
    return left >= right


class SortedList:
    """Sorted mutable sequence with a hand-rolled binary search."""

    DEFAULT_LOAD_FACTOR = 1000
    _repr_running = False

    # ------------------------------------------------------------------
    # construction and internals
    # ------------------------------------------------------------------

    def __init__(self, iterable=None, key=None):
        self._key = key
        self._load = self.DEFAULT_LOAD_FACTOR
        self._items = []
        if iterable is not None:
            self._build(iterable)

    @staticmethod
    def _search_left(items, key):
        """Hand-rolled ``bisect_left`` over the first element of pairs."""
        lo = 0
        hi = len(items)
        while lo < hi:
            mid = (lo + hi) // 2
            if items[mid][0] < key:
                lo = mid + 1
            else:
                hi = mid
        return lo

    @staticmethod
    def _search_right(items, key):
        """Hand-rolled ``bisect_right`` over the first element of pairs."""
        lo = 0
        hi = len(items)
        while lo < hi:
            mid = (lo + hi) // 2
            if key < items[mid][0]:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def _build(self, values):
        key = self._key
        if key is None:
            items = [(value, value) for value in values]
        else:
            items = [(key(value), value) for value in values]
        items.sort(key=_first)
        self._items = items

    def _values_list(self):
        return [pair[1] for pair in self._items]

    @property
    def key(self):
        """Function used to extract the comparison key, or ``None``."""
        return self._key

    def _reset(self, load):
        """Reset the load factor.

        The flat-list implementation keeps the value only so that
        ``_check`` can validate it; it has no effect on layout.
        """
        values = self._values_list()
        self._load = load
        self._build(values)

    # ------------------------------------------------------------------
    # adding values
    # ------------------------------------------------------------------

    def add(self, value):
        key = value if self._key is None else self._key(value)
        pos = self._search_right(self._items, key)
        self._items.insert(pos, (key, value))

    def update(self, iterable):
        values = list(iterable)
        if not values:
            return
        key = self._key
        if key is None:
            new_items = [(value, value) for value in values]
        else:
            new_items = [(key(value), value) for value in values]
        if not self._items:
            new_items.sort(key=_first)
            self._items = new_items
            return
        merged = self._items + new_items
        merged.sort(key=_first)
        self._items = merged

    _update = update

    def __add__(self, other):
        values = self._values_list()
        values.extend(other)
        return type(self)(values, self._key)

    __radd__ = __add__

    def __iadd__(self, other):
        self.update(other)
        return self

    def __mul__(self, num):
        values = self._values_list() * num
        return type(self)(values, self._key)

    __rmul__ = __mul__

    def __imul__(self, num):
        values = self._values_list() * num
        self._build(values)
        return self

    # ------------------------------------------------------------------
    # removing values
    # ------------------------------------------------------------------

    def clear(self):
        self._items = []

    _clear = clear

    def _find(self, value):
        """Return the index of the first value equal to *value*, or -1."""
        items = self._items
        if self._key is None:
            pos = self._search_left(items, value)
            if pos < len(items) and items[pos][1] == value:
                return pos
            return -1
        key = self._key(value)
        pos = self._search_left(items, key)
        while pos < len(items):
            stored_key, stored_value = items[pos]
            if stored_key != key:
                break
            if stored_value == value:
                return pos
            pos += 1
        return -1

    def discard(self, value):
        pos = self._find(value)
        if pos != -1:
            del self._items[pos]

    def remove(self, value):
        pos = self._find(value)
        if pos == -1:
            raise ValueError('{0!r} not in list'.format(value))
        del self._items[pos]

    def pop(self, index=-1):
        if not self._items:
            raise IndexError('pop index out of range')
        length = len(self._items)
        if index < -length or index >= length:
            raise IndexError('list index out of range')
        pair = self._items.pop(index)
        return pair[1]

    def __delitem__(self, index):
        if isinstance(index, slice):
            del self._items[index]
            return
        length = len(self._items)
        if index < -length or index >= length:
            raise IndexError('list index out of range')
        del self._items[index]

    # ------------------------------------------------------------------
    # looking up values
    # ------------------------------------------------------------------

    def __contains__(self, value):
        return self._find(value) != -1

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [pair[1] for pair in self._items[index]]
        return self._items[index][1]

    def __setitem__(self, index, value):
        raise NotImplementedError(
            'use ``del sl[index]`` and ``sl.add(value)`` instead')

    def bisect_left(self, value):
        key = value if self._key is None else self._key(value)
        return self._search_left(self._items, key)

    def bisect_right(self, value):
        key = value if self._key is None else self._key(value)
        return self._search_right(self._items, key)

    bisect = bisect_right
    _bisect_right = bisect_right

    def count(self, value):
        key = value if self._key is None else self._key(value)
        left = self._search_left(self._items, key)
        right = self._search_right(self._items, key)
        if self._key is None:
            return right - left
        total = 0
        for index in range(left, right):
            if self._items[index][1] == value:
                total += 1
        return total

    def index(self, value, start=None, stop=None):
        length = len(self._items)
        if not length:
            raise ValueError('{0!r} is not in list'.format(value))

        if start is None:
            start = 0
        if start < 0:
            start += length
        if start < 0:
            start = 0

        if stop is None:
            stop = length
        if stop < 0:
            stop += length
        if stop > length:
            stop = length

        if stop <= start:
            raise ValueError('{0!r} is not in list'.format(value))

        left = self.bisect_left(value)
        right = self.bisect_right(value)

        if self._key is None:
            pos = left if left > start else start
            if pos < right and pos < stop and pos < length:
                if self._items[pos][1] == value:
                    return pos
        else:
            first = left if left > start else start
            last = right if right < stop else stop
            for pos in range(first, last):
                if self._items[pos][1] == value:
                    return pos

        raise ValueError('{0!r} is not in list'.format(value))

    # ------------------------------------------------------------------
    # iterating values
    # ------------------------------------------------------------------

    def __iter__(self):
        return (pair[1] for pair in self._items)

    def __reversed__(self):
        return (pair[1] for pair in reversed(self._items))

    def islice(self, start=None, stop=None, reverse=False):
        if not self._items:
            return iter(())
        start, stop, _ = slice(start, stop).indices(len(self._items))
        return self._islice(start, stop, reverse)

    def _islice(self, start, stop, reverse):
        if start >= stop:
            return iter(())
        items = self._items
        if reverse:
            return (items[index][1]
                    for index in range(stop - 1, start - 1, -1))
        return (items[index][1] for index in range(start, stop))

    def irange(self, minimum=None, maximum=None, inclusive=(True, True),
               reverse=False):
        if minimum is None:
            start = 0
        elif inclusive[0]:
            start = self.bisect_left(minimum)
        else:
            start = self.bisect_right(minimum)

        if maximum is None:
            stop = len(self._items)
        elif inclusive[1]:
            stop = self.bisect_right(maximum)
        else:
            stop = self.bisect_left(maximum)

        return self._islice(start, stop, reverse)

    # ------------------------------------------------------------------
    # miscellany
    # ------------------------------------------------------------------

    def __len__(self):
        return len(self._items)

    def copy(self):
        clone = type(self)(key=self._key)
        clone._items = list(self._items)
        return clone

    __copy__ = copy

    def append(self, value):
        raise NotImplementedError('use ``sl.add(value)`` instead')

    def extend(self, values):
        raise NotImplementedError('use ``sl.update(values)`` instead')

    def insert(self, index, value):
        raise NotImplementedError('use ``sl.add(value)`` instead')

    def reverse(self):
        raise NotImplementedError('use ``reversed(sl)`` instead')

    def _compare(self, other, op):
        if isinstance(other, SortedList):
            other_values = other._values_list()
        elif _is_sequence(other):
            other_values = other
        else:
            return NotImplemented

        self_values = self._values_list()
        self_len = len(self_values)
        other_len = len(other_values)

        if self_len != other_len:
            if op is _op_eq:
                return False
            if op is _op_ne:
                return True

        for alpha, beta in zip(self_values, other_values):
            if alpha != beta:
                return op(alpha, beta)

        return op(self_len, other_len)

    def __eq__(self, other):
        return self._compare(other, _op_eq)

    def __ne__(self, other):
        return self._compare(other, _op_ne)

    def __lt__(self, other):
        return self._compare(other, _op_lt)

    def __le__(self, other):
        return self._compare(other, _op_le)

    def __gt__(self, other):
        return self._compare(other, _op_gt)

    def __ge__(self, other):
        return self._compare(other, _op_ge)

    def __reduce__(self):
        values = self._values_list()
        if self._key is None:
            return (type(self), (values,))
        return (type(self), (values, self._key))

    def __repr__(self):
        cls = type(self)
        if cls._repr_running:
            return '...'
        cls._repr_running = True
        try:
            return '{0}({1!r})'.format(cls.__name__, self._values_list())
        finally:
            cls._repr_running = False

    def _check(self):
        assert self._load >= 4
        items = self._items
        for pos in range(1, len(items)):
            assert not (items[pos][0] < items[pos - 1][0])
        if self._key is not None:
            for stored_key, stored_value in items:
                assert stored_key == self._key(stored_value)


# ----------------------------------------------------------------------
# verification
# ----------------------------------------------------------------------

def _ref_bisect_left(seq, value):
    lo = 0
    hi = len(seq)
    while lo < hi:
        mid = (lo + hi) // 2
        if seq[mid] < value:
            lo = mid + 1
        else:
            hi = mid
    return lo


def _ref_bisect_right(seq, value):
    lo = 0
    hi = len(seq)
    while lo < hi:
        mid = (lo + hi) // 2
        if value < seq[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def _lcg(seed):
    """Tiny deterministic pseudo-random generator (no ``random`` import)."""
    state = seed
    while True:
        state = (1103515245 * state + 12345) & 0x7FFFFFFF
        yield state


def _self_test():
    # construction
    assert list(SortedList()) == []
    assert list(SortedList([3, 1, 2, 5, 4])) == [1, 2, 3, 4, 5]
    assert list(SortedList('cab')) == ['a', 'b', 'c']
    assert repr(SortedList([1, 2, 3])) == 'SortedList([1, 2, 3])'
    assert len(SortedList([1, 2, 3])) == 3

    # add / update
    sl = SortedList()
    sl.add(3)
    sl.add(1)
    sl.add(2)
    assert sl == [1, 2, 3]
    sl.add(2)
    assert sl == [1, 2, 2, 3]
    sl.update([0, 5, 2])
    assert sl == [0, 1, 2, 2, 2, 3, 5]
    sl.update([])
    assert sl == [0, 1, 2, 2, 2, 3, 5]
    sl.update(sl)
    assert sl == [0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 5, 5]

    # clear
    sl = SortedList([1, 2, 3])
    sl.clear()
    assert sl == [] and len(sl) == 0

    # lookup
    sl = SortedList([1, 2, 2, 2, 3])
    assert sl.bisect_left(2) == 1
    assert sl.bisect_right(2) == 4
    assert sl.bisect(2) == 4
    assert sl.count(2) == 3
    assert sl.count(9) == 0
    assert 2 in sl and 9 not in sl

    # discard / remove
    sl = SortedList([1, 2, 2, 3])
    sl.discard(2)
    assert sl == [1, 2, 3]
    sl.discard(99)
    assert sl == [1, 2, 3]
    sl.remove(2)
    assert sl == [1, 3]
    try:
        sl.remove(99)
    except ValueError as error:
        assert str(error) == '99 not in list'
    else:
        assert False

    # pop
    sl = SortedList('abcde')
    assert sl.pop() == 'e'
    assert sl.pop(2) == 'c'
    assert sl == ['a', 'b', 'd']
    assert sl.pop(-1) == 'd'
    assert sl.pop(0) == 'a'
    assert sl.pop() == 'b'
    try:
        sl.pop()
    except IndexError as error:
        assert str(error) == 'pop index out of range'
    else:
        assert False

    # index
    sl = SortedList('abcde')
    assert sl.index('d') == 3
    assert sl.index('a', 0, 2) == 0
    try:
        sl.index('a', 1)
    except ValueError as error:
        assert str(error) == "'a' is not in list"
    else:
        assert False
    sl = SortedList([1, 2, 2, 2, 3])
    assert sl.index(2) == 1
    assert sl.index(2, 2) == 2
    assert sl.index(2, -3) == 2
    assert sl.index(2, 0, 2) == 1
    try:
        sl.index(2, 0, 1)
    except ValueError:
        pass
    else:
        assert False

    # irange
    sl = SortedList('abcdefghij')
    assert list(sl.irange('c', 'f')) == list('cdef')
    assert list(sl.irange('c', 'f', (False, False))) == list('de')
    assert list(sl.irange('c', 'f', (True, False))) == list('cde')
    assert list(sl.irange('c', 'f', (False, True))) == list('def')
    assert list(sl.irange('c', 'f', reverse=True)) == list('fedc')
    assert list(sl.irange()) == list('abcdefghij')
    assert list(sl.irange('z')) == []
    sl = SortedList([1, 2, 2, 2, 3])
    assert list(sl.irange(2, 2)) == [2, 2, 2]
    assert list(sl.irange(2, 2, (False, False))) == []
    assert list(sl.irange(2, 2, (True, False))) == []
    assert list(sl.irange(2, 2, (False, True))) == []

    # islice
    sl = SortedList('abcdefghij')
    assert list(sl.islice(2, 6)) == list('cdef')
    assert list(sl.islice(2, 6, True)) == list('fedc')
    assert list(sl.islice()) == list('abcdefghij')
    assert list(sl.islice(-3)) == list('hij')
    assert list(sl.islice(5, 2)) == []
    assert list(SortedList().islice()) == []

    # iteration
    assert list(iter(sl)) == list('abcdefghij')
    assert list(reversed(sl)) == list('jihgfedcba')

    # getitem
    sl = SortedList('abcde')
    assert sl[1] == 'b'
    assert sl[-1] == 'e'
    assert sl[2:5] == ['c', 'd', 'e']
    assert sl[::-1] == ['e', 'd', 'c', 'b', 'a']
    assert sl[10:20] == []
    try:
        sl[10]
    except IndexError:
        pass
    else:
        assert False
    try:
        SortedList()[0]
    except IndexError:
        pass
    else:
        assert False

    # delitem
    sl = SortedList('abcde')
    del sl[2]
    assert sl == ['a', 'b', 'd', 'e']
    del sl[:2]
    assert sl == ['d', 'e']
    sl = SortedList('abcdef')
    del sl[::2]
    assert sl == ['b', 'd', 'f']

    sl = SortedList([1, 2, 3])
    try:
        del sl[10]
    except IndexError as error:
        assert str(error) == 'list index out of range'
    else:
        assert False
    try:
        sl.pop(10)
    except IndexError as error:
        assert str(error) == 'list index out of range'
    else:
        assert False

    # add / iadd
    sl = SortedList('bat')
    assert sl + SortedList('cat') == list('aabctt')
    assert sl + ['z'] == list('abtz')
    assert ['z'] + sl == list('abtz')
    sl = SortedList('bat')
    sl += 'cat'
    assert sl == list('aabctt')

    # mul / imul
    sl = SortedList('abc')
    assert sl * 3 == list('aaabbbccc')
    assert 3 * sl == list('aaabbbccc')
    assert sl * 0 == []
    sl *= 3
    assert sl == list('aaabbbccc')

    # comparisons
    assert SortedList([1, 2, 3]) == [1, 2, 3]
    assert [1, 2, 3] == SortedList([1, 2, 3])
    assert SortedList([1, 2, 3]) == (1, 2, 3)
    assert SortedList([1, 2, 3]) != [1, 2]
    assert SortedList([1, 2, 3]) < [1, 2, 4]
    assert SortedList([1, 2, 3]) <= [1, 2, 3]
    assert SortedList([1, 2, 3]) > [1, 2]
    assert SortedList([1, 2, 3]) >= [1, 2, 3]
    assert SortedList([1, 2, 3]) > [1, 2, 2, 9]
    assert (SortedList([1]) == 5) is False
    try:
        SortedList([1]) < 5
    except TypeError:
        pass
    else:
        assert False

    # copy / reset / check
    sl = SortedList([3, 1, 2])
    clone = sl.copy()
    assert clone == sl and clone is not sl
    clone.add(0)
    assert sl == [1, 2, 3] and clone == [0, 1, 2, 3]
    sl._check()
    sl._reset(4)
    sl._check()
    assert sl == [1, 2, 3]

    # reduce
    func, args = SortedList([1, 2, 3]).__reduce__()
    assert func is SortedList and args == ([1, 2, 3],)

    # key mode
    sl = SortedList([3, 1, 2], key=lambda value: -value)
    assert list(sl) == [3, 2, 1]
    assert sl.key is not None
    sl.add(4)
    assert list(sl) == [4, 3, 2, 1]
    assert sl.bisect_left(2) == 2
    assert sl.bisect_right(2) == 3
    assert sl.count(2) == 1
    assert 2 in sl and 5 not in sl
    assert sl.index(2) == 2
    assert list(sl.irange(3, 1)) == [3, 2, 1]
    assert list(sl.islice(0, 2)) == [4, 3]
    assert sl[0] == 4 and sl[-1] == 1
    assert sl[:2] == [4, 3]
    assert sl == [4, 3, 2, 1]
    sl.discard(3)
    assert list(sl) == [4, 2, 1]
    sl.remove(2)
    assert list(sl) == [4, 1]
    assert sl.pop() == 1
    assert sl + [5] == [5, 4]
    assert sl * 2 == [4, 4]
    clone = sl.copy()
    assert clone == [4] and clone.key is sl.key
    clone._check()
    func, args = SortedList([1, 2], key=abs).__reduce__()
    assert func is SortedList and args[0] == [1, 2] and args[1] is abs

    # unsupported mutable-sequence methods
    sl = SortedList([1])
    for call in (
        lambda: sl.append(2),
        lambda: sl.extend([2]),
        lambda: sl.insert(0, 2),
        lambda: sl.reverse(),
        lambda: sl.__setitem__(0, 2),
    ):
        try:
            call()
        except NotImplementedError:
            pass
        else:
            assert False

    # deterministic fuzz against a plain sorted list
    gen = _lcg(12345)
    reference = []
    sl = SortedList()
    for _ in range(400):
        op = next(gen) % 6
        value = next(gen) % 50
        if op == 0:
            sl.add(value)
            reference.append(value)
            reference.sort()
        elif op == 1 and reference:
            index = next(gen) % len(reference)
            assert sl.pop(index) == reference.pop(index)
        elif op == 2:
            sl.discard(value)
            if value in reference:
                reference.remove(value)
        elif op == 3:
            assert sl.bisect_left(value) == _ref_bisect_left(
                reference, value)
            assert sl.bisect_right(value) == _ref_bisect_right(
                reference, value)
        elif op == 4:
            assert sl.count(value) == reference.count(value)
            assert (value in sl) == (value in reference)
        else:
            if reference:
                value = reference[next(gen) % len(reference)]
                assert sl.index(value) == reference.index(value)
                sl.remove(value)
                reference.remove(value)
        assert list(sl) == reference
    sl._check()
    assert list(sl.islice()) == reference
    assert list(sl.islice(reverse=True)) == reference[::-1]


if __name__ == '__main__':
    _self_test()
    print('sorted_list.py: all checks passed')
