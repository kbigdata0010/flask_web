#mongodb local cocnnect
import pymongo
from pymongo import MongoClient
import bson


mongodb_url='mongodb+srv://root:1234@mydb.vqrlsdn.mongodb.net/?retryWrites=true&w=majority&appName=mydb'
class MONGODB:
    def __init__(self, mongodb_url , db_name):
        try:
            self.client = MongoClient(mongodb_url)
            self.db = self.client[db_name]
            print("Connected successfully!!!")
        except:
            print("Could not connect to MongoDB")

    def insert_data(self,collection_name , data):
        document = self.db[collection_name]
        try:
            rec_id1 = document.insert_one(data)
            print("Data inserted with record ids", rec_id1)
        except:
            print("Could not insert data")

    def find_data(self, collection_name , query={} ):
        
        document = self.db[collection_name]
        try:
            cursor = document.find(query)
            # print(cursor)
            find_list=[]
            for record in cursor:
                find_list.append(record)
            
            return find_list
         
        except:
            print("Could not find data")

    def update_data(self, collection_name ,  query , values ):
        document = self.db[collection_name]
        try:
            document.update_one(query,{"$set":values} )
            print("Data updated successfully")
        except:
            print("Could not update data")

    def delete_data(self, collection_name , query):
        document = self.db[collection_name]
        try:
            document.delete_one(query)
            print("Data deleted successfully")
        except:
            print("Could not delete data")





if __name__ == "__main__":
    mongodb = MONGODB(mongodb_url , db_name='mytest')
    doc = {
        "username":"gary3",
        "email":"3@naver.com",
        "password":"1234"
    }
    mongodb.insert_data(collection_name='mydoc',data=doc )
    query = {
        "email":"1@naver.com"
    }
    # find_list = mongodb.find_data(collection='mydoc', query=query)
    # print(find_list)
    query = {'_id':bson.ObjectId("6628640127d20ce07aa99409")  }
    new_values = {"username":"HHHHH", "email":"2@naver.com", "address":"seoul"}
    # mongodb.update_data(collection_name='mydoc' ,query=query, values= new_values)
    # mongodb.delete_data(collection_name='mydoc' , query=query)