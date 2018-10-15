import csv
f = open("/dcs/pg18/u1897477/Downloads/weather.csv","r")
weather_data = f.read()
weather_data = weather_data.split("\n")
spread = []
day = []
for i in weather_data[1:]:
    row = i.split(",")
    max_weather = int(row[1])
    min_weather = int(row[2])
    weather_spread = max_weather - min_weather
    spread.append(weather_spread)
for i in weather_data[1:]:
    x = i.split(",")
    dow = int(x[0])
    day.append(dow)
weather_dictionary = dict(zip(day,spread))
print(min(weather_dictionary.items(), key=lambda x: x[1]))
