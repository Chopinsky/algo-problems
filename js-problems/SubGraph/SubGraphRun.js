let prog = require("./SubGraph");

exports.run = function(testSet, debug) {
  return prog.init(testSet.edges, testSet.steps, testSet.nodes, debug);
};
