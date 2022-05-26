""" class GoogleAPISearch """
# pylint: disable=C0103
import geocoder
import requests


class GoogleAPISearch:
    """simplify calls to google API"""

    def __init__(self):
        self.base_url = "https://maps.googleapis.com/maps/api/place"
        self.key = "AIzaSyCb9HQGlIFqlL_QaCQh2_vQx6cDtOFai0c"

    def get_station_data(self, station_id):
        """get data from specific station"""
        url = (
                self.base_url + f"/details/json?place_id={station_id}&"
        # "fields=name%2Crating%2Cformatted_phone_number"
                                "&key=" + self.key
        )

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def get_nearby_station(self, lat=None, lon=None):
        """retrieve stations around current position
        If no localisation given, it returns stations
        around current position"""
        # lat, lon = '48.97472824016118', '2.0494848456340353'
        if lat is None or lon is None:
            g = geocoder.ip("me")
            lat = g.latlng[0]
            lon = g.latlng[1]

        loc = f"{lat}%2C{lon}"
        url = (
                self.base_url + f"/nearbysearch/json?location={loc}"
                                "&radius=5000&keyword=charging electric vehicule station&key=" + self.key
        )

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.text


if __name__ == "__main__":
    geo = geocoder.ip("me")
    print(geo.latlng)
