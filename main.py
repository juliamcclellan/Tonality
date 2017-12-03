import json

from file_processor import open_file
from audio_parse import parse_audio
from watson import analyze

audio = open_file('resources', 'audio.raw')
parsed = parse_audio(audio)

for result in parsed:
    tone = analyze(result.alternatives[0].transcript)
    print(json.dumps(tone, indent=2))
