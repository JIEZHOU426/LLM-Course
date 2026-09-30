import configparser
from openai import OpenAI

config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")

client = OpenAI(api_key=config["LLM"]["api_key"], base_url="https://api.deepseek.com/v1")

question = input("请输入问题: ")

print("---")
stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": question}],
    stream=True,
)
for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
print()
print("---")
