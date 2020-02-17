"use strict";
exports.__esModule = true;
var DSU = /** @class */ (function () {
    function DSU(count) {
        if (count === void 0) { count = 1; }
        this.dsu = new Array(count);
        for (var i = 0; i < count; i++) {
            this.dsu[i] = i;
        }
    }
    DSU.prototype.find = function (x) {
        if (this.dsu[x] !== x) {
            this.dsu[x] = this.find(this.dsu[x]);
        }
        return this.dsu[x];
    };
    DSU.prototype.union = function (x, y) {
        this.dsu[this.find(x)] = this.dsu[this.find(y)];
    };
    DSU.prototype.merge = function (x, y) {
        this.dsu[this.find(x)] = this.find(y);
    };
    DSU.prototype.debug = function () {
        console.log(this.dsu);
    };
    return DSU;
}());
exports["default"] = DSU;
