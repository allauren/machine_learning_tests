from graphics import *

def main():
    win = GraphWin("My Circle", 1000, 1000)
    c = Point(500,500)
    c.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()