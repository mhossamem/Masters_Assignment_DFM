import pandas as pd
import csv

tableName = 'pollution' # name of the table in the database

df = pd.read_csv('clean.csv', delimiter=';', low_memory= False) # read the csv file

with open("insert-100.sql", "w") as f: # open the sql file
    for index, row in df.iterrows(): # loop through each row in the database
        if(index == 100) : # number of rows to be inserted
            break
        print('INSERT INTO '+ tableName + ' (\'Date_Time\',\'NOx\',\'NO2\',\'NO\',\'NVPM10\',\'VPM10\',\'NVPM25\',\'CO\',\'SO2\',\'O3\',\'PM25\',\'VPM25\',\'PM10\',\'Temperature\',\'RH\',\'Air_Pressure\',\'Current\',\'DateStart\',\'DateEnd\',\'SiteID\',\'Location\',\'geo_point_2d\') VALUES (', 
              row['Date_Time'],row['NOx'],row['NO2'],row['NO'],row['NVPM10'],row['VPM10'],row['NVPM25'],row['CO'],row['SO2'],row['O3'],row['PM25'],row['VPM25'],row['PM10'],row['Temperature'],row['RH'],row['Air_Pressure'],row['Current'],row['DateStart'],row['DateEnd'],row['SiteID'],row['Location'], ',\'' + row['geo_point_2d'] + '\');', file=open('insert-100.sql', 'a'))
        # write to the sql file