import csv

from data.connectors.connectors import RDSconnector

ADRESSE = 9
LON = 43
LAT = 44


def insertLine(line):
    conn.execute_insert(
        "INSERT INTO stz_googleAPI ( latitude , longitude ,station_name) "
        "VALUES (%s, %s, %s)",
        params=(line[LAT], line[LON], line[ADRESSE]),
    )


def main():
    with open(
        "../../../../data/gireve/consolidation-etalab-schema-irve-v-2.0.2-20220723.csv",
        "r",
        encoding="utf-8",
    ) as dataFile:

        headers = dataFile.readline()
        csvReader = csv.reader(dataFile)
        count = 0
        for line in csvReader:

            insertLine(line)
            count += 1
        print(count)


if __name__ == "__main__":
    conn = RDSconnector("../../../../conf.json")
    main()
