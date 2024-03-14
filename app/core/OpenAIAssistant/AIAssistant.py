import os
import time
from openai import OpenAI
from dotenv import load_dotenv


class AIAssistant:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=self.api_key)
        self.assistant_id = os.getenv('OPENAI_ASSISTANT_ID')
        self.thread = self.client.beta.threads.create()

    def ask_question_and_get_response(self, user_input, additional_instructions):
        self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=user_input
        )

        run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant_id,
            additional_instructions=additional_instructions
        )

        while self.client.beta.threads.runs.retrieve(thread_id=self.thread.id, run_id=run.id).status != 'completed':
            if self.client.beta.threads.runs.retrieve(thread_id=self.thread.id, run_id=run.id).status == 'failed':
                print('Run failed')
                print('Reason: ', self.client.beta.threads.runs.retrieve(thread_id=self.thread.id, run_id=run.id).last_error.message)
                return

            time.sleep(2)

        messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
        return messages.data[0].content[0].text.value
    