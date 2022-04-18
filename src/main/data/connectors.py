import pymysql
import json


class RDSconnector():

    def __init__(self, pathToConfFile):
        try:
            with open(pathToConfFile, 'r') as file:

                conf = json.load(file)
                host = conf["RDSconf"]["host"]  # RDS URL
                user = conf["RDSconf"]["user"]  # RDS Mysql user
                password = conf["RDSconf"]["password"]  # RDS Mysql password
                database = conf["RDSconf"]["database"]  # RDS MySQL DB name
                self.connection = pymysql.connect(host=host, user=user, password=password, database=database)
        except Exception as e:
            print("error while reading file : ", e)
            exit(1)
        print("end ! ")

    def executeQuery(self, query):
        with self.connection.cursor() as cur:
            try:
                cur.execute(query)
            except Exception as e:
                print("[ERROR]", e)


if __name__ == '__main__':
    conn = RDSconnector("../../../conf.json")
    conn.executeQuery("show tables")
