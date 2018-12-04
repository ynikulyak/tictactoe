# -----------------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
#
# Date:       11/30/2018
# -----------------------------------------------------------------------------
'''
Tic-tac-toe game for two players: user and computer.
The players take turns marking the spaces in a 3×3 grid.
The player who succeeds in placing three marks in a horizontal, vertical, or
diagonal row wins the game.
The user is assigned one color and the computer is assigned another color.
The user always starts playing first.  The user marks a space on the grid by
clicking on that space.  That space is then colored with the user’s assigned
color.  The computer immediately plays its move by coloring an available space
with the other color.
The game goes on until one player has 3 colored spaces in a line.
The game can also end in a tie if the entire board is full and no player has
completed such a line.
The player is given the option to restart the game, at any point during a game
or after a win, a loss or a tie.
'''
import tkinter
import random


class Game(object):
    '''
    Enter the class docstring here
    '''

    # Add your class variables if needed here - square size, etc...)
    white = 'white'
    board = [['white', 'white', 'white'], ['white', 'white', 'white'], ['white', 'white', 'white']]
    tile_size = 100
    size = len(board)*len(board)


    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        self.color = self.white
        # create frame
        frame = tkinter.Frame(parent)
        # register it with a geometry manager
        frame.grid()

        # Create the restart button widget
        restart_button = tkinter.Button(frame, text="Restart", width=10,
                                        command=self.restart)
        # register it with a geometry manager
        #restart_button.bind("<Button-1>", self.restart)
        restart_button.grid()

        # Create a canvas widget
        self.canvas = tkinter.Canvas(parent, width=self.tile_size*3,
                                     height=self.tile_size*3)
        for row in range(3):
            for column in range(3):
                self.color = 'white'
                self.canvas.create_rectangle(
                                             self.tile_size * column,
                                             self.tile_size * row,
                                             self.tile_size * (column + 1),
                                             self.tile_size * (row + 1),
                                             fill=self.color)
        # when the user clicks on the canvas, we invoke self.play
        self.canvas.bind("<Button-1>", self.play)
        # register it with a geometry manager
        self.canvas.grid()

        self.labelText = ''
        # Create a label widget for the win/lose message
        self.label = tkinter.Label(parent, text=self.labelText)
        self.label.grid()

    def restart(self):
        self.label.config(text="                         ")
        # This method is invoked when the user clicks on the RESTART button.
        for shape in self.canvas.find_all():
            self.canvas.itemconfigure(shape, fill='white')

        for row in range(3):
            for col in range(3):
                self.board[row][col] = 'white'

    def play(self, event):

        # This method is invoked when the user clicks on a square.
        shape = self.canvas.find_closest(event.x, event.y)
        if self.canvas.itemcget(shape, "fill") == 'red' or self.canvas.itemcget(shape, "fill") == 'blue':
            self.canvas.unbind(event)

        elif self.canvas.itemcget(shape, "fill") == 'white':
            self.canvas.itemconfigure(shape, fill='red')
            row = event.x // 100
            col = event.y // 100
            self.board[row][col] = 'red'
            self.size = self.size-1
            if self.size <= 1:
                self.label.config(text="Tie")
                self.canvas.unbind(event)

            while True:
                my_random_x = random.randint(0, self.tile_size * 3)
                my_random_y = random.randint(0, self.tile_size * 3)
                shape1 = self.canvas.find_closest(my_random_x, my_random_y)
                if shape != shape1 and self.canvas.itemcget(shape1, "fill") == self.white:
                    row1 = my_random_x // 100
                    col1 = my_random_y // 100
                    print(row1, col1)
                    self.board[row1][col1] = 'blue'
                    self.size = self.size - 1
                    self.canvas.itemconfigure(shape1, fill='blue')
                    break
                if self.size <= 1:
                    self.label.config(text="Tie")
                    self.canvas.unbind(event)
                    break

        if self.conditions():
            self.canvas.unbind(event)

    def conditions(self):
        if self.board[0][0] == 'red' and self.board[0][1] == 'red' and self.board[0][2] == 'red':
            self.label.config(text="You won")
            return True
        elif self.board[1][0] == 'red' and self.board[1][1] == 'red' and self.board[1][2] == 'red':
            self.label.config(text="You won")
            return True
        elif self.board[2][0] == 'red' and self.board[2][1] == 'red' and self.board[2][2] == 'red':
            self.label.config(text="You won")
            return True
        elif self.board[0][0] == 'red' and self.board[1][1] == 'red' and self.board[2][2] == 'red':
            self.label.config(text="You won")
            return True
        elif self.board[0][2] == 'red' and self.board[1][1] == 'red' and self.board[2][0] == 'red':
            self.label.config(text="You won")
            return True
        elif self.board[0][0] == 'blue' and self.board[0][1] == 'blue' and self.board[0][2] == 'blue':
            self.label.config(text="You lose")
            return True
        elif self.board[1][0] == 'blue' and self.board[1][1] == 'blue' and self.board[1][2] == 'blue':
            self.label.config(text="You lose")
            return True
        elif self.board[2][0] == 'blue' and self.board[2][1] == 'blue' and self.board[2][2] == 'blue':
            self.label.config(text="You lose")
            return True
        elif self.board[0][0] == 'blue' and self.board[1][1] == 'blue' and self.board[2][2] == 'blue':
            self.label.config(text="You lose")
            return True
        elif self.board[0][2] == 'blue' and self.board[1][1] == 'blue' and self.board[2][0] == 'blue':
            self.label.config(text="You lose")
            return True
        return False


def main():
    # Instantiate a root window
    root = tkinter.Tk()
    # Instantiate a Game object
    game = Game(root)
    # Enter the main event loop
    root.mainloop()


if __name__ == '__main__':
    main()
