# Create a list of each line

#with open("weather_data.csv") as data:
#    weather_list = data.readlines()
#    print(weather_list)

# Read csv and create list with temperatures

#import csv

#with open("weather_data.csv") as data:
#    weather_list = csv.reader(data)
#    temperatures = []
#    for row in weather_list:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)


# Do same as above using library pandas
# Pandas DataFrame is the whole csv file, pandas series is one of the columns

import pandas as pd

df = pd.read_csv("weather_data.csv")
#print(df["temp"])

# convert DataFrame to Dictionary
df_dict = df.to_dict()
#print(df_dict)

#temp_list = df["temp"].to_list()
#print(temp_list)

# Calculate the mean of the temperatures

#avg_temperature = sum(temp_list) / len(temp_list)
#rounded_temperature = round(avg_temperature, 2)
#print(f" The average temperature was: {rounded_temperature}")

# Do the same using the pandas data series methods

#print(df["temp"].mean())

# Extract the max temperature

#print(df["temp"].max())

# Get data from a column
#print(df["condition"]) # or
#df.condition

# Get data from a row
#print(df[df.day == "Monday"])

# Extract the row with the maximum temperature
#max_temp = df.temp.max()
#print(df[df.temp == max_temp])

#monday = df[df.day == "Monday"]
#temp_c = monday.temp
#temp_f = temp_c * (9/5) + 32
#print(temp_f)

# Create DataFrame from scratch

#data_dict = {
#    "students": ["Siri", "Bjarne", "Leah"],
#    "scores": [76, 56, 65]
#}

#data = pd.DataFrame(data_dict)
#data.to_csv("student_scores")
#print(data)

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231228.csv")
gray_fur = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
black_fur = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
cinnamon_fur = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]

gray_count = len(gray_fur)
black_count = len(black_fur)
cinnamon_count = len(cinnamon_fur)

fur_color_dict = {"color": ["Gray", "Black", "Cinnamon"],
                  "count": [gray_count, black_count, cinnamon_count]
}

fur_color_data = pd.DataFrame(fur_color_dict)
print(fur_color_data)
#fur_color_data.to_csv("squirrel_count.csv")