#!/usr/bin/python
import requests
import json
import argparse
import os

########################################## Functions


def search(name):
    url = base_url + "games/?api_key=" + api_key + "&format=json&filter=name:" + name + "&field_list=guid,name"
    games_list = requests.get(url, headers=headers)
    all_games = json.loads(games_list.content)
    return all_games['results']


def inspect(guid, dlc=False):
    url = base_url + "game/" + guid + "/?api_key=" + api_key + "&format=json&field_list=name,description,genres,deck"
    if(dlc):
        url = url + ',dlcs'
    game_info = requests.get(url, headers=headers)
    results = json.loads(game_info.content)
    return results['results']


###################################### Vars
api_key = os.environ['APIKEY']
headers = {'User-Agent': 'tmoody technical test'}  # api requested useragent to identify who is using it
base_url = "https://www.giantbomb.com/api/"


parser = argparse.ArgumentParser(description='search games')
parser.add_argument('function', type=str, choices=['search', 'inspect'],
                    help='type of request (search or inspect)')
parser.add_argument('filter', type=str,
                    help='search criteria')
parser.add_argument('--dlc', action='store_true',
                    help='Used with inspect to return DLC')
args = parser.parse_args()

######################## main
if(args.function == 'search'):
    results = search(args.filter)
#   for game in results:
#        inspect(game['guid'])
else:
    if(args.dlc):
        results = inspect(args.filter, True)
    else:
        results = inspect(args.filter)

print(json.dumps(results, indent=2, sort_keys=True))
