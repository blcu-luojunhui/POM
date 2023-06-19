import openai


class Azure:
    """
    使用GPT-3.5模型
    """
    def __init__(self):
        self.api_key = "b0e51a242c3745bf85af1cd77c9e9dcd"
        self.api_base = "https://madacode-gpt-api.openai.azure.com/"
        self.api_type = 'azure'
        self.api_version = '2023-03-15-preview'
        self.deployment_name = 'gpt35'
        self.messages = []

    # 单轮对话
    def single_conversation(self, content):
        openai.api_key = self.api_key
        openai.api_base = self.api_base
        openai.api_type = self.api_type
        openai.api_version = self.api_version
        response = openai.ChatCompletion.create(
            engine=self.deployment_name,
            messages=[{"role": "user", "content": content}]
        )
        return response.choices[0].message.content

    # 多轮对话
    def multi_conversations(self, content):
        openai.api_key = self.api_key
        openai.api_base = self.api_base
        openai.api_type = self.api_type
        openai.api_version = self.api_version
        question = {
            "role": 'user',
            "content": content
        }
        self.messages.append(question)
        response = openai.ChatCompletion.create(
            engine=self.deployment_name,
            # 对话列表
            messages=self.messages
        )
        answer = response.choices[0].message.content
        answer_obj = {
            "role": 'assistant',
            "content": answer
        }
        self.messages.append(answer_obj)
        return answer








