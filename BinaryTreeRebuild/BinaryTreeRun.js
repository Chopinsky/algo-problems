const binaryTree = require("./BinaryTree");

const run = function(preorder, postorder, debug) {
  let root = binaryTree.rebuild(preorder, postorder);
  binaryTree.inorderTraversal(root);
};

module.exports = {
  run
};
