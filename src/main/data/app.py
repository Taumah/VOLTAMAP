"""
    This file contains the main function,
    used for the whole project
"""
import json

import pandas

from main.data.connectors.GoogleAPISearch import GoogleAPISearch
from main.data.connectors.connectors import RDSconnector


# GOOGLE_API_KEY = "AIzaSyCb9HQGlIFqlL_QaCQh2_vQx6cDtOFai0c"


def update_checkpoint(string, target_table):
    with open(
            f"./checkpoint/{target_table}/fetch_grid.json", "w", encoding="utf-8"
    ) as file:
        json.dump(
            string,
            fp=file,
            indent=4,
            separators=(", ", ": "),
            sort_keys=True,
        )


def grid_fetch(target_table):
    """read checkpoint file to move x and y cursor along France (GPS)"""
    conn = RDSconnector("../../../conf.json")

    with open(f"./checkpoint/{target_table}/fetch_grid.json", "r", encoding="utf-8") as file:
        string = json.load(file)
    bounding_box = (
        (
            string["coordinates"]["dest"]["lat"],
            string["coordinates"]["dest"]["lon"]
        ),
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

    origin_insert_count = insert_count = 1500

    while string["coordinates"]["current"]["lon"] > string["coordinates"]["dest"]["lon"]:
        while string["coordinates"]["current"]["lat"] < string["coordinates"]["dest"]["lat"]:
            print(string["coordinates"]["current"]["lon"], string["coordinates"]["current"]["lat"])
            insert_count -= 1
            coordinates_insert(conn, string["coordinates"]["current"]["lat"] / precision,
                               string["coordinates"]["current"]["lon"] / precision, target_table)
            update_checkpoint(string, target_table)
            string["coordinates"]["current"]["lat"] += width_steps

            if insert_count == 0:
                string["total_inserts"] += origin_insert_count
                update_checkpoint(string, target_table)
                return

        string["coordinates"]["current"]["lon"] += height_steps
        string["coordinates"]["current"]["lat"] = string["coordinates"]["origin"]["lat"]
    string["total_inserts"] += origin_insert_count - insert_count
    update_checkpoint(string, target_table)


def coordinates_insert(conn , lat, lon, table):
    """Writes line to RDS db"""
    already_known = pandas.DataFrame(
        data=conn.execute_select(
            f"select id , api_id, latitude, longitude, insert_time  from stz_{table}"
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
                f"insert into stz_{table}(id, api_id , latitude, longitude) "
                f"values(null,'{station['place_id']}','{lat}','{lng}')"
            )

    print(already_known)
    print(nearby)


def main():
    """Main function"""
    # coordinates_insert()
    grid_fetch("googleAPI")
    # grid_fetch("tomtomAPI")


if __name__ == "__main__":
    main()
