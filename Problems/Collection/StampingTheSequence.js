"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var StampingTheSequence = /** @class */ (function () {
    function StampingTheSequence() {
    }
    StampingTheSequence.prototype.genTestCase = function (caseNum) {
        switch (caseNum) {
            case 1:
                return Executor_1.TestCaseFactory(["aabcaca", "abca"], [3, 0, 1]);
            case 2:
                return Executor_1.TestCaseFactory(["aaaaabc", "abc"], [0, 1, 2, 3, 4]);
            case 3:
                return Executor_1.TestCaseFactory(["eyeeye", "abc"], []);
            default:
                return Executor_1.TestCaseFactory(["ababc", "abc"], [0, 2]);
        }
    };
    StampingTheSequence.prototype.make = function (caseNum, debug) {
        var testCase = this.genTestCase(caseNum);
        this.debug = debug;
        this.target = testCase.data[0].split("");
        this.stamp = testCase.data[1].split("");
        this.answer = testCase.target;
        if (this.debug) {
            console.log(this.target);
            console.log(this.stamp);
        }
    };
    StampingTheSequence.prototype.solve = function () {
        if (this.target.length < this.stamp.length) {
            console.log("Target length must be longer than the stamp length");
            return;
        }
        if (this.target.length === this.stamp.length && !this.matchFrom(0)) {
            console.log("No match has been found");
            return;
        }
        var result = this.run();
        if (this.validate(this.target)) {
            console.log("Success! Index: [" + result + "]");
            console.log("Expected array: [" + this.answer + "]");
        }
        else {
            console.log("Unable to find the match!");
        }
    };
    StampingTheSequence.prototype.matchFrom = function (start) {
        if (this.stamp.length + start > this.target.length) {
            return false;
        }
        for (var i = 0; i < this.stamp.length; i++) {
            if (this.target[start + i] === "*" ||
                this.target[start + i] === this.stamp[i]) {
                continue;
            }
            else {
                return false;
            }
        }
        return true;
    };
    StampingTheSequence.prototype.maskFrom = function (start) {
        var count = 0;
        for (var i = 0; i < this.stamp.length; i++) {
            if (this.target[start + i] !== "*") {
                this.target[start + i] = "*";
                count++;
            }
        }
        return count;
    };
    StampingTheSequence.prototype.validate = function (result) {
        for (var i = 0; i < result.length; i++) {
            if (result[i] !== "*") {
                return false;
            }
        }
        return true;
    };
    StampingTheSequence.prototype.run = function () {
        var start = this.target.length - this.stamp.length;
        var count = 0;
        var result = [];
        var masked = {};
        var toContinue = true;
        while (toContinue) {
            toContinue = false;
            for (var i = start; i >= 0; i--) {
                if (masked[i]) {
                    continue;
                }
                if (this.matchFrom(i)) {
                    count += this.maskFrom(i);
                    result.push(i);
                    masked[i] = true;
                    toContinue = true;
                    if (this.debug) {
                        console.log("Mask at " + i + ": " + this.target + " with " + count);
                    }
                    if (count === this.target.length) {
                        return result.reverse();
                    }
                }
            }
        }
        return [];
    };
    return StampingTheSequence;
}());
exports.StampingTheSequence = StampingTheSequence;
