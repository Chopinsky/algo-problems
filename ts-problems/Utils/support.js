String.prototype.startsWith = function (str, pos) {
    if (pos === void 0) { pos = 0; }
    if (this.length - pos < str.length) {
        return false;
    }
    return this.slice(pos, str.length) === str;
};
