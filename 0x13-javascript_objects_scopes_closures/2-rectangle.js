#!/usr/bin/node
// 2-rectangle.js

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // Create an empty object
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
