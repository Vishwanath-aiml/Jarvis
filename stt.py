import numpy as np
from sounddevice import InputStream
from moonshine_voice import ( 
    Transcriber,
    TranscriptEventListener,  # Parent module for encapsulation
    get_model_for_language, # Choosing the model with the language
    ModelArch  # To choose the model architecture
)

print(1)
model_path, model_arch = get_model_for_language("en", ModelArch.MEDIUM_STREAMING)
transcriber = Transcriber(model_path = model_path, model_arch = model_arch)


# the guy who listens the audio from the mic
class Listener(TranscriptEventListener):
    """
    - Prints the audio while it is being transcribed.
    - On completiong of a line it prints it with a starter "Final:"

    """

    def on_line_text_changed(self, event):
        print(event.line.text)

    def on_line_completed(self, event):
        print(f"Final: {event.line.text} ")


listener = Listener()
# letting transcriber know this guy will listen to the input audio
transcriber.add_listener(listener)

# Starting the moonshine in start, so it doesnt cause restart delay every time
transcriber.start()
print(2)

# The user defined function that gets called on voice input
def callback(indata, frames, time, status):
    """
    - This takes in the audio and calculates the RMS
    - If it crosses the 5th percentile of observed auido
    - If greater, then it will pass it to the moonshine model
    - Else just skips it

    """

    # level = np.sqrt(np.mean(indata**2))
    # if level > np.float32(0.0001954533):
    #     # add_audio doesn't take numpy 2d arrays, so we need to flatten them
    #     # Converting to list as the array contains np.float which again not supported
    #     audio = indata[:, 0].tolist()
    #     transcriber.add_audio(audio)
    audio = indata[:, 0].tolist()
    transcriber.add_audio(audio)


stream = InputStream(
    samplerate = 16000,  # Number of frames
    dtype = 'float32',
    channels = 1,
    callback = callback,
    blocksize = 800  # No of frames sent to callback at once
)

stream.start()
print(3)

# This block exists so the program doesnt end, else the mic stops instantly to execute the next line
try:
    while True:
        pass
except KeyboardInterrupt:
    stream.stop()
    stream.close()
    print(4)





