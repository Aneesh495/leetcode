
/**
 * Construct the rectangle with area equal to `area`
 * Return [L, W] where L >= W and L * W == area and L - W is minimal
 * @param {number} area
 * @return {number[]}
 */
var constructRectangle = function(area) {
  // Start from the integer square root of area
  // The closest factors to each other lie around sqrt(area)
  let w = Math.floor(Math.sqrt(area));

  // Move downward until we find a divisor
  while (area % w !== 0) {
    w -= 1;
  }

  // Compute the matching length
  const l = area / w;

  // Ensure L >= W as required
  return [l, w];
};
