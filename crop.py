import pandas as pd
import time as time
start_time = time.time() #starting exem cution timer
print(pd.__version__) #checking pandas version for compatability
df = pd.read_csv("air-quality-data-2003-2022.csv", delimiter=";", parse_dates=["Date Time"], low_memory = False)
# reading the csv file with pandas and using faster and newer optimized engine to read the csv, parsing date time column as date time
#-------------------- please remove engine parameter if python is not up-to-date------------------#
print(len(df)) # printing length before cropping data
df = df[df["Date Time"] >= "2010-01-01"] #setting crop frame
print(len(df)) #printing length after cropping data

df.to_csv("crop.csv", index=False, sep=";") #save changes to a new csv file

print("Total execution time: ", time.time() - start_time()) #preview execution time