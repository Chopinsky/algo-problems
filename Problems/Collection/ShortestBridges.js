"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var ShortestBridges = /** @class */ (function () {
    function ShortestBridges() {
        this.debug = false;
        this.queue = new Array();
    }
    ShortestBridges.prototype.solve = function () {
        var steps = this.findSteps();
        console.log("Steps to connect all the islands: " + steps);
        console.log("Expected steps: " + this.result + "\n");
    };
    ShortestBridges.prototype.make = function (caseNum, debug) {
        var testCase = this.genTestCase(caseNum);
        this.bridges = testCase.data;
        this.result = testCase.target;
        this.debug = debug;
        if (this.bridges.length === 0 || this.bridges[0].length === 0) {
            console.error("Wrong data set size for " + this.bridges);
            return;
        }
        var found = false;
        for (var i = 0; i < this.bridges.length && !found; i++) {
            for (var j = 0; j < this.bridges[0].length && !found; j++) {
                if (this.bridges[i][j]) {
                    this.dfs(j, i);
                    found = true;
                }
            }
        }
        if (this.debug) {
            console.log(this.queue);
        }
    };
    ShortestBridges.prototype.genTestCase = function (caseNum) {
        switch (caseNum) {
            case 1:
                return Executor_1.TestCaseFactory([
                    [1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1]
                ], 1);
            case 2:
                return Executor_1.TestCaseFactory([[0, 1, 0], [0, 0, 0], [0, 0, 1]], 2);
            default:
                return Executor_1.TestCaseFactory([[1, 0], [0, 1]], 1);
        }
    };
    ShortestBridges.prototype.dfs = function (x, y) {
        if (x < 0 ||
            y < 0 ||
            x >= this.bridges[0].length ||
            y >= this.bridges.length ||
            this.bridges[y][x] !== 1) {
            return;
        }
        this.bridges[y][x] = 2;
        this.queue.push([x, y]);
        this.dfs(x - 1, y);
        this.dfs(x + 1, y);
        this.dfs(x, y - 1);
        this.dfs(x, y + 1);
    };
    ShortestBridges.prototype.findSteps = function () {
        var steps = 0;
        var dirs = [0, 1, 0, -1, 0];
        while (this.queue.length > 0) {
            var len = this.queue.length;
            while (len > 0) {
                var x = this.queue[0][0];
                var y = this.queue[0][1];
                if (this.debug) {
                    console.log(this.queue);
                }
                this.queue.splice(0, 1);
                len--;
                for (var i = 0; i < 4; i++) {
                    var tx = x + dirs[i];
                    var ty = y + dirs[i + 1];
                    if (tx < 0 ||
                        ty < 0 ||
                        tx >= this.bridges[0].length ||
                        ty >= this.bridges.length ||
                        this.bridges[ty][tx] === 2) {
                        continue;
                    }
                    if (this.bridges[ty][tx] === 1) {
                        return steps;
                    }
                    this.bridges[ty][tx] = 2;
                    this.queue.push([ty, tx]);
                }
            }
            steps++;
        }
        return steps;
    };
    return ShortestBridges;
}());
exports.ShortestBridges = ShortestBridges;
