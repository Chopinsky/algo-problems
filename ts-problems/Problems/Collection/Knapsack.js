"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var Knapsack = /** @class */ (function () {
    function Knapsack() {
        this._testCase = null;
        this._debug = false;
    }
    Knapsack.prototype.solve = function () {
        if (!this._testCase) {
            console.error("No test case is valid or provided...");
            return;
        }
        var _a = this._testCase.data, itemVal = _a[0], itemWeight = _a[1], maxWeight = _a[2];
        var itemLen = itemVal.length;
        var maxVal = 0;
        for (var i = 1; i <= itemLen; i++) {
            var itemIndex = i - 1;
            for (var j = itemWeight[itemIndex]; j <= maxWeight; j++) {
                if (this._debug) {
                    console.log("dp[" + i + "][" + j + "] = " + this._dp[i - 1][j] + " vs. " + (this._dp[i - 1][j - itemWeight[itemIndex]] + itemVal[itemIndex]));
                }
                this._dp[i][j] = Math.max(this._dp[i - 1][j], this._dp[i - 1][j - itemWeight[itemIndex]] + itemVal[itemIndex]);
                if (i === itemLen && this._dp[i][j] > maxVal) {
                    maxVal = this._dp[i][j];
                }
            }
        }
        if (this._debug) {
            console.log("\n", this._dp, "\n");
        }
        console.log("The largest amount of values that can be placed in the pack is " + maxVal + "...\nExpected value is: " + this._testCase.target + "...\n      ");
    };
    Knapsack.prototype.make = function (caseNum, debug) {
        this._testCase = this.genTestCase(caseNum);
        if (this._testCase.data.length !== 3 ||
            !this._testCase.data[0] ||
            !this._testCase.data[1] ||
            this._testCase.data[0].length !== this._testCase.data[1].length) {
            console.error("Invalid test data: the weight and value array must have the same length: " + this._testCase.data[0].length + " vs. " + this._testCase.data[1].length);
            this._testCase = null;
            return;
        }
        var itemLen = this._testCase.data[0].length + 1;
        var weightLen = this._testCase.data[2] + 1;
        this._dp = new Array(itemLen);
        for (var i = 0; i < itemLen; i++) {
            this._dp[i] = new Array(weightLen);
            for (var j = 0; j < weightLen; j++) {
                this._dp[i][j] = 0;
            }
        }
    };
    Knapsack.prototype.genTestCase = function (caseNum) {
        switch (caseNum) {
            case 0:
            default:
                return Executor_1.TestCaseFactory([[1, 2, 4, 5], [1, 1, 2, 2], 4], 9);
        }
    };
    return Knapsack;
}());
exports.Knapsack = Knapsack;
