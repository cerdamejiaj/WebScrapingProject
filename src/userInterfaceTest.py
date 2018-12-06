import tkinter
import csv

root = tkinter.Tk()
with open("../build/weather.csv", newline = "") as file:
    reader = csv.reader(file)
    r = 0
    for col in reader:
        c = 0
        for row in col:
            label = tkinter.Label(root, width = 30, height = 5, text = row, relief = tkinter.RIDGE)
            label.grid(row = r, column = c)
            c += 1
        r += 1
root.mainloop()
