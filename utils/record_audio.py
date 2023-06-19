class AudioData:
    def __init__(self, frames, sample_size, channels, rate):
        self.frames = frames
        self.sample_size = sample_size
        self.channels = channels
        self.rate = rate


def record_audio() -> AudioData:
    import pyaudio

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()

    print("Recording")

    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    frames = []
    seconds = 3

    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Finished recording")

    audio_data = AudioData(frames, p.get_sample_size(FORMAT), CHANNELS, RATE)

    return audio_data
