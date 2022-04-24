""" class GoogleAPISearch """
# pylint: disable=C0103
import requests


class GoogleAPISearch:
    """ simplify calls to google API"""
    def __init__(self):
        self.base_url = "https://maps.googleapis.com/maps/api/place"
        self.key = "AIzaSyCb9HQGlIFqlL_QaCQh2_vQx6cDtOFai0c"

    def get_station_data(self):
        """ get data from specific station"""
        url = self.base_url + "/details/json?place_id=ChIJN1t_tDeuEmsRUsoyG83frY4&" \
                              "fields=name%2Crating%2Cformatted_phone_number" \
                              "&key=" + self.key

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def get_nearby_station(self):
        """ retrieve stations around current position"""
        url = self.base_url + "/nearbysearch/json?location=48.97472824016118%2C2.0494848456340353" \
                              "&radius=5000&keyword=charging electric vehicule station&key=" \
              + self.key

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)


if __name__ == "__main__":
    search = GoogleAPISearch()

    search.get_nearby_station()
