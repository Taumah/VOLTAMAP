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
