const binaryTree = require("./BinaryTree");

const run = function(set, debug) {
  let { preorder, postorder } = set;
  let root = binaryTree.rebuild(preorder, postorder);
  binaryTree.inorderTraversal(root);
};

module.exports = {
  run
};
