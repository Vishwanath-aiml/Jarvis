# from ollama import chat

# def ask(question):

#     stream = chat(
#         model = "qwen3:4b-instruct",
#         messages = [
#             {
#             "role": "system",
#             "content": "You are Jarvis. Never mention Qwen or Alibaba. Keep replies under 2 sentences."
#             },
#             {
#                 "role": "user",
#                 "content" : question
#             }
#         ],
#         options={
#             "num_ctx": 4096,
#             "num_predict": 20,
#             "temperature": 0,
#             "num_thread": 8
#         },
#         stream = True
#     )

#     answer = ""
#     for chunk in stream:
#         piece = chunk.message.content
#         print(piece, end = "", flush = True)
#         answer += piece

#     print()

#     return answer

import time
from ollama import chat

def ask(question):

    start = time.perf_counter()

    stream = chat(
        model="qwen3:4b",
        messages=[
            {"role": "user", "content": question}
        ],
        stream=True
    )

    print(f"chat() returned: {time.perf_counter() - start:.3f}s")

    first = True

    for chunk in stream:

        if first:
            print(f"FIRST CHUNK: {time.perf_counter() - start:.3f}s")
            first = False

        print(chunk.message.content, end="", flush=True)

    print()