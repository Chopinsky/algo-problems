"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var LargestCommonFactor = /** @class */ (function () {
    function LargestCommonFactor() {
        this._factors = {};
        this._store = new Array();
    }
    LargestCommonFactor.prototype.genTestCase = function (caseNum) {
        switch (caseNum) {
            case 1:
                return Executor_1.TestCaseFactory([9, 20, 50, 63], 2);
            case 2:
                return Executor_1.TestCaseFactory([2, 3, 4, 6, 7, 12, 21, 39], 8);
            default:
                return Executor_1.TestCaseFactory([4, 6, 15, 35], 4);
        }
    };
    LargestCommonFactor.prototype.make = function (caseNum, debug) {
        var _this = this;
        var testCase = this.genTestCase(caseNum);
        if (!testCase || !testCase.data) {
            console.error("Unable to generate test cases...");
            return;
        }
        this._data = testCase.data;
        this._answer = testCase.target;
        this._dsu = new Array(this._data.length);
        for (var i = 0; i < this._data.length; i++) {
            this._dsu[i] = i;
        }
        this._data
            .sort(function (a, b) {
            return a - b;
        })
            .forEach(function (val, idx) {
            var factors = _this.findFactors(val);
            if (factors.length > 0) {
                factors.forEach(function (factor) {
                    if (!_this._factors.hasOwnProperty(factor)) {
                        _this._factors[factor] = new Array();
                    }
                    _this._factors[factor].push(idx);
                });
            }
            _this._store.push(factors);
        });
        if (debug) {
            console.log(this._factors);
            console.log(this._store);
            console.log(this._dsu);
        }
    };
    LargestCommonFactor.prototype.solve = function () {
        // let dyes: number[] = new Array(this._data.length);
        // let group = 1;
        var _this = this;
        var ans = 1;
        var c = {};
        this._data.forEach(function (val) {
            var idx = _this.dsuFind(val);
            if (!c.hasOwnProperty(idx)) {
                c[idx] = 0;
            }
            c[idx] += 1;
            ans = Math.max(ans, c[idx]);
        });
        console.log("The answer is: " + ans);
        console.log("Expected answer is: " + this._answer);
    };
    LargestCommonFactor.prototype.findFactors = function (num, includeSelf) {
        if (includeSelf === void 0) { includeSelf = false; }
        if (num <= 0) {
            return [];
        }
        else if (num === 1) {
            return [num];
        }
        var bound = Math.floor(Math.sqrt(num));
        var result = includeSelf ? [1, num] : [];
        for (var i = 2; i <= bound; i++) {
            if (num % i === 0) {
                result.push(i);
                this.dsuUnion(num, i);
                var pair = num / i;
                if (i !== pair) {
                    result.push(pair);
                    this.dsuUnion(num, pair);
                }
            }
        }
        return result.sort(function (a, b) {
            return a - b;
        });
    };
    LargestCommonFactor.prototype.dsuFind = function (x) {
        if (this._dsu[x] !== x) {
            this._dsu[x] = this.dsuFind(this._dsu[x]);
        }
        return this._dsu[x];
    };
    LargestCommonFactor.prototype.dsuUnion = function (x, y) {
        this._dsu[this.dsuFind(x)] = this._dsu[this.dsuFind(y)];
    };
    return LargestCommonFactor;
}());
exports.LargestCommonFactor = LargestCommonFactor;
