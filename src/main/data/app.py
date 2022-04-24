"""
    This file contains the main function,
    used for the whole project
"""
import requests


def empty_array(size):
    """ returns an array of size <size> filled with zeros """
    if size == 0:
        return []
    if size < 0:
        raise ValueError("Length cannot be negative")
    return [0] * size


GOOGLE_API_KEY = "AIzaSyCb9HQGlIFqlL_QaCQh2_vQx6cDtOFai0c"


def get_place_details(place_id):
    """performs a Get request on Google Places API"""
    url = (
        f"https://maps.googleapis.com/maps/api/place/details/"
        f"json?place_id={place_id}&"
        f"key={GOOGLE_API_KEY}"
    )
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


def get_search_details(place_id):
    """get all infos from place given as param"""

    url = (
        f"https://maps.googleapis.com/maps/api/place/details/"
        f"json?place_id={place_id}&"
        f"key={GOOGLE_API_KEY}"
    )
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


def main():
    """Main function"""
    get_place_details("ChIJyeCGP7Bl5kcRAKxjPvJs41M")


if __name__ == "__main__":
    main()
