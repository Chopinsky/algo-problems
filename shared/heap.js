'use strict';

const lessFunc = function (a, b) {
	return a < b;
}

const heap = function (arr, less) {
	const _heap = Array.isArray(arr) ? arr : [];
	const _less = typeof less === 'function' ? less : lessFunc;

	const heapify = function () {
		for (let i = Math.floor(_heap.length / 2); i >= 0; i--) {
			siftDown(i);
		}
	};

	const push = function (val) {
		_heap.push(val);
		siftUp(_heap.length - 1);
	};

	const pop = function () {
		if (_heap.length === 0) {
			return null;
		}

		swap(0, _heap.length - 1);
		const item = _heap.pop();

		siftDown(0);
		return item;
	};

	const len = function () {
		return _heap.length;
	}

	const toSortedArr = function () {
		const ans = [];

		while (_heap.length > 0) {
			ans.push(pop());
		}

		return ans;
	}

	const peak = function () {
		if (_heap.length === 0) {
			return null;
		}

		return _heap[0];
	}

	const swap = function (i, j) {
		const temp = _heap[i];
		_heap[i] = _heap[j];
		_heap[j] = temp;
	};

	const siftDown = function (i) {
		const size = _heap.length;
		if (i >= (size / 2)) {
			return;
		}

		let l = 2*i+1, r = 2*i+2, old = _heap[i];
		let idx = i;

		if (l < size && _less(_heap[l], _heap[idx])) {
			idx = l;
		}

		if (r < size && _less(_heap[r], _heap[idx])) {
			idx = r;
		}

		if (idx === l) {
			swap(i, l);
			siftDown(l);
		} else if (idx === r) {
			swap(i, r);
			siftDown(r);
		}
	};

	const siftUp = function (i) {
		if (i === 0 || i >= _heap.length) {
			return;
		}

		const p = Math.floor((i - 1) / 2);
		if (_less(_heap[i], _heap[p])) {
			swap(i, p);
			siftUp(p);
		}

		siftDown(i);
	};

	const print = function () {
		console.log(_heap);
	};

	if (_heap.length > 1) {
		heapify();
	}

	return {
		heapify,
		push,
		pop,
		peak,
		print,
		len,
		toSortedArr,
	};
};

module.exports = heap;
