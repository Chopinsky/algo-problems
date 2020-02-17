const node = {
  val: null,
  next: null
};

const build = function(array) {
  let head = null;
  let curr = null;

  array.forEach(val => {
    let next = Object.assign({}, node);
    next.val = val;

    if (!curr) {
      head = next;
      curr = next;
    } else {
      curr.next = next;
      curr = next;
    }
  });

  return head;
};

const enumList = function(head) {
  let curr = head;
  while (curr) {
    console.log(`${curr.val} ->`);
    curr = curr.next;
  }
};

const split = function(head, count) {
  let curr = head;
  while (curr && count > 0) {
    curr = curr.next;
  }

  let rest = curr ? curr.next : null;
  if (curr) {
    curr.next = null;
  }

  return rest;
};

const merge = function(l1, l2) {
  let head = null;
  let tail = Object.assign({}, node);

  // merge the overlapped
  while (l1 && l2) {
    if (l1.val < l2.val) {
      tail.next = l1;
      l1 = l1.next;
    } else {
      tail.next = l2;
      l2 = l2.next;
    }

    tail = tail.next;
    if (!head) {
      head = tail;
    }
  }

  // append the rest
  tail.next = l1 ? l1 : l2;

  // exhuast the tail
  while (tail.next) {
    tail = tail.next;
  }

  return {
    head,
    tail
  };
};

const sort = function(list) {
  if (!list || !list.next) {
    return list;
  }

  let len = 0;
  let curr = list;

  while (curr) {
    curr = curr.next;
    len++;
  }

  console.log(len);

  let dummy = Object.assign({}, node);
  dummy.next = list;

  let l, r, tail;
  for (let n = 1; n < len; n <<= 1) {
    curr = dummy.next;
    tail = dummy;

    while (curr) {
      l = curr;
      r = split(l, n);
      curr = split(r, n);

      let merged = merge(l, r);

      tail.next = merged.head;
      tail = merged.tail;
    }
  }

  return dummy.next;
};

exports.run = function(test, debug) {
  let list = build(test);
  enumList(sort(list));
};
