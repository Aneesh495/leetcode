class NeighborSum {
  late final List<List<int>> _grid;
  late final List<List<int>> _position;
  late final int _n;

  NeighborSum(List<List<int>> grid) {
    _grid = grid;
    _n = grid.length;
    _position = List.generate(_n * _n, (_) => [0, 0]);
    for (int r = 0; r < _n; r++) {
      for (int c = 0; c < _n; c++) {
        _position[grid[r][c]] = [r, c];
      }
    }
  }

  int _sum(int value, List<List<int>> directions) {
    final place = _position[value];
    int total = 0;
    for (final direction in directions) {
      final r = place[0] + direction[0];
      final c = place[1] + direction[1];
      if (r >= 0 && r < _n && c >= 0 && c < _n) {
        total += _grid[r][c];
      }
    }
    return total;
  }

  int adjacentSum(int value) {
    return _sum(value, [[1, 0], [-1, 0], [0, 1], [0, -1]]);
  }

  int diagonalSum(int value) {
    return _sum(value, [[1, 1], [1, -1], [-1, 1], [-1, -1]]);
  }
}