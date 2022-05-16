from tkinter import Button
import random


# Creating a class: A blueprint from which objects are created....in this instance, the button object
import settings


class Cell:
    # Creating an array for all of our cells
    all = []

    # Defining what each of our cells has
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Appending the object to the Cell.all list
        Cell.all.append(self)

    # Creating the button(cell) object
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=5,
            text=f'{self.x}, {self.y}'
        )
        # Binding different actions to the buttons
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)

        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

        print("Left click")
        print(f'Cell({self.x}, {self.y})')
        print(f'Cell{self.is_mine}')

    def right_click_actions(self, event):
        print("Right click")
        print(f'Cell({self.x}, {self.y})')

    def show_mine(self):
        #Interupt game and show player lost
        self.cell_btn_object.config(
            bg='red'
        )

    def show_cell(self):
        self.cell_btn_object.config(
            bg='green'
        )

    @staticmethod
    def randomize_mines():
        mines = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for mines in mines:
            mines.is_mine = True
        print(Cell.all)

    # This returns a string of the object example [Cell(5,4)]
    def __repr__(self):
        return f'Cell({self.x}, {self.y})'
