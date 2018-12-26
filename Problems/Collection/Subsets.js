"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var Subsets = /** @class */ (function () {
    function Subsets() {
    }
    Subsets.prototype.genTestCase = function (caseNum) {
        var data;
        var result;
        switch (caseNum) {
            case 1:
                data = [];
                result = "";
            default:
                data = [1, 2, 3];
                result = [[3], [2], [1], [1, 2, 3], [1, 3], [1, 2], [2, 3], []];
        }
        return Executor_1.TestCaseFactory(data, result);
    };
    Subsets.prototype.make = function (caseNum, debug) {
        var testCase = this.genTestCase(caseNum);
        this.result = new Array();
        this.nums = testCase.data;
        this.ans = testCase.target;
    };
    Subsets.prototype.solve = function () {
        for (var n = 0; n <= this.nums.length; n++) {
            this.dfs(n, 0, []);
        }
        if (this.result && this.result.length > 0) {
            this.result.forEach(function (ary) {
                console.log(ary);
            });
        }
    };
    Subsets.prototype.dfs = function (size, start, curr) {
        if (curr.length === size) {
            this.result.push(curr.slice());
            return;
        }
        for (var i = start; i < this.nums.length; i++) {
            curr.push(this.nums[i]);
            this.dfs(size, i + 1, curr);
            curr.pop();
        }
    };
    return Subsets;
}());
exports.Subsets = Subsets;
