"""
Automatic Indexes: 
We hard coded the indexes corresponding to the TMIN and TMAX columns.  Use the header row to 
determine the indexes for these values, so your program can work for Sitka or Death Valley. 
Use the station name to automatically generate an appropriate title for your graph as well.

Create 2 subplot graphs in one visualization so you can see both graphs to compare side by side.

Matplotlib's pyplot API has a convenience function called subplots() which acts as a utility wrapper 
and helps in creating common layouts of subplots, including the enclosing figure object, in a single call.

# fig, ax = plt.subplots(2,2)  -  this will create a visualization with 2 charts on it
"""
import csv
from datetime import datetime

from matplotlib import pyplot as plt


def get_weather_data(file_name, dates, highs, lows, date_index, high_index, low_index):
    """Get the highs and lows from a data file."""
    with open(file_name) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, and high and low temperatures from this file.
        for row in reader:
            converted_date = datetime.strptime(row[date_index], "%Y-%m-%d")
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {converted_date}")
            else:
                dates.append(converted_date)
                highs.append(high)
                lows.append(low)


# Get weather data for Sitka.
file_name = "sitka_weather_2018_simple.csv"
dates, highs, lows = [], [], []
get_weather_data(file_name, dates, highs, lows, date_index=2, high_index=5, low_index=6)

# Plot Sitka weather data.
fig, ax = plt.subplots(2)
ax[0].plot(dates, highs, c="red")
ax[0].plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Get weather data for Death Valley.
file_name = "death_valley_2018_simple.csv"
dates, highs, lows = [], [], []
get_weather_data(file_name, dates, highs, lows, date_index=2, high_index=4, low_index=5)

# Add Death Valley data to current plot.
ax[1].plot(dates, highs, c="red")
ax[1].plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format
title = "Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US"
plt.title(title, fontsize=12)
plt.xlabel("", fontsize=12)
ax[0].set_title("SITKA AIRPORT, AK US", fontsize=12)
ax[1].set_title("DEATH VALLEY, CA US", fontsize=12)
fig.autofmt_xdate()
plt.ylabel("", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)
# plt.ylim(10, 130)

plt.show()
"""
fig, ax = plt.subplots(2, 2)
fig2, a = plt.subplots(2)

a[0].plot(dates, highs, c="red")
a[1].plot(dates, lows, c="blue")

plt.show()
"""

"""
file_name = "death_valley_2018_simple.csv"
file_name = "sitka_weather_2018_simple.csv"
place_name = ""
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print(header_row)
    date_index = header_row.index("DATE")
    high_index = header_row.index("TMAX")
    low_index = header_row.index("TMIN")
    name_index = header_row.index("NAME")

    # Get dates high & low
    dates = []
    highs = []
    lows = []
    for row in reader:
        # Grab the station name, if it's not already set.
        if not place_name:
            place_name = row[name_index]
            print(place_name)

        converted_date = datetime.strptime(row[date_index], "%Y-%m-%d")
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {converted_date}")
        else:
            dates.append(converted_date)
            highs.append(high)
            lows.append(low)


# Plot the high and low temperatures.
fig, a = plt.subplots(2)

fig, ax = plt.subplots()
ax.plot(dates, highs, c="red")
ax.plot(dates, lows, c="blue")

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot.
title = f"Daily high and low temperatures - 2018 at {place_name}"

plt.title(title, fontsize=16)
plt.xlabel("", fontsize=12)
###fig.autofmt_xdate(converted_date)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

ax[0].plot(dates, highs, c="red")
ax[1].plot(dates, lows, c="blue")

plt.show()



#original code
open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

print(type(header_row))


for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []
lows = []


for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)

# plot highs on a chart


# Matplotlib's pyplot API has a conveneince function called subplots...

# ax = plt.subplots()


fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")


# the call to fig.autofmt_xdate() draws the date
# labels diagonally to prevent them from overlapping


fig.autofmt_xdate()


# we pass fill_between() the list dates for the x-values & then the 2 y-value series highs & lows. The facecolor
# argument determines the color of the shaded region; we give it a low alpha value of 0.1 so the filled region
# connects the two data series w/out distracting from the info they represent

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)


plt.title("Dailey high & low temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)
# ^^ by default it gives you major so you dont have to write it but i leave there for help

plt.show()

# matplotlib's pyplot API has a convenience function called subplots() which acts as a utility wrapper &
# helps in creating common layouts of subplots, including the enclosing figure object in a single call.

fig2, a = plt.subplots(2, 2)

a[0].plot(dates, highs, c="red")
a[1].plot(dates, lows, c="blue")

plt.show()


# --------------------DEATH VALLEY ORIGINAL CODE------------------------

import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)
print(type(header_row))

##The enumerate() function returns both the index of each item &
# the value of each item as you loop through a list


for index, column_header in enumerate(header_row):
    print(index, column_header)


highs = []
dates = []
lows = []

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
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"missing data for {converted_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(converted_date)


# print(highs)


# plot highs on a chart


import matplotlib.pyplot as plt


# Matplotlib's pyplot API has a conveneince function called subplots...

# ax = plt.subplots()


fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")


# the call to fig.autofmt_xdate() draws the date
# labels diagonally to prevent them from overlapping


fig.autofmt_xdate()


# we pass fill_between() the list dates for the x-values & then the 2 y-value series highs & lows. The facecolor
# argument determines the color of the shaded region; we give it a low alpha value of 0.1 so the filled region
# connects the two data series w/out distracting from the info they represent

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)


plt.title("Dailey high & low temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)
# ^^ by default it gives you major so you dont have to write it but i leave there for help

plt.show()
"""
