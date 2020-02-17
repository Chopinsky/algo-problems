"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var DistributingCoins = /** @class */ (function () {
    function DistributingCoins() {
    }
    DistributingCoins.prototype.genTestCase = function (caseNum) {
        var data;
        var result;
        switch (caseNum) {
            case 1:
                data = [0, 3, 0];
                result = 3;
                break;
            case 2:
                data = [1, 0, 2];
                result = 2;
                break;
            case 3:
                data = [1, 0, 0, 3];
                result = 4;
                break;
            default:
                data = [3, 0, 0];
                result = 2;
        }
        return Executor_1.TestCaseFactory(data, result);
    };
    DistributingCoins.prototype.make = function (caseNum, debug) {
        var test = this.genTestCase(caseNum);
        this.data = test.data;
        this.len = this.data.length;
        this.result = test.target;
        this.answer = 0;
    };
    DistributingCoins.prototype.solve = function () {
        // upside-down balancing... overall net-flow is 0.
        this.balance(0);
        console.log("Calculated steps: " + this.answer);
        console.log("Expected steps: " + this.result);
    };
    DistributingCoins.prototype.balance = function (node) {
        if (node >= this.len) {
            return 0;
        }
        // pre-iterating the tree, stored in the form of a balanced tree
        var left = 2 * node + 1 < this.len ? this.balance(2 * node + 1) : 0;
        var right = 2 * node + 2 < this.len ? this.balance(2 * node + 2) : 0;
        // answer is the flow required from or to the left and right branches to balance the tree
        this.answer += Math.abs(left) + Math.abs(right);
        // return the net-flow through this node, which is what to give/ask for from the parent
        return this.data[node] - 1 + left + right;
    };
    return DistributingCoins;
}());
exports.DistributingCoins = DistributingCoins;
