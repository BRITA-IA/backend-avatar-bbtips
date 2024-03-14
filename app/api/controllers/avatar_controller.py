from app.config.connection_mysql import ConnectionMySQL
from app.core.OpenAIAssistant.AIAssistant import AIAssistant 

class AvatarController:

    def __init__(self) -> None:
        self.connection = ConnectionMySQL()
        self.assistant = AIAssistant()
        

    def get_response_for_question(self, data: any):
        question = data.get('question')

        #ejemplo de uso
        # pregunta del usuario
        additional_instructions = "Sé amable y comprensiva con el usuario"
        response = self.assistant.ask_question_and_get_response(question, additional_instructions)
        return response
