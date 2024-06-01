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
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for c in range(self._num_cols):
            col = []
            for r in range(self._num_rows):
                cell = Cell(self._win)
                col.append(cell)
            self._cells.append(col)

        for c in range(self._num_cols):
            for r in range(self._num_rows):
                self._draw_cell(c, r)
                

    def _draw_cell(self, c, r):
        if self._win is None:
            return
        cell = self._cells[c][r]
        x1 = c * self._cells_size_x + self._x1
        y1 = r * self._cells_size_y + self._y1
        x2 = c * self._cells_size_x + self._x1 + self._cells_size_x
        y2 = r * self._cells_size_y + self._y1 + self._cells_size_y
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
        c = self._num_cols - 1
        r = self._num_rows - 1
        exit = self._cells[c][r]
        exit.has_bottom_wall = False
        self._draw_cell(c, r)

    def _break_walls_r(self, c, r):
        curr = self._cells[c][r]
        curr.visited = True
        while True:
            to_visit = []
            if c > 0 and not self._cells[c - 1][r].visited:
                to_visit.append((c - 1, r))
            if c < self._num_cols - 1 and not self._cells[c + 1][r].visited:
                to_visit.append((c + 1, r))
            if r > 0 and not self._cells[c][r - 1].visited:
                to_visit.append((c, r - 1))
            if r < self._num_rows - 1 and not self._cells[c][r + 1].visited:
                to_visit.append((c, r + 1))
            
            if len(to_visit) == 0:
                self._draw_cell(c, r)
                return
            
            dir = to_visit[random.randrange(len(to_visit))]
            next = self._cells[dir[0]][dir[1]]

            if dir[0] == c - 1:
                next.has_right_wall = False
                curr.has_left_wall = False
            elif dir[0] == c + 1:
                next.has_left_wall = False
                curr.has_right_wall = False
            elif dir[1] == r + 1:
                next.has_top_wall = False
                curr.has_bottom_wall = False
            elif dir[1] == r - 1:
                next.has_bottom_wall = False
                curr.has_top_wall = False

            self._break_walls_r(dir[0], dir[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for  cell in col:
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, c, r):
        self._animate()
        current = self._cells[c][r]
        current.visited = True
       
        if c == self._num_cols - 1 and r == self._num_rows - 1:
             return True
    
        if c > 0:
            left = self._cells[c - 1][r]
            if not current.has_left_wall and left.visited == False:
                current.draw_move(left)
                if self._solve_r(c - 1, r):
                    return True
                else:
                    current.draw_move(left, True)
        if c < self._num_cols - 1:
            right = self._cells[c + 1][r]
            if not current.has_right_wall and right.visited == False:
                current.draw_move(right)
                if self._solve_r(c + 1, r):
                    return True
                else:
                    current.draw_move(right, True)
       
        if r > 0:
            up = self._cells[c][r - 1]
            if not current.has_top_wall and up.visited == False:
                current.draw_move(up)
                if self._solve_r(c, r - 1):
                    return True
                else:
                    current.draw_move(up, True)
        if  r < self._num_rows - 1: 
            down = self._cells[c][r + 1]
            if not current.has_bottom_wall and down.visited == False:
                current.draw_move(down)
                if self._solve_r(c, r + 1):
                    return True
                else:
                    current.draw_move(down, True)
        
        return False
       
            
            

            

