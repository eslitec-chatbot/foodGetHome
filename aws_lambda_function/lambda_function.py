import requests
from bs4 import BeautifulSoup
import pymongo
from dotenv import find_dotenv, load_dotenv
import os
import json


dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class MongoManager(object):

    client = pymongo.MongoClient(os.environ.get("FOOD_POKEMON_MONGO_URI"))
    db = client["foodpokemon"]

    def get_collection(self, collection_name):
        return self.db[collection_name]

    @staticmethod
    def insert_collection(collection, insert_data):
        try:
            result = collection.insert_one(insert_data)
            return result
        except Exception as e:
            print (e)

    @staticmethod
    def update_collection(collection, find, insert_data):
        try:
            result = collection.find_one_and_update(
                find,
                {"$set": insert_data}, upsert=True)
            return result
        except Exception as e:
            print (e)

    @staticmethod
    def find(collection, script={}):
        try:
            return collection.find(script)
        except Exception as e:
            print (e)


def lambda_handler(event, context=None):
    try:
        event = json.loads(event['body'])
    except:
        pass

    api = event['api']
    mongo = MongoManager()
    if api == 'createUser':
        result = update_or_create_user(mongo, event)
    elif api == 'updateUserCrop':
        result = update_users_crop(mongo, event)
    elif api == 'getCrop':
        result = get_crop(mongo, event)
    elif api == 'getUserCrop':
        result = get_user_crop(mongo, event)
    else:
        result = 'Hello from Lambda!'
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }


def get_user_crop(mongo, event):
    print ("in get_user_crop")
    data = event['data']
    user_collection = mongo.get_collection("users")
    user = mongo.find(user_collection, {"lineId": data["lineId"]})
    if user.count() > 0:
        user = user[0]
        users_crops = user["myCrops"]
        for i, c in enumerate(users_crops):
            users_crops[i]["_id"] = str(c["_id"])
        return users_crops
    else:
        return "Crop or User not found"

def update_or_create_user(mongo, event):
    print ("in update_or_create_user")
    data = event['data']
    user_collection = mongo.get_collection("users")
    user = mongo.find(user_collection, {"lineId": data["lineId"]})
    if user.count() == 0:
        mongo.insert_collection(user_collection, {
            "lineId": data["lineId"],
            "name": data["name"],
            "profileImage": data["profileImage"],
            "myCrops": []
        })
        return data
    else:
        mongo.update_collection(user_collection,
            find={"lineId": data["lineId"]},
            insert_data={
                "name": data["name"],
                "profileImage": data["profileImage"],
            }
        )
        return data
    print (data)

def update_users_crop(mongo, event):
    print ("in update_users_crop")
    data = event['data']
    crop_collection = mongo.get_collection("crops")
    user_collection = mongo.get_collection("users")
    crop = mongo.find(crop_collection, {"traceCode": data["traceCode"]})
    user = mongo.find(user_collection, {"lineId": data["lineId"]})
    if crop.count() > 0 and user.count() > 0:
        user = user[0]
        crop = crop[0]
        users_crops = user["myCrops"]
        crop.update(scanNumber=1)
        for i, c in enumerate(users_crops):
            if c["traceCode"] == data["traceCode"]:
                users_crops[i]["scanNumber"] += 1
                crop = None
                break

        if crop or len(users_crops) == 0:
            users_crops.append(crop)

        mongo.update_collection(user_collection,
            find={"lineId": data["lineId"]},
            insert_data={"myCrops": users_crops}
        )

        return data
    else:
        return "Crop or User not found"
    return ''

def get_crop(mongo, event):
    print ("in get_crop")
    data = event['data']
    crop_collection = mongo.get_collection("crops")
    crop = mongo.find(crop_collection, {"traceCode": data["traceCode"]})
    if crop.count() > 0:
        crop[0] = str(crop[0])
        return crop[0]
    else:
        return 'Crop not found'

if __name__ == "__main__":
    # Add yourself test data
    lambda_handler(event)

