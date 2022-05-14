"""
    This file contains the main function,
    used for the whole project
"""
import json

import pandas

from main.data.GoogleAPISearch import GoogleAPISearch
from main.data.connectors import RDSconnector


# GOOGLE_API_KEY = "AIzaSyCb9HQGlIFqlL_QaCQh2_vQx6cDtOFai0c"


def main():
    """Main function"""
    conn = RDSconnector("../../../conf.json")
    alreadyKnown = pandas.DataFrame(
        data=conn.execute_select("select id , latitude, longitude , googleID from stationID"),
        columns=["id", "latitude", "longitude", "googleID"])

    GoogleAPI = GoogleAPISearch()
    nearby = json.loads(GoogleAPI.get_nearby_station())

    # print("test1" in alreadyKnown['googleID'].to_numpy())
    #
    for station in nearby['results']:

        if station['place_id'] in alreadyKnown['googleID'].to_numpy():
            print(f"{station['place_id']} already known")
        else:
            print(f"inserting {station['place_id']}")
            lat = station["geometry"]["location"]["lat"]
            lng = station["geometry"]["location"]["lng"]
            conn.execute_insert(
                "insert into stationID(id , latitude, longitude , googleID) "
                f"values(null,'{lat}','{lng}','{station['place_id']}')")

    print(alreadyKnown)
    print(nearby)


if __name__ == "__main__":
    main()
