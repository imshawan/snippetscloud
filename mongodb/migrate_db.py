'''
    migrate_db.py

    Author:         Shawan Mandal
    Description:    This script helps in cloning an entire mongodb database collection to a new one. 
                    Either locally or on the same atlas cluster.
'''

from pymongo import MongoClient

SOURCE_DB_URL = "mongodb+srv://mydatabase:testpwd@mongo.jufi.mongodb.net/"
# Replace with your mongo connection URL

SOURCE_DATABASE = input("Enter source DB name: ").strip() #
TARGET_DATABASE = input(f"Enter new/target DB name: (default is {SOURCE_DATABASE}) ").strip()

dump_case = input("Dump locally? (yes/no) ").strip()
if TARGET_DATABASE == "":
    TARGET_DATABASE = SOURCE_DATABASE # Using the same name for the newly created DB
SOURCE_CLIENT = MongoClient(SOURCE_DB_URL)
LOCAL_CLIENT = MongoClient("mongodb://localhost:27017/") #If want to dump locally
CLIENT = SOURCE_CLIENT
WRITE_CLIENT = SOURCE_CLIENT
if (dump_case.lower() == "yes" or dump_case.lower() == "y"):
    WRITE_CLIENT = LOCAL_CLIENT

DATABASE = CLIENT[SOURCE_DATABASE]
COLLECTIONS = DATABASE.list_collection_names()

print(f"Found {len(COLLECTIONS)} collections in target database i.e {SOURCE_DATABASE} \n")
try:
    for each in COLLECTIONS:
        print(f"Migrating collection '{each}' to {TARGET_DATABASE}")
        print(f"Found {DATABASE[each].count_documents({})} documents inside '{each}' collection") 
        for x in DATABASE[each].find({}):
            WRITE_CLIENT[TARGET_DATABASE][each].insert_one(x)
        print(f"Completed migrating collection: {each} \n\n")
    print(f"Successfully migrated all collections from {SOURCE_DATABASE} to {TARGET_DATABASE} \n")
    print("Task completed successfully!")
except Exception(err):
    print(err)
    print("Task failed due to exception...")

input("Press any key to continue...")