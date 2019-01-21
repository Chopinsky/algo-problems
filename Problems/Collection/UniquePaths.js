"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var UniquePaths = /** @class */ (function () {
    function UniquePaths() {
    }
    UniquePaths.prototype.genTestCase = function (caseNum) {
        var data;
        var result;
        switch (caseNum) {
            case 1:
                data = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]];
                result = 4;
            default:
                data = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]];
                result = 2;
        }
        return Executor_1.TestCaseFactory(data, result);
    };
    UniquePaths.prototype.make = function (caseNum, debug) {
        var test = this.genTestCase(caseNum);
        this.map = test.data;
        this.ans = test.target;
        this.m = this.map.length;
        this.n = this.map[0].length;
        this.dp = new Array(this.m);
        var size = Math.pow(2, this.m * this.n);
        for (var i = 0; i < this.m; i++) {
            this.dp[i] = new Array(this.n);
            for (var j = 0; j < this.n; j++) {
                this.dp[i][j] = new Array(size);
            }
        }
    };
    UniquePaths.prototype.solve = function () {
        var state = 0;
        var sx = -1;
        var sy = -1;
        for (var y = 0; y < this.m; y++) {
            for (var x = 0; x < this.n; x++) {
                if (this.map[y][x] === 0 || this.map[y][x] === 2) {
                    state += this.calcKey(x, y);
                }
                else if (this.map[y][x] === 1) {
                    sx = x;
                    sy = y;
                }
            }
        }
        var res = this.dfs(sx, sy, state);
        console.log("The final count of possible paths are: " + res);
        console.log("Expected count of possible paths are: " + this.ans);
    };
    UniquePaths.prototype.dfs = function (x, y, state) {
        if (!!this.dp[y][x][state]) {
            return this.map[y][x][state];
        }
        if (this.map[y][x] === 2) {
            return state === 0;
        }
        var paths = 0;
        var dirs = [-1, 0, 1, 0, -1];
        for (var i = 0; i < 4; i++) {
            var tx = x + dirs[i];
            var ty = y + dirs[i + 1];
            if (tx < 0 ||
                tx === this.n ||
                ty < 0 ||
                ty === this.m ||
                this.map[ty][tx] === -1) {
                continue;
            }
            var key = this.calcKey(tx, ty);
            if (!(state & key)) {
                // opposite states, pass
                continue;
            }
            paths += this.dfs(tx, ty, state ^ key);
        }
        this.dp[y][x][state] = paths;
        return this.dp[y][x][state];
    };
    UniquePaths.prototype.calcKey = function (x, y) {
        return Math.pow(2, y * this.n + x);
    };
    return UniquePaths;
}());
exports.UniquePaths = UniquePaths;
