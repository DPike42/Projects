import tkinter as tk

def main():
  pass


def displayBoard():
  root = tk.Tk()
  logo = tk.PhotoImage(file="chessboard.gif")
  w1 = tk.Label(root, text = "C  H  E  S  S     U   L  T  R  A ").pack()
  w2 = tk.Label(root, image = logo).pack()

  w3 = tk.Label(root, justify = tk.LEFT, padx = 400, pady = 20).pack(side = "left")

  root.mainloop()

displayBoard()
