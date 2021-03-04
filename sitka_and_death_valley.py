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
# -----------------NOT WORKING
"""
import csv
from datetime import datetime

from matplotlib import pyplot as plt


def get_weather_data(file_name, dates, highs, lows, date_index, high_index, low_index):
    # Get the highs and lows from a data file.
    with open(file_name) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        date_index = header_row.index("DATE")
        high_index = header_row.index("TMAX")
        low_index = header_row.index("TMIN")
        name_index = header_row.index("NAME")

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
get_weather_data(file_name, dates, highs, lows, date_index, high_index, low_index)

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
plt.ylim(10, 130)

# Format
title = "Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US"
plt.suptitle(title, fontsize=12)
plt.xlabel("", fontsize=12)
ax[0].set_title("SITKA AIRPORT, AK US", fontsize=12)
ax[1].set_title("DEATH VALLEY, CA US", fontsize=12)
fig.autofmt_xdate()
plt.ylabel("", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)
# plt.ylim(10, 130)

plt.show()

"""
# --------------------------------RUNS BUT DOES NOT HAVE AUTO INDEX--------------------------------------
import csv
from datetime import datetime

from matplotlib import pyplot as plt


def get_weather_data(file_name, dates, highs, lows, date_index, high_index, low_index):
    # Get the highs and lows from a data file.
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
ax[0].fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Get weather data for Death Valley.
file_name = "death_valley_2018_simple.csv"
dates, highs, lows = [], [], []
get_weather_data(file_name, dates, highs, lows, date_index=2, high_index=4, low_index=5)

# Add Death Valley data to current plot.
ax[1].plot(dates, highs, c="red")
ax[1].plot(dates, lows, c="blue")
ax[1].fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
plt.ylim(10, 130)

# Format
title = "Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US"
plt.suptitle(title, fontsize=12)
plt.xlabel("", fontsize=12)
ax[0].set_title("SITKA AIRPORT, AK US", fontsize=12)
ax[1].set_title("DEATH VALLEY, CA US", fontsize=12)
fig.autofmt_xdate()
plt.ylabel("", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)
# plt.ylim(10, 130)

plt.show()
