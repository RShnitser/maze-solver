from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0, 50), Point(800, 50)), "black")
    win.wait_for_close()

main()
