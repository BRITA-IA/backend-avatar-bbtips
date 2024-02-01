from app.config.connection_mysql import ConnectionMySQL


class AvatarController:

    def __init__(self) -> None:
        self.connection = ConnectionMySQL()
        pass

    def get_response_for_question(self, req):
        print(req)
        self.connection.connect()
        query = f'INSERT INTO usuarios (Name, DateActive, Region) VALUES ("{req["user"]}", "{req["date"]}", "{req["region"]}")'
        response = self.connection.insert_query(query)
        self.connection.desconnect()
        return response
