import pymongo

myclient = pymongo.MongoClient("mongodb://95.111.235.214:32768/")

mydb = myclient["sgsForm"]
mycol = mydb["registros"]



# print(mydb.list_collection_names())
#
# collist = mydb.list_collection_names()
# if "customers" in collist:
#   print("The collection exists.")

# print(myclient.list_database_names())
#
# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#   print("The database exists.")