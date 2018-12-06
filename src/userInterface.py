import tkinter
import csv

root = tkinter.Tk()
with open("../build/weather.csv", newline = "") as file:
    reader = csv.reader(file)
    r = 2
    for col in reader:
        c = 2
        for row in col:
            label = tkinter.Label(root, width = 25, height = 3, text = row, relief = tkinter.RIDGE)
            label.grid(row = r, column = c)
            c += 1
        r += 1
root.mainloop()
