import json
import requests

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    topartist = "joe"

    data = requests.get(url).text
    data = json.loads(data)
    
    #print "topartists is a: " + str(type(data["topartists"]))
    #print "keys for topartist are: " + str(data["topartists"].keys())

    #print "artist is a: " + str(type(data["topartists"]["artist"]))
    # only works if you limit to one row returned...print "keys for artist are: " + str(data["topartists"]["artist"].keys())

    #print "first artist name is: " + str(data["topartists"]["artist"][0]["name"])
    #test line, one more change,
    # last test change
    topartist = data["topartists"]["artist"][0]["name"]

    #print data["topartists"]["@attr"]
    #print data["topartists"]["artist"]

    
    return topartist

if __name__ == "__main__":

    url = "http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=539f153bb0a2ca75980baa81c1722995&format=json"

    api_get_request(url)
