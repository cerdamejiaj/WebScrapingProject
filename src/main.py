import weatherData

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
