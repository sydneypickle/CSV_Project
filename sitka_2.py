import csv
from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

##The enumerate() function returns both the index of each item &
# the value of each item as you loop through a list


for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs = []
dates = []

# as an example
# mydate = "2018-07-01"
# converted_date = datetime.strptime(mydate, "%Y-%m-%d")

# print(converted_date)

# we call the method strptime() using the string containing the date we want to work with
#  as its first argument. the 2nd argument tells python how the date is formatted.  in this examp,
#  python interprets '%Y-' to mean the part of the string before the first dash is a 4digit yr;
#  '%m-' means the part of the string before the 2nd dash is the num representing the month;
# & '%d' means the last part of the string is the day of the month, from 1-31

for row in csv_file:
    highs.append(int(row[5]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)

# print(highs)


# plot highs on a chart


import matplotlib.pyplot as plt


# Matplotlib's pyplot API has a conveneince function called subplots...

# ax = plt.subplots()


fig = plt.figure()

plt.plot(dates, highs, c="red")

# the call to fig.autofmt_xdate() draws the date
# labels diagonally to prevent them from overlapping

fig.autofmt_xdate()

plt.title("Dailey high temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)
# ^^ by default it gives you major so you dont have to write it but i leave there for help

plt.show()
