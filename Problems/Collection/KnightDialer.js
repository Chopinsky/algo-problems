"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var ROW = 4;
var COLUMN = 3;
var boardMap = [
    [[1, 0], [1, 2]],
    [[1, 2], [2, 1]],
    [[2, 0], [2, 2]],
    [[1, 0], [2, 1]],
    [[0, 2], [2, 2], [3, 1]],
    [],
    [[0, 0], [2, 0], [3, 1]],
    [[0, 1], [1, 2]],
    [[0, 0], [0, 2]],
    [[0, 1], [1, 0]]
];
var KnightDialer = /** @class */ (function () {
    function KnightDialer() {
    }
    KnightDialer.prototype.make = function (caseNum, debug) {
        this._testCase = this.genTestCase(caseNum);
        this._debug = debug;
    };
    KnightDialer.prototype.solve = function () {
        var steps = this._testCase.data[0];
        if (steps <= 0) {
            console.error("Unable to initialize the DP array: expecting more than 1 step, but get " + steps);
        }
        var dp = this.initAry(steps);
        if (dp === null || dp.length === 0) {
            console.error("Unable to initialize the DP array: expecting more than 1 step, but get " + steps);
        }
        var _loop_1 = function (k) {
            var _loop_2 = function (i) {
                var _loop_3 = function (j) {
                    dp[k][i][j] = 0;
                    var lastMoves = this_1.lastMoves(i, j);
                    if (lastMoves && lastMoves.length > 0) {
                        lastMoves.forEach(function (board) {
                            var lastMove = dp[k - 1][board[0]][board[1]];
                            dp[k][i][j] += typeof lastMove === "number" ? lastMove : 0;
                        });
                    }
                };
                for (var j = 0; j < COLUMN; j++) {
                    _loop_3(j);
                }
            };
            for (var i = 0; i < ROW; i++) {
                _loop_2(i);
            }
        };
        var this_1 = this;
        for (var k = 1; k < steps; k++) {
            _loop_1(k);
        }
        var ans = 0;
        dp[steps - 1].forEach(function (board) {
            if (Array.isArray(board) && board.length > 0) {
                board.forEach(function (count) {
                    ans += count;
                });
            }
        });
        console.log("Unique numbers are: " + ans);
        console.log("Expected numbers are: " + this._testCase.target);
    };
    KnightDialer.prototype.genTestCase = function (caseNum) {
        switch (caseNum) {
            case 1:
                return Executor_1.TestCaseFactory([2], 20);
            case 2:
                return Executor_1.TestCaseFactory([3], 46);
            default:
                return Executor_1.TestCaseFactory([1], 10);
        }
    };
    KnightDialer.prototype.initAry = function (steps) {
        if (steps <= 0) {
            return null;
        }
        var dp = new Array(steps);
        for (var k = 0; k < steps; k++) {
            dp[k] = new Array(ROW);
            for (var i = 0; i < ROW; i++) {
                dp[k][i] = new Array(COLUMN);
                if (k === 0) {
                    for (var j = 0; j < COLUMN; j++) {
                        if (i === 3 && (j === 0 || j === 2)) {
                            dp[0][i][j] = 0;
                        }
                        else {
                            dp[0][i][j] = 1;
                        }
                    }
                }
            }
        }
        return dp;
    };
    KnightDialer.prototype.lastMoves = function (row, column) {
        var num = this.boardToNum(row, column);
        if (num === undefined) {
            return [];
        }
        return boardMap[num];
    };
    KnightDialer.prototype.boardToNum = function (row, column) {
        if (row >= ROW || column >= COLUMN) {
            return undefined;
        }
        if (row === 3) {
            if (column === 1) {
                return 0;
            }
            else {
                return undefined;
            }
        }
        return row * 3 + column + 1;
    };
    return KnightDialer;
}());
exports.KnightDialer = KnightDialer;
