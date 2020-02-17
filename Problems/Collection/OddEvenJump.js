"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var OddEvenJump = /** @class */ (function () {
    function OddEvenJump() {
    }
    OddEvenJump.prototype.genTestCase = function (caseNum) {
        var data;
        var result;
        switch (caseNum) {
            case 1:
                data = [2, 3, 1, 1, 4];
                result = 3;
                break;
            case 2:
                data = [5, 1, 3, 4, 2];
                result = 3;
                break;
            default:
                data = [10, 13, 12, 14, 15];
                result = 2;
        }
        return Executor_1.TestCaseFactory(data, result);
    };
    OddEvenJump.prototype.make = function (caseNum, debug) {
        var test = this.genTestCase(caseNum);
        this.data = test.data;
        this.ans = test.target;
    };
    OddEvenJump.prototype.solve = function () {
        var dp = new Array(this.data.length);
        var map = {};
        var len = this.data.length;
        var res = 1;
        map[this.data[len - 1]] = len - 1;
        for (var i = 0; i < len; i++) {
            if (i === len - 1) {
                dp[i] = [1, 1];
            }
            else {
                dp[i] = [0, 0];
            }
        }
        for (var i = len - 2; i >= 0; i--) {
            var keys = Object.keys(map).map(function (val) { return parseInt(val); });
            var val = this.data[i];
            var upper = Number.MAX_VALUE;
            var lower = Number.MIN_VALUE;
            for (var j = 0; j < keys.length; j++) {
                if (keys[j] > lower && keys[j] < val) {
                    lower = keys[j];
                }
                else if (keys[j] < upper && keys[j] >= val) {
                    upper = keys[j];
                }
            }
            if (lower > Number.MIN_VALUE) {
                var lower_index = map[lower];
                dp[i][1] = dp[lower_index][0];
            }
            if (upper < Number.MAX_VALUE) {
                var upper_index = map[upper];
                dp[i][0] = dp[upper_index][1];
                if (dp[i][0] === 1) {
                    res++;
                }
            }
            map[this.data[i]] = i;
        }
        console.log("Possible routes: " + res);
        console.log("Expected routes: " + this.ans);
    };
    return OddEvenJump;
}());
exports.OddEvenJump = OddEvenJump;
