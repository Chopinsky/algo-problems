const rebuild = function(preorder, postorder) {
  if (
    !Array.isArray(preorder) ||
    !Array.isArray(postorder) ||
    preorder.length !== postorder.length
  ) {
    console.error(
      "Pre-order traversal array and postorder traversal array must have same length"
    );

    return null;
  }

  if (preorder.length === 0) {
    return null;
  }

  if (preorder[0] !== postorder[postorder.length - 1]) {
    console.error(
      `The input arrays are incoherent:\nPre: ${preorder.toString()}\nPost: ${postorder.toString()}`
    );
    return null;
  }

  // step 1: remove the root value from the arrays
  let value = postorder.pop();
  preorder.splice(0, 1);

  let root = {
    value,
    left: null,
    right: null
  };

  // if the arrays are empty now, we're done.
  if (preorder.length === 0) {
    return root;
  }

  // step 2: find the subarray for the subtree
  const leftRootValue = preorder[0];
  let index = 0;

  while (index < postorder.length) {
    if (postorder[index] === leftRootValue) {
      // the index of the root value in the post-order array
      break;
    }

    index++;
  }

  const leftPreSubarr = preorder.splice(0, index + 1);
  const leftPostSubarr = postorder.splice(0, index + 1);

  root.left = rebuild(leftPreSubarr, leftPostSubarr);
  root.right = rebuild(preorder, postorder);

  return root;
};

const preTraversal = function(root) {
  if (!root) {
    return;
  }

  console.log(root.value);
  preTraversal(root.left);
  preTraversal(root.right);
};

const postTraversal = function(root) {
  if (!root) {
    return;
  }

  postTraversal(root.left);
  postTraversal(root.right);
  console.log(root.value);
};

const inorderTraversal = function(root) {
  if (!root) {
    return;
  }

  inorderTraversal(root.left);
  console.log(root.value);
  inorderTraversal(root.right);
};

module.exports = {
  rebuild,
  preTraversal,
  inorderTraversal,
  postTraversal
};
