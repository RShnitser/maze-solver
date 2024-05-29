from cell import Cell
import time
import random

class Maze:
    def __init__(self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
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

        if seed is not None:
            random.seed(seed)

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
        if self._win is None:
            return
        cell = self._cells[c][r]
        x1 = r * self._cells_size_x + self._x1
        y1 = c * self._cells_size_y + self._y1
        x2 = r * self._cells_size_x + self._x1 + self._cells_size_x
        y2 = c * self._cells_size_y + self._y1 + self._cells_size_y
        cell.draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        self._draw_cell(0, 0)
        c = len(self._cells) - 1
        r = len(self._cells[0]) - 1
        exit = self._cells[c][r]
        exit.has_bottom_wall = False
        self._draw_cell(r, c)

    def _break_walls_r(self, r, c):
        curr = self._cells[c][r]
        curr.visited = True
        while True:
            to_visit = []
            if c > 0:
                if not self._cells[c - 1][r].visited:
                    to_visit.append((c - 1, r))
            if c < self._num_cols - 1:
                if not self._cells[c + 1][r].visited:
                    to_visit.append((c + 1, r))
            if r > 0:
                if not self._cells[c][r - 1].visited:
                    to_visit.append(c, r - 1)
            if r < self._num_rows - 1:
                if not self._cells[c][r + 1].visited:
                    to_visit.append(c, r + 1)
            
            if len(to_visit) == 0:
                self._draw_cell(r, c)
                return
            
            dir = to_visit[random.randrange(0, len(to_visit))]
            next = self._cells[dir[0]][dir[1]]
            if dir[0] < c:
                next.has_right_wall = False
                curr.has_left_wall = False
            elif dir[0] > c:
                next.has_left_wall = False
                curr.has_right_wall = False
            elif dir[1] < r:
                next.has_bottom_wall = False
                curr.has_top_wall = False
            elif dir[1] > r:
                next.has_top_wall = False
                curr.has_bottom_wall = False

            self._break_walls_r(dir[1], dir[0])
            
            

            

