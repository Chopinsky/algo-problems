const run = function(count, debug) {
  const prog = require("./AllTrees");
  let treeRoots = prog.trees(count);
  if (treeRoots) {
    let count = 1;
    treeRoots.forEach(root => {
      console.log(`\n+++ Tree ${count} +++\n`);
      prog.printTree(root);
      console.log("\n================\n");
      count++;
    });
  }
};

const run2 = function(count, debug) {
  const prog = require("./AllTrees");

  let start = new Date();
  let ans = prog.trees2(count);
  let diff = new Date() - start;

  if (count < 16) {
    let num = 1;
    ans.forEach(arr => {
      console.log(`\nTree #${num++}: `, arr);
    });
  } else {
    console.log(
      `\nToo man results, skipping display of every single one of them; Total trees count: ${
        ans.length
      }.`
    );
  }

  console.info(`Total run time: ${diff} ms.`);
};

module.exports = {
  run,
  run2
};
