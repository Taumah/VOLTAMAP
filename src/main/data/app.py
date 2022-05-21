"""
    This file contains the main function,
    used for the whole project
"""
import json

import pandas

from main.data.connectors.GoogleAPISearch import GoogleAPISearch
from main.data.connectors.connectors import RDSconnector


# GOOGLE_API_KEY = "AIzaSyCb9HQGlIFqlL_QaCQh2_vQx6cDtOFai0c"


def grid_fetch():
    """read checkpoint file to move x and y cursor along France (GPS)"""
    with open("./checkpoint/fetch_grid.json", "r", encoding="utf-8") as file:
        string = json.load(file)
    bounding_box = (
        (string["coordinates"]["dest"]["lat"], string["coordinates"]["dest"]["lon"]),
        (
            string["coordinates"]["current"]["lat"],
            string["coordinates"]["current"]["lon"],
        ),
    )

    precision = 1e8
    height, width = string["height"], string["width"]

    width_steps = round(
        (bounding_box[0][0] - string["coordinates"]["origin"]["lat"]) / width
    )
    height_steps = round(
        (bounding_box[0][1] - string["coordinates"]["origin"]["lon"]) / height
    )

    print(width_steps, height_steps)
    origin_insert_count = insert_count = 60
    for x_coord in range(bounding_box[1][0], bounding_box[0][0], width_steps):
        for y_coord in range(bounding_box[1][1], bounding_box[0][1], height_steps):
            print(x_coord / precision, y_coord / precision)
            # coordinates_insert(x / precision, y / precision)
            insert_count -= 1
            if insert_count == 0:
                string["coordinates"]["current"]["lat"] = x_coord
                string["coordinates"]["current"]["lon"] = y_coord
                string["total_inserts"] += origin_insert_count
                with open(
                    "./checkpoint/fetch_grid.json", "w", encoding="utf-8"
                ) as file:
                    json.dump(
                        string,
                        fp=file,
                        indent=4,
                        separators=(", ", ": "),
                        sort_keys=True,
                    )
                return


def coordinates_insert(lat=None, lon=None):
    """Writes line to RDS db"""
    conn = RDSconnector("../../../conf.json")
    already_known = pandas.DataFrame(
        data=conn.execute_select(
            "select id , api_id, latitude, longitude, insert_time  from stz_googleAPI"
        ),
        columns=["id", "api_id", "latitude", "longitude", "insert_time"],
    )

    google_api = GoogleAPISearch()
    nearby = json.loads(google_api.get_nearby_station(lat, lon))

    # print("test1" in alreadyKnown['googleID'].to_numpy())
    #
    for station in nearby["results"]:

        if station["place_id"] in already_known["api_id"].to_numpy():
            print(f"{station['place_id']} already known")
        else:
            print(f"inserting {station['place_id']}")
            lat = station["geometry"]["location"]["lat"]
            lng = station["geometry"]["location"]["lng"]
            conn.execute_insert(
                "insert into stz_googleAPI(id, api_id , latitude, longitude) "
                f"values(null,'{station['place_id']}','{lat}','{lng}')"
            )

    print(already_known)
    print(nearby)


def main():
    """Main function"""
    # coordinates_insert()
    grid_fetch()


if __name__ == "__main__":
    main()
