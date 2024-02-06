
import pandas as pd
import time as time #packages used
start_time = time.time() #starting timer 
print(pd.__version__) #checking pd version

df = pd.read_csv("crop.csv", delimiter=";", parse_dates=["Date Time"], low_memory = False)
# reading the csv file with pandas and using faster and newer optimized engine to read the csv, parsing date time column as date time
#-------------------- please remove engine parameter if python is not up-to-date------------------#
correctDataDictionary = {
    188: 'AURN Bristol Centre',
    203: 'Brislington Depot',
    206: 'Rupert Street',
    209: 'IKEA M32',
    213: 'Old Market',
    215: 'Parson Street School',
    228: 'Temple Meads Station',
    270: 'Wells Road',
    271: 'Trailer Portway P&R',
    375: 'Newfoundland Road Police Station',
    395: "Shiner's Garage",
    452: 'AURN St Pauls',
    447: 'Bath Road',
    459: 'Cheltenham Road \ Station Road',
    463: 'Fishponds Road',
    481: 'CREATE Centre Roof',
    500: 'Temple Way',
    501: 'Colston Avenue',
    672: 'Marlborough Street'
} #correct data dictionary to compare the values
dudCount = 0 #counter to make sure the number is correct
for row in df.index: #iterating over the index
    if df.loc[row, "Location"] != correctDataDictionary[df.loc[row, "SiteID"]]: # condition for correct location / site id pair and siteid validity
        print("Line : " + str(row) + " , Wrong value : " + df.loc[row,"Location"] + ", Correct value : " + correctDataDictionary[df.loc[row,"SiteID"]]) # printing the line number, the wrong data and it's correct value
        df.drop(row, inplace = True)  # dropping the row from the csv
        dudCount +=1 #increment the counter

print("Total length after cleaning: " + str(len(df))) #preview length of dataframe after cleaning
print("Total count for dud records: " + str(dudCount)) #preview count for dud records
df.to_csv("clean.csv", index=False, sep=";") #save changes to a new csv file

print("Total execution time: ", time.time() - start_time()) #preview execution time
