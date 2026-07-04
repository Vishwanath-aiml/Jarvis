from speech import record_audio
from transcriber import transcribe
from brain import ask
import time

audio = record_audio()

t = time.time()
question = transcribe(audio)
print("Whisper:", time.time()-t)

print(question)

t = time.time()
answer = ask(question)
print("LLM:", time.time()-t)