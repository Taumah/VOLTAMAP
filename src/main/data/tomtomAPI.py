import requests


class GoogleAPISearch:
    base_url = "https://maps.googleapis.com/maps/api/place/details/json?"

    def getStationData(self):
        url = self.base_url + "place_id=ChIJN1t_tDeuEmsRUsoyG83frY4&fields=name%2Crating%2Cformatted_phone_number" \
                              "&key=AIzaSyCb9HQGlIFqlL_QaCQh2_vQx6cDtOFai0c"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)


class TomtomAPISearch:

    def __init__(self):
        self.base_url = "https://api.tomtom.com/search/2/"

    def getStationData(self, Station):
        url = self.base_url + f"chargingAvailability.json?" \
                              f"key=NGxlSU04s6PDx4eCnI2sxGhMlAx6Lp2R&chargingAvailability={Station}"

        c = requests.get(url)
        return c.json()

    def getDetails(self):
        url = self.base_url + "poiSearch/pizza.json?key=NGxlSU04s6PDx4eCnI2sxGhMlAx6Lp2R"
        return url

    def searchAllStationID(self):
        query = "electric"
        url = self.base_url + f"poiSearch/{query}.json?" \
                              "key=NGxlSU04s6PDx4eCnI2sxGhMlAx6Lp2R&typehead=true" \
                              "&countrySet=FR&limit=5&ofs=0"
        c = requests.get(url)
        return c.json()


if __name__ == "__main__":
    tomtomAPI = TomtomAPISearch()
    print(tomtomAPI.getStationData("056009007851772"))

    for station in tomtomAPI.searchAllStationID()['results']:
        print(station['id'])
        print(tomtomAPI.getStationData(station['id']))
