# (1) Create program to parse csv file to read the weather

## Import modules
import csv
import matplotlib.pyplot as plt
from datetime import datetime

## Identify file to read from
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'


## Open and parse through file
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	# print(header_row)

	## Loop through values one by one with enumerate method
	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)

	## Print the High Temperatures with Error Handling
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], '%Y-%m-%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date, 'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
	# print(highs)
	# print(dates)

## Configure Plot for High Temperatures
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates,highs, lows, facecolor='blue', alpha=0.1)



## Format Plot title and axis labels
plt.title('Daily High and Low Temperatures 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=10)

## Plot the high temperatures
plt.show()

## Practice with strptime funtion
# first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
# print(first_date)
