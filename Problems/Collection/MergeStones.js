"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var MergeStones = /** @class */ (function () {
    function MergeStones() {
    }
    MergeStones.prototype.genTestCase = function (caseNum) {
        var data;
        var result;
        switch (caseNum) {
            case 1:
                data = [[3, 2, 4, 1], [3]];
                result = -1;
                break;
            case 2:
                data = [[3, 5, 1, 2, 6], [3]];
                result = 25;
                break;
            default:
                data = [[3, 2, 4, 1], [2]];
                result = 20;
        }
        return Executor_1.TestCaseFactory(data, result);
    };
    MergeStones.prototype.make = function (caseNum, debug) {
        var test = this.genTestCase(caseNum);
        this.data = test.data[0];
        this.step = test.data[1][0];
        this.result = test.target;
        this.debug = debug;
    };
    MergeStones.prototype.solve = function () {
        var answer = this.merge();
        console.log("Calculated result: " + answer);
        console.log("Expected result: " + this.result);
    };
    MergeStones.prototype.merge = function () {
        if ((this.data.length - 1) % (this.step - 1) !== 0) {
            return -1;
        }
        var total = 0;
        while (this.data.length >= this.step) {
            var sum = this.data
                .slice(0, this.step)
                .reduce(function (sum, curr) { return sum + curr; }, 0);
            var min = sum;
            var pos = [0];
            for (var i = this.step; i < this.data.length; i++) {
                // use sliding window to find the smallest consecutive-k subarray
                sum = sum + this.data[i] - this.data[i - this.step];
                if (this.debug) {
                    console.log(this.data + " with " + min + ", @ " + i + " = " + sum + " (+" + this.data[this.step] + " - " + this.data[i - this.step] + ")");
                }
                if (sum < min) {
                    pos = [i - this.step + 1];
                    min = sum;
                }
                else if (sum === min) {
                    pos.push(i - this.step + 1);
                }
            }
            for (var j = pos.length - 1; j >= 0; j--) {
                if (j === pos.length - 1 || pos[j] + this.step <= pos[j + 1]) {
                    total += this.updateDataArray(pos[j]);
                }
            }
        }
        if (this.data.length === 1) {
            return total;
        }
        else {
            return -1;
        }
    };
    MergeStones.prototype.updateDataArray = function (index) {
        var elem = this.data
            .slice(index, index + this.step)
            .reduce(function (sum, curr) { return sum + curr; }, 0);
        this.data = this.data.slice(0, index).concat([
            elem
        ], this.data.slice(index + this.step));
        if (this.debug) {
            console.log("Index: " + index + ", Length: " + this.data);
        }
        return elem;
    };
    return MergeStones;
}());
exports.MergeStones = MergeStones;
