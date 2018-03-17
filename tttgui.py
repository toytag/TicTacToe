import math, time
import tkinter as tk
import tkinter.messagebox
from tttcore import TTTcore

class TTTgui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.core = TTTcore()
        self.title('Tic-Tac-Toe Game')
        self.geometry('300x300+400+200')
        self.__create_canvas()
        self.__setup_chess_board()
        self.mainloop()

    def __create_canvas(self):
        self.canvas = tk.Canvas(self, bg='lightcyan', width=300, height=300)
        self.canvas.pack()

    def __setup_chess_board(self):
        self.canvas.create_line(100, 0, 100, 300, width=2)
        self.canvas.create_line(200, 0, 200, 300, width=2)
        self.canvas.create_line(0, 100, 300, 100, width=2)
        self.canvas.create_line(0, 200, 300, 200, width=2)
        self.canvas.bind('<Button-1>', self.__scheduler)
        self.canvas.bind('<Button-2>', self.__regret)

    def __draw_circle(self, event):
        if event.x >= 0 and event.y >= 0:
            i = math.floor(event.x/100)
            j = math.floor(event.y/100)
            if self.core.put_chess(i, j):
                return None
            x = i * 100 + 10
            y = j * 100 + 10
            self.canvas.create_oval(x, y, x+80, y+80, width=5, outline='#e59832', tag=str(self.core.counter)+'_')

    def __draw_cross(self, event):
        if event.x >= 0 and event.y >= 0:
            i = math.floor(event.x/100)
            j = math.floor(event.y/100)
            if self.core.put_chess(i, j):
                return None
            x = i * 100 + 15
            y = j * 100 + 15
            self.canvas.create_line(x, y, x+70, y+70, width=5, fill='#2585e5', tag=str(self.core.counter)+'_')
            self.canvas.create_line(x, y+70, x+70, y, width=5, fill='#2585e5', tag=str(self.core.counter)+'_')

    def __scheduler(self, event):
        if self.core.counter%2 == 0:
            self.__draw_circle(event)
        else:
            self.__draw_cross(event)
        if self.core.check():
            winner = 'circle win' if self.core.counter%2 == 1 else 'cross win'
            tkinter.messagebox.showinfo('WINNER', winner)
        elif self.core.counter == 9:
            tkinter.messagebox.showinfo('WINNER', 'Tie')

    def __regret(self, event):
        if self.core.history != []:
            self.core.chess_board[self.core.history.pop()] = 0
            self.canvas.delete(str(self.core.counter)+'_')
            self.core.counter -= 1


if __name__ == '__main__':
    game = TTTgui()
