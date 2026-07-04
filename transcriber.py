import subprocess

WHISPER = r"E:\Projects\Jarvis\tools\whisper-bin-x64\Release\whisper-cli.exe"
MODEL = r"E:\Projects\Jarvis\Models\whisper\ggml-small.en-q5_1.bin"

def transcribe(audio_path):
    result = subprocess.run(
        [
            WHISPER,
            "-m", MODEL,
            "-f", audio_path,
            "-ng"
        ],
        capture_output = True,
        text = True
    )
    
    text = result.stdout

    if "]" in text:
        text = text.split("]", 1)[1]

    return text.strip() 