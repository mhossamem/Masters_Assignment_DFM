import pandas as pd
import pymongo # import the pymongo module

client  = pymongo.MongoClient("mongodb://localhost:27017/") # connect to the database

df = pd.read_csv('clean.csv',delimiter=';', low_memory=False) # read the csv file

df = df[df['Location'] == 'Old Market'] # get the desired station

print(df.head()) #check head of data frame

db = client["NOSQL_MODEL"] # name of the mongo database

dataDocuments = df.to_dict('records') # convert the data frame to a list of dictionaries for mongodb

db.Station_Collection.insert_many(dataDocuments) # insert the data into the collection using insert many functionality while creating the collection