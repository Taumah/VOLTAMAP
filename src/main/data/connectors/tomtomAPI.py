""" class TomtomAPISearch """
# pylint: disable=C0103
import geocoder
import requests


class TomtomAPISearch:
    """simplify calls to tomtom API"""

    def __init__(self):
        self.base_url = "https://api.tomtom.com/search/2/"
        self.key = "NGxlSU04s6PDx4eCnI2sxGhMlAx6Lp2R"

    def get_station_data(self, Station):
        """get data from specific station"""
        url = (
            self.base_url + f"chargingAvailability.json?"
            f"key={self.key}&chargingAvailability={Station}"
        )

        c = requests.get(url)
        return c.json()

    def get_station_summary(self, Station):
        """get stats from station"""
        data = self.get_station_data(Station)
        stations = 0
        available = 0
        for detail in data["connectors"]:
            stations += detail["total"]
            available += detail["current"]["available"]

        return f"{available} stations out of {stations}"

    def get_ids_around(self, lat=None, lon=None):
        """retrieve Ids of stations around current position"""
        ids = []
        query = "Electric Vehicle Charging Station"
        #  get lat and lon from app/website

        if lat is None or lon is None:
            g = geocoder.ip("me")
            lat = g.latlng[0]
            lon = g.latlng[1]

        url = (
            self.base_url + f"poiSearch/{query}.json?"
            f"key={self.key}&typehead=true"
            f"&countrySet=FR&limit=5&ofs=0&limit=5&"
            f"ofs=0&lat={lat}&lon={lon}"
            f"&radius=1000&categoryset=7309"
        )
        data = requests.get(url)
        for item in data.json()["results"]:
            ids.append(item["id"])
        return ids


if __name__ == "__main__":
    tomtomAPI = TomtomAPISearch()
    # print(tomtomAPI.get_station_data("056009007851772"))

    print(tomtomAPI.get_station_summary("250009041145403"))
    # for station in tomtomAPI.get_ids_around()['results']:
    #     print(station['id'])
    #     print(tomtomAPI.get_station_data(station['id']))
