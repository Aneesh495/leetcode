
var canVisitAllRooms = function(rooms) {
  const n = rooms.length;
  const seen = new Array(n).fill(false);
  const stack = [0];
  seen[0] = true;
  let visited = 1;

  while (stack.length) {
    const room = stack.pop();
    for (const key of rooms[room]) {
      if (!seen[key]) {
        seen[key] = true;
        visited++;
        stack.push(key);
      }
    }
  }
  return visited === n;
};
