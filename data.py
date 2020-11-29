import requests
import re

title = "Clothing Brand"
unitList = ['jackets', 'shirts', 'accessories']
url = 'https://bad-api-assignment.reaktor.com'
urlUnitList = ['/products/', '/availability/']

# Database initialisation will be with ORM and SQLite in v2.0
database = {}
manufBase = []

# Singleton class should be good practice here, as database in v2.0
def unit_table(unit_type):
    database.clear()
    manufBase.clear()
    # first GET API request
    getData = requests.get(url + urlUnitList[0] + unit_type).json()
    for i in range(0, len(getData)):
        if getData[i]['manufacturer'] not in manufBase:
            manufBase.append(getData[i]['manufacturer'])
        else:
            pass

        if getData[i]['id'] not in database:
            database[getData[i]['id']] = {'manufacturer': getData[i]['manufacturer'],
                                          'name': getData[i]['name'],
                                          'color': getData[i]['color'],
                                          'price': getData[i]['price'],
                                          }
        else:
            database[getData[i]['id']].update({'manufacturer': getData[i]['manufacturer'],
                                               'name': getData[i]['name'],
                                               'color': getData[i]['color'],
                                               'price': getData[i]['price'],
                                               })

    # Second GET API request to check availability and add it to first json db
    for key in manufBase:
        getAvailability = requests.get(url + urlUnitList[1] + key).json()
        for i in range(0, len(getAvailability['response'])):
            availabilityValue = re.findall(r'\>(.*?)\</', getAvailability['response'][i]['DATAPAYLOAD'])
            aidi = getAvailability['response'][i]['id'].lower()
            if aidi in database:
                database[aidi].update(availability=availabilityValue[0])
            else:
                pass
    return database