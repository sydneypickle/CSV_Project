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


# -----------------FINAL CODE
import csv
from datetime import datetime

# AUTO INDEX SITKA
open_sitka_file = "sitka_weather_2018_simple.csv"

sitka_location_name = " "

with open(open_sitka_file) as s:
    csv_file = csv.reader(s)
    header_row = next(csv_file)

    print(header_row)
    date_index = header_row.index("DATE")
    high_index = header_row.index("TMAX")
    low_index = header_row.index("TMIN")
    name_index = header_row.index("NAME")

    s_dates = []
    s_highs = []
    s_lows = []

    for row in csv_file:
        try:
            high = int(row[high_index])
            low = int(row[low_index])
            converted_date = datetime.strptime(row[date_index], "%Y-%m-%d")
            sitka_location_name = row[name_index]
        except ValueError:
            print(f"Missing data for {converted_date}")
        else:
            s_dates.append(converted_date)
            s_highs.append(int(row[high_index]))
            s_lows.append(int(row[low_index]))

# AUTO INDEX DV
open_dv_file = "death_valley_2018_simple.csv"

dv_location_name = " "

with open(open_dv_file) as d:
    csv_file = csv.reader(d)
    header_row = next(csv_file)

    print(header_row)
    date_index = header_row.index("DATE")
    high_index = header_row.index("TMAX")
    low_index = header_row.index("TMIN")
    name_index = header_row.index("NAME")

    d_dates = []
    d_highs = []
    d_lows = []

    for row in csv_file:
        try:
            high = int(row[high_index])
            low = int(row[low_index])
            converted_date = datetime.strptime(row[date_index], "%Y-%m-%d")
            dv_location_name = row[name_index]
        except ValueError:
            print(f"Missing data for {converted_date}")
        else:
            d_dates.append(converted_date)
            d_highs.append(int(row[high_index]))
            d_lows.append(int(row[low_index]))

# CREATE PLOT
from matplotlib import pyplot as plt

fig, ax = plt.subplots(2)
plt.suptitle(
    f"Temperature comparison between {sitka_location_name} and {dv_location_name} \n",
    fontsize=12,
)
# SITKA PLOT
ax[0].plot(s_dates, s_highs, c="red")
ax[0].plot(s_dates, s_lows, c="blue")
ax[0].fill_between(s_dates, s_highs, s_lows, facecolor="blue", alpha=0.1)
ax[0].title.set_text(f"{sitka_location_name}")
# DV PLOT
ax[1].plot(d_dates, d_highs, c="red")
ax[1].plot(d_dates, d_lows, c="blue")
ax[1].fill_between(d_dates, d_highs, d_lows, facecolor="blue", alpha=0.1)
ax[1].title.set_text(f"{dv_location_name}")

# FORMAT
plt.xlabel(" ", fontsize=12)
fig.autofmt_xdate()
plt.tick_params(axis="both", which="major", labelsize=12)

plt.show()
