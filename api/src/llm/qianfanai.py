from typing import (
    Callable,
    List,
)

import qianfan
import tiktoken
from llm.basellm import BaseLLM
from retry import retry

class QianFanChat(BaseLLM):
    """Wrapper around OpenAI Chat large language models."""

    def __init__(
        self,
        access_key: str,
        secret_key: str,
        model_name: str = "Yi-34B-Chat",
        temperature: float = 0.01,
    ) -> None:
        self.access_key = access_key
        self.secret_key = secret_key
        self.temperature = temperature
        self.model = model_name

    def generate(self,messages: List[str],) -> str:
        chat_comp = qianfan.ChatCompletion(access_key=self.access_key, secret_key=self.secret_key)
        completions = chat_comp.do(
                model=self.model,
                temperature=self.temperature,
                messages=messages,
            )
        return completions["result"]
    async def generateStreaming(
        self,
        messages: List[str],
        onTokenCallback=Callable[[str], None],
    ) -> str:
        chat_comp = qianfan.ChatCompletion(access_key=self.access_key, secret_key=self.secret_key)
        result = []
        completions = chat_comp.do(
            model=self.model,
            temperature=self.temperature,
            messages=messages,
            stream = True
        )
        result = []
        for message in completions:
            # Process the streamed messages or perform any other desired action
            delta = message["choices"][0]["delta"]
            if "content" in delta:
                result.append(delta["content"])
            await onTokenCallback(message)
        return result

    def num_tokens_from_string(self, string: str) -> int:
        encoding = tiktoken.encoding_for_model(self.model)
        num_tokens = len(encoding.encode(string))
        return num_tokens

    def max_allowed_token_length(self) -> int:

        return 2049
