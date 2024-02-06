import sqlite3
import pandas as pd #imports

conn = sqlite3.connect('pollution.db') #db creation
cur = conn.cursor()

try : # table creation for station data
    cur.execute('''CREATE TABLE Station(
    SiteID INTEGER NOT NULL,
    Location TEXT,
    geo_point_2d TEXT,
    PRIMARY KEY(SiteID)
    )
    ''')

except sqlite3.Error as e : #error handling
    print((e))

else: #success handling
    print(('Station table created successfully!'))


try: #table creation for reading data
    cur.execute('''CREATE TABLE Reading( 
        readingId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        Date_Time DATETIME,
        NOX FLOAT,
        NO2 FLOAT,
        NO FLOAT,
        NVPM10 FLOAT,
        VPM10 FLOAT,
        NVPM25 FLOAT,
        CO FLOAT,
        SO2 FLOAT,
        O3 FLOAT,
        PM25 FLOAT,
        VPM25 FLOAT,
        PM10 FLOAT,
        Temperature FLOAT,
        RH FLOAT,
        Air_Pressure FLOAT,
        Current BOOLEAN,
        DateStart DATETIME,
        DateEnd DATETIME,
        Instrument_Type TEXT,
        SiteID INTEGER NOT NULL,
        FOREIGN KEY(SiteID) REFERENCES Station(SiteID)
        )''')
  
except sqlite3.Error as e :
    print(e)

else:
    print(('Reading table created successfully!'))


try: #table creation for measure data
    cur.execute('''CREATE TABLE measureInfo( 
        Measure TEXT PRIMARY KEY NOT NULL,
        unit TEXT NOT NULL,
        description TEXT NOT NULL
        )'''
    )
except sqlite3.Error as e : 
    print(e)

else: 
    print(('Measure table created successfully!'))

conn.commit()
conn.close()

#--------------------------------------------------------------- inserting records into database---------------------------------------------------------------
cursor = conn.cursor()

df = pd.read_csv('clean.csv', delimiter=';', low_memory= False) #reading data

print(df.head()) 

print(df.columns) #checking data columns

for row in df.itertuples(): #splitting rows into different tables
    print(row)
    cursor.execute(            '''INSERT INTO Reading(  
            Date_Time,NOx,NO2,NO,NVPM10,VPM10,NVPM25,CO,SO2,O3,PM25,VPM25,PM10,Temperature,RH,Air_Pressure,Current,DateStart,DateEnd,SiteID) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', 
            (row.Date_Time,row.NOx,row.NO2,row.NO,row.NVPM10,row.VPM10,row.NVPM25,row.CO,row.SO2,row.O3,row.PM25,row.VPM25,row.PM10,row.Temperature,row.RH,row.Air_Pressure,row.Current,row.DateStart,row.DateEnd,row.SiteID))
    cursor.execute('''INSERT or REPLACE INTO Station(SiteID,Location,geo_point_2d) VALUES (?,?,?)''', (row.SiteID,row.Location, row.geo_point_2d))
    conn.commit()

conn.close()


        