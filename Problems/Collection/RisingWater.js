"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var makeNode = function () {
    return {
        val: Number.MAX_VALUE,
        visited: false
    };
};
var RisingWater = /** @class */ (function () {
    function RisingWater() {
    }
    RisingWater.prototype.genTestCase = function (caseNum) {
        var data;
        var result;
        switch (caseNum) {
            case 1:
                data = [
                    [0, 1, 2, 3, 4],
                    [24, 23, 22, 21, 5],
                    [12, 13, 14, 15, 16],
                    [11, 17, 18, 19, 20],
                    [10, 9, 8, 7, 6]
                ];
                result = 16;
                break;
            default:
                data = [[0, 2], [1, 3]];
                result = 3;
        }
        return Executor_1.TestCaseFactory(data, result);
    };
    RisingWater.prototype.make = function (caseNum, debug) {
        var test = this.genTestCase(caseNum);
        this.data = test.data;
        this.result = test.target;
        this.debug = debug;
    };
    RisingWater.prototype.solve = function () {
        var _this = this;
        var len = this.data.length;
        var dp = new Array(len);
        for (var i = 0; i < len; i++) {
            dp[i] = new Array(len);
            for (var j = 0; j < len; j++) {
                dp[i][j] = makeNode();
            }
        }
        var queue = [];
        var currX = 0;
        var currY = 0;
        dp[0][0].val = this.data[0][0];
        queue.push([0, 0]);
        var _loop_1 = function () {
            var node = queue.splice(0, 1);
            currX = node[0][0];
            currY = node[0][1];
            dp[currX][currY].visited = true;
            var currVal = dp[currX][currY].val;
            var neighbors = this_1.neighbors(currX, currY);
            neighbors.forEach(function (coord) {
                var x = coord[0];
                var y = coord[1];
                if (dp[x][y].val === Number.MAX_VALUE || currVal < dp[x][y].val) {
                    // first visit or we have a better path
                    dp[x][y].val = Math.max(currVal, _this.data[x][y]);
                    if (!_this.isInQueue(queue, coord)) {
                        queue.push(coord);
                    }
                }
            });
            if (this_1.debug) {
                console.log("======= " + [currX, currY] + " =======");
                for (var i = 0; i < len; i++) {
                    var row = [];
                    for (var j = 0; j < len; j++) {
                        row.push(dp[i][j].val);
                    }
                    console.log(row);
                }
            }
        };
        var this_1 = this;
        while (queue.length > 0) {
            _loop_1();
        }
        console.log("Final val: " + dp[len - 1][len - 1].val);
        console.log("Expected val: " + this.result);
    };
    RisingWater.prototype.neighbors = function (x, y) {
        var neighbors = [];
        var boundary = this.data.length;
        if (x > 0) {
            neighbors.push([x - 1, y]);
        }
        if (x < boundary - 1) {
            neighbors.push([x + 1, y]);
        }
        if (y > 0) {
            neighbors.push([x, y - 1]);
        }
        if (y < boundary - 1) {
            neighbors.push([x, y + 1]);
        }
        return neighbors;
    };
    RisingWater.prototype.isInQueue = function (queue, coord) {
        for (var i = 0; i < queue.length; i++) {
            if (queue[i][0] === coord[0] && queue[i][1] === coord[1]) {
                return true;
            }
        }
        return false;
    };
    return RisingWater;
}());
exports.RisingWater = RisingWater;
