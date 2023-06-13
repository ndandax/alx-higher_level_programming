#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (w === 0 || h === 0 || h < 0 || w < 0) {
      const emptyObject = Object.create(null);
      this.emptyObject = emptyObject;
    }
  }
}
module.exports = Rectangle;
