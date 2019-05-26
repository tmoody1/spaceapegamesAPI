#!/usr/bin/python
import requests
import json
import argparse
import os

def search(name):
    url = base_url + "games/?api_key=" + api_key + "&format=json&field_list=name,guid"
    games_list = requests.get(url,headers=headers)
    all_games = json.loads(games_list.content)
    matching = {}
    for game in all_games['results']:
        if( name.lower() in game['name'].lower() ):
            print(game['name'])
            matching[name] = game['guid']
    return matching

def inspect(guid):
    url = base_url + "game/" + guid + "/?api_key=" + api_key + "&format=json"
    game_info = requests.get(url,headers=headers)
    print(game_info.content)

api_key = os.environ['APIKEY']
headers = {'User-Agent': 'tmoody technical test'} # api requested useragent to identify who is using this
base_url = url = "https://www.giantbomb.com/api/"


parser = argparse.ArgumentParser(description='search games')
parser.add_argument('function', type=str,choices=['search','inspect'],
                    help='type of request (search or inspect)')
parser.add_argument('filter', type=str,
                    help='search criteria')
args = parser.parse_args()

if( args.function == 'search'):
    results = search(args.filter)
    print(results)
else:
    inspect(args.filter)
#print("full games list is ", results)