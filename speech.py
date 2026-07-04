import sounddevice as sd
import soundfile as sf
from datetime import datetime

SAMPLERATE = 16000 # The frequency it will read
CHANNELS = 1

def record_audio(duration = 5):
    filename = datetime.now().strftime("%Y%m%d_%H%M%S.wav")
    print("Recording....")

    recording = sd.rec(
        int(duration*SAMPLERATE),
        samplerate = SAMPLERATE,
        channels = CHANNELS,
        dtype = "float32"
    )

    sd.wait()  # Wait for the input

    sf.write(filename, recording, SAMPLERATE)

    print("Recording Saved:", filename)

    return filename