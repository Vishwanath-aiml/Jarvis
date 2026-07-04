# Jarvis

## Attempt 1 – Offline Speech Pipeline

### Goal
Build the first version of an offline AI assistant.

### What I built
- Audio recording using sounddevice
- Offline transcription pipeline
- Initial experiments with Whisper

### Outcome
The prototype worked, but it wasn't suitable for my vision of real-time streaming speech recognition.

### Why it will be replaced
The architecture required processing completed audio instead of continuously understanding speech. The next attempt migrates to Moonshine's streaming transcription engine.

## External Dependencies

The following are intentionally **not** included in this repository.

### Whisper Model

Place the model here:

```
Models/whisper/ggml-small.en-q5_1.bin
```

### whisper.cpp

Extract the Windows release here:

```
tools/whisper-bin-x64/
```