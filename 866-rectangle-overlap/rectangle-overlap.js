
var isRectangleOverlap = function(rec1, rec2) {
  const [x1, y1, x2, y2] = rec1;
  const [a1, b1, a2, b2] = rec2;
  return !(x2 <= a1 || a2 <= x1 || y2 <= b1 || b2 <= y1);
};
