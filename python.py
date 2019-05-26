#!/usr/bin/python
import requests
import json
import argparse
import os

def search(name):
    headers = {'User-Agent': 'tmoody technical test'} # api requested useragent to identify who is using this
    url = "https://www.giantbomb.com/api/games/?api_key=" + api_key + "&format=json&field_list=name,id"
    games_list = requests.get(url,headers=headers)
    all_games = json.loads(games_list.content)
    matching = {}
    for game in all_games['results']:
        if( name.lower() in game['name'].lower() ):
            print(game['name'])
            matching[name] = game['id']
    return matching


api_key = os.environ['APIKEY']
print(api_key)
parser = argparse.ArgumentParser(description='search games')
parser.add_argument('function', type=str,choices=['search','inspect'],
                    help='type of request (search or inspect)')
parser.add_argument('filter', type=str,
                    help='search criteria')
args = parser.parse_args()


results = search(args.filter)
#print("full games list is ", results)


