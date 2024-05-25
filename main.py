from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(50, 50, 100, 100)
    c2 = Cell(win)
    c2.draw(100, 50, 150, 100)
    c.draw_move(c2)
    
    win.wait_for_close()

main()
