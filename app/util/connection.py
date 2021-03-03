import pymysql


class Mysql_Connector:
    def __init__(self):
        self.host = "db4free.net"
        self.user = "visie_user"
        self.password = "visie_pass"
        self.data_base = "visie_db"

    def __connect__(self):
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.data_base,
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.cursor = self.connection.cursor()

    def __disconnect__(self):
        self.connection.close()

    def search(self, query):
        self.__connect__()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.__disconnect__()
        return result

    def modify(self, query):
        self.__connect__()
        self.cursor.execute(query)
        self.connection.commit()
        self.__disconnect__()
