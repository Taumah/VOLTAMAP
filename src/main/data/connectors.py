""" Classes to transfer data to outside of module"""
import sys
import json
import pymysql


class RDSconnector:
    """object to execute queries on RDS"""

    # todo : possible swap from query var to set of : table + column + where (select)
    # todo : possible swap from query var to set of : table + column + values (insert)
    def __init__(self, path_to_conf_file):
        self.bucket_name = None
        try:
            with open(path_to_conf_file, "r", encoding="UTF-8") as file:

                conf = json.load(file)
                host = conf["RDSconf"]["host"]  # RDS URL
                user = conf["RDSconf"]["user"]  # RDS Mysql user
                password = conf["RDSconf"]["password"]  # RDS Mysql password
                database = conf["RDSconf"]["database"]  # RDS MySQL DB name
                self.connection = pymysql.connect(host=host, user=user, password=password, database=database)
        except (FileNotFoundError, FileNotFoundError) as error:
            print("error while reading file : ", error)
            sys.exit()
        print("end ! ")

    def execute_select(self, query):
        """launch RDS query"""
        with self.connection.cursor() as cur:
            try:
                cur.execute(query)
            except Exception as error:
                print("[ERROR]", error)

            return cur.fetchall()

    def execute_insert(self, query):
        with self.connection.cursor() as cur:
            status=cur.execute(query) != 0

            self.connection.commit()
            return status

    # def define_bucket(self, bucket_name):
    #     """set bucket to use... delete later"""
    #     self.bucket_name = bucket_name


if __name__ == "__main__":
    conn = RDSconnector("../../../conf.json")
    print(conn.execute_select("select id , latitude, longitude from stationID"))

    # print(conn.execute_query("describe stationID"))

