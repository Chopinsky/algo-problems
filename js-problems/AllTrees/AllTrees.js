const nodeTemplate = {
  value: 0,
  left: null,
  right: null
};

const trees = function(count) {
  if (count % 2 === 0) {
    console.error(
      "The sub-tree must have odd number of nodes to be a full binary tree..."
    );

    return null;
  }

  if (count === 1) {
    return [Object.create(nodeTemplate)];
  }

  let ans = [];
  for (let i = 1; i < count; i += 2) {
    let left = trees(i);
    let right = trees(count - i - 1);

    left.forEach(lNode => {
      right.forEach(rNode => {
        let root = Object.create(nodeTemplate);
        root.left = Object.create(lNode);
        root.right = Object.create(rNode);

        ans.push(root);
      });
    });
  }

  return ans;
};

const trees2 = function(count) {
  if (count % 2 === 0) {
    console.error(
      "The sub-tree must have odd number of nodes to be a full binary tree..."
    );

    return null;
  }

  return trees2Recursive(count, []);
};

const trees2Recursive = function(count, cache) {
  if (count % 2 === 0) {
    console.error(
      "The sub-tree must have odd number of nodes to be a full binary tree..."
    );

    return null;
  }

  if (cache && cache.length >= count && cache[count - 1].length > 0) {
    return cache[count - 1];
  }

  if (count === 1) {
    let ans = [[0, null, null]];
    cache[0] = ans;

    return ans;
  }

  let ans = [];
  for (let i = 1; i < count; i += 2) {
    let left = trees2Recursive(i, cache);
    let right = trees2Recursive(count - i - 1, cache);

    left.forEach(lArr => {
      right.forEach(rArr => {
        let result = [0];

        result.push(...lArr);
        result.push(...rArr);

        ans.push(result);
      });
    });
  }

  cache[count - 1] = ans;
  return ans;
};

const printTree = function(root) {
  if (root) {
    console.log(root.value);

    printTree(root.left);
    printTree(root.right);
  } else {
    console.log("null");
  }
};

module.exports = {
  trees,
  trees2,
  printTree
};
