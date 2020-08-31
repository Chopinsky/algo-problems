/**
 * @param {number[][]} intervals
 * @return {number[]}
 */
var findRightInterval = function(intervals) {
  if (!intervals || intervals.length === 0) {
    return [];
  }

  if (intervals.length === 1) {
    return [-1];
  }

  const arr = [];
  for (let i = 0; i < intervals.length; i++) {
    arr.push({
      idx: i,
      start: intervals[i][0],
      end: intervals[i][1],
    })
  }

  arr.sort(function (a, b) {
    return a.start - b.start;
  });

  console.log(arr);

  const ans = new Array(intervals.length);

  for (let i = 0; i < arr.length; i++) {
    if (i === arr.length - 1) {
      ans[arr[i].idx] = -1;
      continue
    }

    const idx = find(arr, i);

    if (idx < 0) {
      ans[arr[i].idx] = -1;
    } else {
      ans[arr[i].idx] = arr[idx].idx;
    }
  }

  return ans;
};

var find = function (arr, i) {
  if (
    i === arr.length-1
    || (i === arr.length - 2 && arr[i].end > arr[i+1].start)
    || (arr[i].end > arr[arr.length-1].start)
  ) {
    return -1;
  }

  if (arr[i].end <= arr[i+1].start) {
    return i+1;
  }

  let l = i, r = arr.length-1;
  while (l < r) {
    const m = Math.floor((l+r)/2);
    if (arr[m].start >= arr[i].end) {
      r = m - 1;
    } else {
      l = m + 1;
    }
  }

  if (l === i) {
    // no "right-interval" found
    return -1;
  }

  if (arr[i].end > arr[l].start) {
    for (let j = l+1; j < arr.length; j++) {
      if (arr[i].end <= arr[j].start) {
        return j;
      }
    }
  }

  return l
}
