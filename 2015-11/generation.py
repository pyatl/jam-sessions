""" Implementation of a generation of cells for Conway's Game of Life 
    Author: JR Rickerson
    Written for Python 3
"""

GRID_INPUT = """20 20
....................
....................
....................
....................
..........***.......
.........*..***.....
..........***.......
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
...................."""


class Generation():
    def __init__(self, grid=None, rows=None, cols=None):
        self.cols = cols or 0
        self.rows = rows or 0
        self.grid = grid or [[0] * cols for r in range(rows)]

    @staticmethod
    def empty(rows, cols):
        """Create an generation of the specified size with no living cells."""
        grid = [[0] * cols for r in range(rows)]
        return Generation(grid, rows, cols)
        
    @staticmethod
    def parse(grid_string):
        """Parse a generation string in the format produced by __str__"""
        dimensions, *lines = grid_string.split('\n')
        rows, cols = [int(d) for d in dimensions.split()]
        grid = []
        for line in lines:
            data = line.replace('.', '0').replace('*', '1')
            row = [int(cell) for cell in data]
            grid.append(row)

        return Generation(grid, rows, cols)

    def __str__(self):
        """Output the generation in a string format suitable for file
        storage."""
        outstr = '{} {}\n'.format(self.rows, self.cols)
        rowstrs = []
        for row in self.grid:
            datastr = ''.join([str(c) for c in row])
            rowstrs.append(datastr.replace('0', '.').replace('1', '*'))

        return outstr + '\n'.join(rowstrs)

    def next(self):
        """Create a new Generation object, representing the next calculated
        generation of cells."""
        # Assume an all-dead grid
        next_grid = [[0] * self.cols for r in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cell((row, col))
                neighbors = self.cell_neighbors((row, col))
                live_count = sum([self.cell(n) for n in neighbors])
                # Conway's Rule #3
                if cell and live_count in [2, 3]:
                    next_grid[row][col] = 1
                # Conway's Rule #4
                elif not cell and live_count == 3:
                    next_grid[row][col] = 1

        nextgen = Generation(grid=next_grid, rows=self.rows, cols=self.cols)
        return nextgen

    def cell(self, coords):
        """Get the state of a cell at the specified coordinates (row, col)"""
        y, x = coords
        # If the cell is out of bounds, consider it dead.
        if x < 0 or x >= self.cols:
            return 0
        if y < 0 or y >= self.rows:
            return 0

        return self.grid[y][x]

    def cell_neighbors(self, coords):
        """Get a list of 8 neighbor coordinates from a cell's coordinates"""
        y, x = coords
        # Four orthogonal neighbors
        n, s, e, w = (y - 1, x), (y + 1, x), (y, x + 1), (y, x - 1)
        # Four diagonal neighbors
        nw, ne, sw, se = (n[0], n[1] - 1), (n[0], n[1] + 1), (s[0], s[1] - 1), (s[0], s[1] + 1)

        return [n, ne, e, se, s, sw, w, nw]


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 1
    g = Generation.parse(GRID_INPUT)
    print('Initial:')
    print(g)
    for i in range(n):
        g = g.next()
        print('Gen {}:'.format(i + 1))
        print(g)

