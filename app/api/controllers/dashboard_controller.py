from app.config.connection_mysql import ConnectionMySQL


class DashboardController:

    def __init__(self) -> None:
        self.connection = ConnectionMySQL()
        pass

    def comments_users(self):

        query = f'SELECT * FROM comentarios_usuarios'
        response = self.connection.fetch_query(query)

        if len(response) == 0:
            return {'error': False, 'data': 'No hay comentarios'}

        return {'error': False, 'data': response}
