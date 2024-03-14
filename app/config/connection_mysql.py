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
                password=self.password,
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

    def execute_query(self, query):

        try:
            self.connect()
            if self.connection:
                cursor = self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()
                cursor.close()
                return 'query execute success'
        except Exception as e:
            print(f'error in execute query: {e}')
        finally:
            self.desconnect()

    def fetch_query(self, query):
        """
        This function is only read data from database

        query: str

        returns: list[]
        """
        try:
            self.connect()
            if self.connection:
                cursor = self.connection.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                column_names = [column[0] for column in cursor.description]

                results = []
                for row in rows:
                    result_dict = dict(zip(column_names, row))
                    results.append(result_dict)
                cursor.close()
                return results
            
        except Exception as e:
            print(f'error in fetch cuery: {e}')
        
        finally:
            self.desconnect()
