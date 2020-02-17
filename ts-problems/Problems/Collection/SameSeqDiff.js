"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var SameSeqDiff = /** @class */ (function () {
    function SameSeqDiff() {
    }
    SameSeqDiff.prototype.genTestCase = function (caseNum) {
        var data;
        var result;
        switch (caseNum) {
            case 1:
                data = [2, 1];
                result = [
                    10,
                    12,
                    21,
                    23,
                    32,
                    34,
                    43,
                    45,
                    54,
                    56,
                    65,
                    67,
                    76,
                    78,
                    87,
                    89,
                    98
                ];
            default:
                data = [3, 7];
                result = [181, 292, 707, 818, 929];
        }
        return Executor_1.TestCaseFactory(data, result);
    };
    SameSeqDiff.prototype.make = function (caseNum, debug) {
        var testCase = this.genTestCase(caseNum);
        this.n = testCase.data[0];
        this.k = testCase.data[1];
    };
    SameSeqDiff.prototype.solve = function () {
        var ans = new Array();
        if (this.n === 1) {
            ans.push(0);
        }
        for (var i = 1; i <= 9; i++) {
            this.dfs(this.n - 1, i, ans);
        }
        console.log(ans);
    };
    SameSeqDiff.prototype.dfs = function (n, cur, ans) {
        if (n === 0) {
            ans.push(cur);
        }
        var l = cur % 10;
        if (l + this.k <= 9) {
            this.dfs(n - 1, cur * 10 + l + this.k, ans);
        }
        if (l - this.k >= 0 && this.k !== 0) {
            this.dfs(n - 1, cur * 10 + l - this.k, ans);
        }
    };
    return SameSeqDiff;
}());
exports.SameSeqDiff = SameSeqDiff;
