"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var compare = function (one, two) {
    return Math.abs(one - two) < Math.pow(10, -9);
};
var EqualRationalNumbers = /** @class */ (function () {
    function EqualRationalNumbers() {
        this.answer = false;
    }
    EqualRationalNumbers.prototype.genTestCase = function (caseNum) {
        var data;
        var result;
        switch (caseNum) {
            case 1:
                data = ["0.1666(6)", "0.166(66)"];
                result = true;
                break;
            case 2:
                data = ["0.9(9)", "1.0"];
                result = true;
                break;
            default:
                data = ["0.(52)", "0.5(25)"];
                result = true;
                break;
        }
        return Executor_1.TestCaseFactory(data, result);
    };
    EqualRationalNumbers.prototype.make = function (caseNum, debug) {
        var testCase = this.genTestCase(caseNum);
        this.first = testCase.data[0];
        this.second = testCase.data[1];
        this.answer = testCase.target;
    };
    EqualRationalNumbers.prototype.solve = function () {
        var f = this.parse(this.first);
        var s = this.parse(this.second);
        console.log("First: " + f + "; Second: " + s);
        console.log("Result: " + compare(f, s));
    };
    EqualRationalNumbers.prototype.parse = function (num) {
        if (num.length === 0 || num === ".") {
            return 0;
        }
        var dot = num.indexOf(".");
        var rStart = num.indexOf("(");
        var rEnd = num.lastIndexOf(")");
        var i = 0;
        var n = 0;
        var nLen = 0;
        var r = 0;
        var rLen = 0;
        if (dot < 0) {
            return parseInt(num);
        }
        else if (dot === num.length - 1) {
            return parseInt(num.substring(0, num.length - 1));
        }
        else if (dot > 0) {
            i = parseInt(num.substring(0, dot));
        }
        if (rStart > dot + 1) {
            var nStr = num.substring(dot + 1, rStart);
            nLen = nStr.length;
            n = parseInt(nStr);
        }
        if (rEnd > rStart + 1) {
            var rStr = num.substring(rStart + 1, rEnd);
            rLen = rStr.length;
            r = parseInt(rStr);
        }
        var nFactor = n === 0 ? 0 : n / Math.pow(10, nLen);
        var rFactor = r === 0 ? 0 : r / Math.pow(10, nLen) / (Math.pow(10, rLen) - 1);
        return i + nFactor + rFactor;
    };
    return EqualRationalNumbers;
}());
exports.EqualRationalNumbers = EqualRationalNumbers;
