from app.config.connection_mysql import ConnectionMySQL
import dotenv, os, jwt

class UserController:

    def __init__(self) -> None:
        self.connection = ConnectionMySQL()
        pass

    def validate_access_token(self, req):
        dotenv.load_dotenv()
        token = req.get('token')

        try:
            secret_key  = os.getenv('SECRET_JWT')
            token_decode = jwt.decode(token, secret_key, algorithms= ['HS256'])
            user_id = token_decode['user']
            query = f'SELECT * FROM usuarios WHERE IDUser = {user_id}'
            response = self.connection.fetch_query(query)
            if len(response) > 0:
                return {'error': False, 'data': response[0]}
            
            return {'error': True}


        except Exception as e:
            print(f'error in valid_access_token user: {e}')

            return {'error': True, 'data':'Error en la validacion del token'}

    def authentication(self, req):
        dotenv.load_dotenv()
        mail = req.get('mail')
        password = req.get('pass')

        try:

            query = f'SELECT * FROM usuarios WHERE Mail ="{mail}"'
            response = self.connection.fetch_query(query)

            if len(response) == 0:
                return {'error': True, 'data': 'Correo o contraseña incorrectos'}
            
            user = response[0]

            if user['Mail'] == mail and user['Pass'] == password:
                secret_key  = os.getenv('SECRET_JWT')
                payload = {
                    'user': user['IDUser'],
                    'role': user['IDRole']
                }
                token = jwt.encode(payload, secret_key, algorithm='HS256')
                query = f'UPDATE usuarios SET Access_Token ="{token}"'
                res = self.connection.execute_query(query)
                print(res)
                return {'error': False, 'data': user, 'token': token}
            else:
                return {'error': True, 'data': 'Correo o contraseña incorrectos'}          
        except Exception as e:
            print(f'error in autentication user: {e}')
            return 'Error en la autentificación'
