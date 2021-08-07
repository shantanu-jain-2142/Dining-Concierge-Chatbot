from decimal import Decimal
import json
import boto3
import requests


def load_restaurants(restaurant_list, dynamodb=None):
    """
    Adds data to dynamo db in a table called yelp-restaurants.
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('yelp-restaurants')
    for restaurant in restaurant_list:
        # print (restaurant)
        table.put_item(Item=restaurant)


def createReadableFileForES():
    """
    Scrapes the data for adding it to a json file in a format accepted by ES.
    Curl command is then used for calling the _bulk api of ES.
    """
    scrapedRestaurants = []
    with open('./restaurants_clean.json', 'r') as jsonFile:
        restaurantList = json.load(jsonFile)
    for restaurant in restaurantList:
        scrapedRestaurants.append(
            {'id': restaurant['id'], 'cuisine': restaurant['cuisine']}
        )
    # print(scrapedRestaurants)
    fd = open('esIndices.json', 'w')
    for restaurant in scrapedRestaurants:
        dictToWrite = {"index": { "_index": "restaurants", "_type": "Restaurants", "_id": restaurant['id'] }}
        dataDictToWrite = {"cuisine" : restaurant['cuisine']}
        # fd.write(json.dump(dictToWrite)+"\n"+json.dump(dataDictToWrite)+"\n")
        json.dump(dictToWrite, fd)
        fd.write("\n")
        json.dump(dataDictToWrite, fd)
        fd.write("\n")
    fd.close()

if __name__ == '__main__':
    with open("./restaurants_clean.json") as json_file:
        restaurant_list = json.load(json_file, parse_float=Decimal)
        # print (restaurant_list)
    load_restaurants(restaurant_list)
    createReadableFileForES()