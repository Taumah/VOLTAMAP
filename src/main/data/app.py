"""
    This file contains the main function,
    used for the whole project
"""
import json
import time

import geocoder
import pandas

from data.connectors.GoogleAPISearch import GoogleAPISearch
from data.connectors.connectors import RDSconnector


# GOOGLE_API_KEY = "AIzaSyCb9HQGlIFqlL_QaCQh2_vQx6cDtOFai0c"
# GOOGLE_API_KEY = "AIzaSyBVfRkQ9x5_2EVe510QaYS9h2qHVI0bxwk"


def update_checkpoint(string, target_table):
    """
    update checkpoint
    """
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

    with open(
            f"./checkpoint/{target_table}/fetch_grid.json", "r", encoding="utf-8"
    ) as file:
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

    origin_insert_count = insert_count = min(width * height / 50, 12000)

    while (
            string["coordinates"]["current"]["lon"] > string["coordinates"]["dest"]["lon"]
    ):
        while (
                string["coordinates"]["current"]["lat"]
                < string["coordinates"]["dest"]["lat"]
        ):
            print(
                string["coordinates"]["current"]["lon"],
                string["coordinates"]["current"]["lat"],
            )
            insert_count -= 1
            coordinates_insert(
                conn,
                string["coordinates"]["current"]["lat"] / precision,
                string["coordinates"]["current"]["lon"] / precision,
                target_table,
            )
            update_checkpoint(string, target_table)
            string["coordinates"]["current"]["lat"] += width_steps

            if insert_count == 0:
                string["total_inserts"] += origin_insert_count
                update_checkpoint(string, target_table)
                return
            time.sleep(1)

        string["coordinates"]["current"]["lon"] += height_steps
        string["coordinates"]["current"]["lat"] = string["coordinates"]["origin"]["lat"]
    string["total_inserts"] += origin_insert_count - insert_count
    update_checkpoint(string, target_table)


def add_suspicious_point(station):
    lat = station["geometry"]["location"]["lat"]
    lng = station["geometry"]["location"]["lng"]
    name = station["name"]
    place_id = station["place_id"]
    with open(f"./checkpoint/googleAPI/dense_places.csv", "a") as file:
        file.write("%s,%s,%s,%s" % (place_id, lat, lng, name))


def coordinates_insert(conn, lat, lon, table):
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
        lat = station["geometry"]["location"]["lat"]
        lng = station["geometry"]["location"]["lng"]
        icon = station["icon"]
        name = station["name"]
        if station["place_id"] in already_known["api_id"].to_numpy():
            print(f"{station['place_id']} already known, updating")
            conn.execute_insert(
                f"update stz_{table} set "
                f"latitude=%s, "
                f"longitude=%s, "
                f"icon=%s, "
                f"station_name=%s, "
                f"json_data=%s "
                f"where api_id=%s",
                params=(lat, lng, icon, name, station.__str__(), station['place_id'])
            )
        else:
            print(f"inserting {station['place_id']}")
            conn.execute_insert(
                f"insert into stz_{table}(id, api_id , latitude, longitude, icon , station_name, json_data) "
                f"values(null,%s,%s,%s,%s,%s,%s)",
                params=(station['place_id'], lat, lng, icon, name, station.__str__())
            )

    print(len(already_known), "stations registered")
    print(len(nearby["results"]), "stations nearby")
    if len(nearby["results"]) == 100:
        print("suspected dense area")
        add_suspicious_point(nearby["results"][0])


def one_fetch():
    """launch tests for app.py"""

    # google_api = GoogleAPISearch()
    # dic = json.loads(google_api.get_nearby_station())
    g = geocoder.ip("me")
    lat = g.latlng[0]
    lon = g.latlng[1]
    conn = RDSconnector("../../../conf.json")

    coordinates_insert(conn, lat, lon, 'googleAPI')
    # print(dic)


def main():
    """Main function"""
    # coordinates_insert()
    grid_fetch("googleAPI")
    # grid_fetch("tomtomAPI")

    # one_fetch()


if __name__ == "__main__":
    main()
