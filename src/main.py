import weatherData
import tkinter
import csv


def main():
     soup = weatherData.getPageRequest()
     seven_day = weatherData.weeklyWeather(soup)
     periods = weatherData.weekdays(seven_day)
     short_descs = weatherData.getShortDescription(seven_day)
     temps = weatherData.getTemp(seven_day)
     # descs = weatherData.getDescription(seven_day)
     weatherData.createTable(periods, short_descs, temps)
     # weatherData.importData()

if __name__ == '__main__':

    main()
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
