# spaceapegamesAPI

This code was made using the API from https://www.giantbomb.com/api/  
This provides a sample python script that can query the API.


# Usage
You will need to provide an API KEY for this to work.
I created a file called apikey with the environment variable APIKEY=... and sourced the file
Alternatively just run

```
export "APIKEY=...."
```

To search all games with ape in the name  
./api.py search ape  
To search for information on the game returned in the search  
./api.py inspect <guid>  
To return dlc as well as base info  
./api.py inspect <guid> --dlc  

The 2 apis I use are  
curl "https://www.giantbomb.com/api/games/?api_key=${APIKEY}&format=json&field_list=name,id" | jq  
curl "https://www.giantbomb.com/api/game/{guid}/?api_key=${APIKEY}&format=json&field_list=name" | jq

# Tests
Tests are simple flake8 and unittest
Confirm that the functions used in the script return expected output
the queries used by the tests return
```
[
  {
    "guid": "3030-19578",
    "name": "Scapeghost"
  }
]
```
And
```
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
```