import env
import speech_to_text as stt
import assistant.assistant as assistant
from utils.record_audio import record_audio
from utils.save_audio_to_file import save_audio_to_file

AUDIO_FILE_PATH = "test.wav"

audio = record_audio()

save_audio_to_file(
    file_path=AUDIO_FILE_PATH,
    frames=audio.frames,
    sample_size=audio.sample_size,
    channels=audio.channels,
    rate=audio.rate,
)

transcription = stt.transcript(AUDIO_FILE_PATH)

response = assistant.ask_assistant(transcription)

print(response)
