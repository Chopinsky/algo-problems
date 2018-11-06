declare interface String {
  startsWith(this: string, str: string, pos?: number): boolean;
}

String.prototype.startsWith = function(
  this: string,
  str: string,
  pos: number = 0
) {
  if (this.length - pos < str.length) {
    return false;
  }

  return this.slice(pos, str.length) === str;
};
