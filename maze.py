from cell import Cell
import time

class Maze:
    def __init__(self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cells_size_x = cell_size_x
        self._cells_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for c in range(self._num_cols):
            col = []
            for r in range(self._num_rows):
                cell = Cell(self._win)
                col.append(cell)
            self._cells.append(col)

        for c in range(self._num_cols):
            for r in range(self._num_rows):
                self._draw_cell(r, c)
                

    def _draw_cell(self, r, c):
        cell = self._cells[c][r]
        x1 = r * self._cells_size_x + self._x1
        y1 = c * self._cells_size_y + self._y1
        x2 = r * self._cells_size_x + self._x1 + self._cells_size_x
        y2 = c * self._cells_size_y + self._y1 + self._cells_size_y
        cell.draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
