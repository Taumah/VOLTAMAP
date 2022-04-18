import requests


class TomtomAPISearch:

    def __init__(self):
        self.base_url = "https://api.tomtom.com/search/2/"
        self.key = "NGxlSU04s6PDx4eCnI2sxGhMlAx6Lp2R"

    def getStationData(self, Station):
        url = self.base_url + f"chargingAvailability.json?" \
                              f"key={self.key}&chargingAvailability={Station}"

        c = requests.get(url)
        return c.json()

    def getStationSummary(self, Station):
        data = self.getStationData(Station)
        stations = 0
        available = 0
        for detail in data['connectors']:
            stations += detail['total']
            available += detail['current']['available']

        return f"{available} stations out of {stations}"

    def getIdsAround(self):
        ids = []
        query = "Electric Vehicle Charging Station"
        # todo : get lat and lon from app/website
        url = self.base_url + f"poiSearch/{query}.json?" \
                              f"key={self.key}&typehead=true" \
                              f"&countrySet=FR&limit=5&ofs=0&limit=5&" \
                              f"ofs=0&lat=48.977890&lon=2.049340" \
                              f"&radius=1000&categoryset=7309"
        c = requests.get(url)
        for item in c.json()['results']:
            ids.append(item['id'])
        return ids


if __name__ == "__main__":
    tomtomAPI = TomtomAPISearch()
    # print(tomtomAPI.getStationData("056009007851772"))

    print(tomtomAPI.getStationSummary("250009041145403"))
    # for station in tomtomAPI.getIdsAround()['results']:
    #     print(station['id'])
    #     print(tomtomAPI.getStationData(station['id']))
