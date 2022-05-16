from tkinter import *
import settings
import util
from cell import Cell

root = Tk()
root.config(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
# Override the settings of the window
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='grey',  # Change later to black
    width=settings.WIDTH,
    height=util.height_prct(25)
)

top_frame.place(
    x=0, y=0
)

left_frame = Frame(
    root,
    bg='light grey',
    width=util.width_prct(25),
    height=util.height_prct(75)
)

left_frame.place(
    x=0, y=util.height_prct(25)
)

center_frame = Frame(
    root,
    bg='white',
    width=util.width_prct(75),
    height=util.height_prct(75)
)

center_frame.place(
    x=util.width_prct(25), y=util.height_prct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

Cell.randomize_mines()
for c in Cell.all:
    print(c.is_mine)


# Run the window
root.mainloop()