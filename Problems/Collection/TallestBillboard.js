"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var TallestBillboard = /** @class */ (function () {
    function TallestBillboard() {
    }
    TallestBillboard.prototype.genTestCase = function (caseNum) {
        var data;
        var result;
        switch (caseNum) {
            case 1:
                data = [];
                result = "";
            default:
                data = [1, 2, 3, 6];
                result = 6;
        }
        return Executor_1.TestCaseFactory(data, result);
    };
    TallestBillboard.prototype.make = function (caseNum, debug) {
        var testCase = this.genTestCase(caseNum);
        if (testCase) {
            this.rods = testCase.data.sort(function (a, b) { return a - b; });
            this.ans = testCase.target;
        }
        this.debug = debug;
        if (this.rods && this.rods.length > 0) {
            this.sum = this.rods.reduce(function (sum, curr) {
                return sum + curr;
            }, 0);
            this.dp = new Array(this.sum + 1);
            for (var i = 0; i < this.dp.length; i++) {
                this.dp[i] = i === 0 ? 0 : -1;
            }
            if (this.debug) {
                console.log("Rods: " + this.rods);
            }
        }
    };
    TallestBillboard.prototype.solve = function () {
        var rows = this.rods.length;
        for (var i = 0; i < rows; i++) {
            var curr = this.dp.map(function (val) { return val; });
            var rod = this.rods[i];
            for (var j = 0; j <= this.sum - rod; j++) {
                if (curr[j] < 0) {
                    continue;
                }
                var idxAdd = j + rod;
                var idxMinus = Math.abs(j - rod);
                this.dp[idxAdd] = Math.max(this.dp[idxAdd], curr[j]);
                this.dp[idxMinus] = Math.max(this.dp[idxMinus], curr[j] + Math.min(rod, j));
            }
        }
        console.log("Answer: " + this.dp[0]);
    };
    return TallestBillboard;
}());
exports.TallestBillboard = TallestBillboard;
