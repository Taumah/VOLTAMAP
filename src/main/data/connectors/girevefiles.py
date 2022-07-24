"""
New data source added at the end of the project
"""
import csv
# pylint: disable=import-error

from data.connectors.connectors import RDSconnector

ADRESSE = 9
LON = 43
LAT = 44


def insert_line(line):
    """insert into database"""
    conn.execute_insert(
        "INSERT INTO stz_googleAPI ( latitude , longitude ,station_name) "
        "VALUES (%s, %s, %s)",
        params=(line[LAT], line[LON], line[ADRESSE]),
    )


def main():
    """main bloc"""
    with open(
        "../../../../data/gireve/consolidation-etalab-schema-irve-v-2.0.2-20220723.csv",
        "r",
        encoding="utf-8",
    ) as data_file:

        data_file.readline()
        csv_reader = csv.reader(data_file)
        count = 0
        for line in csv_reader:

            insert_line(line)
            count += 1
        print(count)


if __name__ == "__main__":
    conn = RDSconnector("../../../../conf.json")
    main()
