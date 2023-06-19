def save_audio_to_file(file_path: str, frames, sample_size, channels, rate):
    import wave

    wf = wave.open(file_path, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(sample_size)
    wf.setframerate(rate)
    wf.writeframes(b"".join(frames))
    wf.close()
