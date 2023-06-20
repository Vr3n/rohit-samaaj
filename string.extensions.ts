interface String {
  titleCase(): string;
}

String.prototype.titleCase = function () {
  let upper = true;
  let newStr = "";
  for (let i = 0, l = this.length; i < l; i++) {
    if (this[i] == " ") {
      upper = true;
      newStr += this[i];
      continue;
    }
    newStr += upper ? this[i]?.toUpperCase() : this[i]?.toLowerCase();
    upper = false;
  }
  return newStr;
};
