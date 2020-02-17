"use strict";
exports.__esModule = true;
var ThreeSumMulti = /** @class */ (function () {
    function ThreeSumMulti() {
        this._combSet = {
            largest: -1
        };
        this.comb = function (n, k) {
            var key = n + "," + k;
            if (this._combSet[key]) {
                return this._combSet[key];
            }
            var top = n;
            for (var index = top - 1; index > n - k; index--) {
                top *= index;
            }
            var bottom = k;
            for (var index = k - 1; index > 0; index--) {
                bottom *= index;
            }
            this._combSet[key] = Math.floor(top / bottom);
            return this._combSet[key];
        };
    }
    ThreeSumMulti.prototype.make = function (caseNum, debug) {
        var _this = this;
        this._testCase = this.genTestCase(caseNum);
        this._debug = debug;
        if (this._testCase.data) {
            this._testCase.data.forEach(function (val) {
                if (_this._combSet[val]) {
                    _this._combSet[val] += 1;
                }
                else {
                    _this._combSet[val] = 1;
                }
                if (val > _this._combSet["largest"]) {
                    _this._combSet["largest"] = val;
                }
            });
        }
        if (this._debug) {
            console.log("Combo set -> " + this._combSet);
        }
    };
    ThreeSumMulti.prototype.solve = function () {
        var ans = 0;
        var target = this._testCase.target;
        for (var i = 0; i <= target; i++) {
            for (var j = i; j <= target; j++) {
                var k = target - i - j;
                if (k < 0 || k > this._combSet["largest"] || k < j) {
                    // 0 <= i <= j <= k <= upper bound
                    continue;
                }
                if (!this._combSet[i] || !this._combSet[j] || !this._combSet[k]) {
                    // the number is not in the provided array
                    continue;
                }
                if (i === j && j === k && this._combSet[i] >= 3) {
                    // (1, j, k) where all 3 numbers are the same
                    ans +=
                        ((this._combSet[i] - 2) *
                            (this._combSet[i] - 1) *
                            this._combSet[i]) /
                            6;
                }
                else if (i === j && j !== k && this._combSet[i] >= 2) {
                    // (i, i, k)
                    ans +=
                        (this._combSet[i] * (this._combSet[i] - 1) * this._combSet[k]) / 2;
                }
                else if (i !== j && j === k && this._combSet[j] >= 2) {
                    // (i, j, j)
                    ans +=
                        (this._combSet[i] * (this._combSet[j] - 1) * this._combSet[j]) / 2;
                }
                else {
                    // (i, j, k) are all different numbers
                    ans += this._combSet[i] * this._combSet[j] * this._combSet[k];
                }
            }
        }
        console.log("Solved -- combinations are " + ans);
    };
    ThreeSumMulti.prototype.genTestCase = function (caseNum) {
        var data = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5];
        var target = 8;
        switch (caseNum) {
            case 0:
                break;
            case 1:
                data = [1, 1, 2, 2, 2, 2];
                target = 5;
                break;
            default:
                break;
        }
        return {
            data: data,
            target: target
        };
    };
    return ThreeSumMulti;
}());
exports.ThreeSumMulti = ThreeSumMulti;
