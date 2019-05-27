# spaceapegamesAPI

This code was made using the API from https://www.giantbomb.com/api/
This provides a sample python script that can query the API.
you will need to provide an API KEY for this to work.
I created a file called apikey with the environment variable APIKEY=... and sourced the file
Alternatively just run

export "APIKEY=...."

run with
./api.py search ape # to search all games with ape in the name
./api.py inspect <guid> to search for information on the game returned in the search
./api.py inspect <guid> --dlc to return dlc as well as base info

The 2 apis I use are
curl "https://www.giantbomb.com/api/games/?api_key=${APIKEY}&format=json&field_list=name,id" | jq
curl "https://www.giantbomb.com/api/game/{guid}/?api_key=${APIKEY}&format=json&field_list=name" | jq

the tests return
[
  {
    "guid": "3030-19578",
    "name": "Scapeghost"
  }
]
And
{
"deck": null,
"description": null,
"genres": [
    {
    "api_detail_url": "https://www.giantbomb.com/api/genre/3060-4/",
    "id": 4,
    "name": "Adventure",
    "site_detail_url": "https://www.giantbomb.com/games/?wikiSlug=adventure&wikiTypeId=3060&wikiId=4&genre=4"
    }
],
"name": "Scapeghost"
}