import requests
import xmltodict
import json

BOEStation = "Bank of England Museum, Bank"

def getBOE(allstations):
    for eachstation in allstations['station']:
        try:
            if (BOEStation == eachstation['name']):
                return eachstation
        except Exception as e:
            print ("Exception in getting the name " + str(e));


try:
    r = requests.get('https://tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml')
    xmldictdata = xmltodict.parse(r.content)
    json_data=json.dumps(xmldictdata)
    j = json.loads(json_data)
    allstations = j['stations']
    BOEStation= getBOE(allstations)
    print ("The number of available bikes are "+ BOEStation['nbBikes'])
except Exception as e:
    print ("Exception raised when invoking the Santander URL " + str(e));

