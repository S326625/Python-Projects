# -*- coding: utf-8 -*-
"""
 By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Neela Rajesh
# Section:      213
# Assignment:   Lab 11-3: weather_data
# Date:         11/8/23

"""

weatherFile = open('WeatherDataCLL.csv', 'r')
weatherLines = weatherFile.read()

weatherList = weatherLines.split("\n")
weatherListNew = []

for i in range(1, len(weatherList)):
    weatherLine = weatherList[i]
    weatherLineList = weatherLine.split(",")
    weatherListNew.append(weatherLineList)


if weatherListNew[0][5].isdigit():
    max_temp = int(weatherListNew[0][5])
else:
    max_temp = 0

if weatherListNew[0][6].isdigit():
    min_temp = int(weatherListNew[0][6])
else:
    min_temp = 0
    

for j in range(1, len(weatherListNew)):
    if weatherListNew[j][5].isdigit():
        if max_temp < int(weatherListNew[j][5]):
            max_temp = int(weatherListNew[j][5])
    else:
        continue
    
    if weatherListNew[j][6].isdigit():
        if min_temp > int(weatherListNew[j][6]):
            min_temp = int(weatherListNew[j][6])
    else:
        continue


print("10-year maximum temperature:", max_temp, "F")
print("10-year minimum temperature:", min_temp, "F")
print()

month = input("Please enter a month: ")
year = int(input("Please enter a year: "))
print()

monthDict = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
sum_temp = 0
sum_humid = 0
sum_wind = 0
count_prec = 0
count_temp = 0
count_humid = 0
count_wind = 0
count_day = 0

for k in range(len(weatherListNew)):
    weatherLineDate = weatherListNew[k][0]
    weatherDateList = weatherLineDate.split("/")
    weatherDateMonth = weatherDateList[0]
    weatherDateYear = weatherDateList[2]
    
    
    if monthDict[month] == int(weatherDateMonth):
        if year == int(weatherDateYear):
            count_day += 1
            
            if weatherListNew[k][4].isdigit():
                weatherDateTemp = int(weatherListNew[k][4])
                sum_temp += weatherDateTemp
                count_temp += 1
                
            if weatherListNew[k][3].isdigit():
                weatherDateHumid = int(weatherListNew[k][3])
                sum_humid += weatherDateHumid
                count_humid += 1
            
            if weatherListNew[k][1] != '':
                weatherDateWind = float(weatherListNew[k][1])
                sum_wind += weatherDateWind
                count_wind += 1
            
            if weatherListNew[k][2] != '':
                if float(weatherListNew[k][2]) > 0:
                    count_prec += 1
                
            
temp_avg = sum_temp/count_temp
humid_avg = sum_humid/count_humid
wind_avg = sum_wind/count_wind
percent_prec = (count_prec/count_day) * 100

temp_avg = round(temp_avg, 1)
humid_avg = round(humid_avg, 1)
percent_prec = round(percent_prec, 1)     

print(f"For {month} {year}:") 
print("Mean average daily temperature:", temp_avg, "F")
print("Mean relative humidity:", humid_avg, "%")
print(f"Mean daily wind speed: {wind_avg:.2f} mph")
print("Percentage of days with precipitation:", percent_prec, "%")
    
#Comment