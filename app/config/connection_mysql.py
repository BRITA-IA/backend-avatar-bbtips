import mysql.connector
import dotenv
import os

class ConnectionMySQL:

    def __init__(self):
        dotenv.load_dotenv()
        self.host = os.getenv('MYSQL_HOST')
        self.user = os.getenv('MYSQL_USER')
        self.password = os.getenv('MYSQL_PASSWORD')
        self.database = os.getenv('MYSQL_DATABASE')
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password =self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print('Database is connected')
                return self.connection
        except mysql.connector.Error as e:
            print(f'Error trying conecct in database: {e}')

    def desconnect(self):
        if self.connection:
            self.connection.close()
            print('Connection close')

    def insert_query(self, query):

        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()
                cursor.close()
                return 'insert successfull'
            except Exception as e:
                print(f'error in insert query: {e}')
        

    def execute_query(self, query):
        """
        This function is only read data from database

        query: str

        returns: list[]
        """
        if self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query)
            #commit for insert data
            # self.connection.commit()
            res = cursor.fetchall()
            cursor.close()
            return res